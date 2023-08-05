# -*- coding: utf-8 -*- {{{
# ===----------------------------------------------------------------------===
#
#                 Installable Component of Eclipse VOLTTRON
#
# ===----------------------------------------------------------------------===
#
# Copyright 2022 Battelle Memorial Institute
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# ===----------------------------------------------------------------------===
# }}}

import base64
import glob
import hashlib
import logging
import os
import shutil
from pathlib import Path
import sys
import tempfile

import gevent
import yaml

from volttron.client.vip.agent.results import AsyncResult

from volttron.utils import (
    execute_command, )
from volttron.utils import jsonapi

# from volttron.platform import agent, config, jsonapi, get_home
# from volttron.platform.agent.utils import execute_command
# from volttron.platform.packaging import add_files_to_package, create_package


class InstallRuntimeError(RuntimeError):
    pass


_log = logging.getLogger(__name__)

_stdout = sys.stdout
_stderr = sys.stderr


def install_requirements(agent_source):
    req_file = os.path.join(agent_source, "requirements.txt")

    if os.path.exists(req_file):
        _log.info(f"Installing requirements for agent from {req_file}.")
        cmds = ["pip", "install", "-r", req_file]
        try:
            execute_command(cmds, logger=_log, err_prefix="Error installing requirements")
        except InstallRuntimeError:
            sys.exit(1)


def install_agent_directory(opts, publickey=None, secretkey=None):
    """
    The main installation method for installing the agent on the correct local
    platform instance.
    :param opts:
    :param package:
    :param agent_config:
    :return:
    """
    if os.path.isfile(os.path.join(opts.install_path, "setup.py")):
        if os.path.isfile(os.path.join(opts.install_path, "Pipfile")):
            cmd = ["pipenv", "run", "python3", "setup.py", "bdist_wheel"]
        else:
            cmd = ["python3", "setup.py", "bdist_wheel"]
    elif os.path.isfile(os.path.join(opts.install_path, "pyproject.toml")):
        cmd = ["poetry", "build"]
    else:
        raise InstallRuntimeError(
            f"Unable to build file. No setup.py or poetry.lock file exists in {opts.install_path}")
    output = execute_command(cmd, cwd=opts.install_path)
    # wheel should be in dist dir
    dist_path = os.path.abspath(os.path.join(opts.install_path, "dist"))
    match = glob.glob(os.path.join(dist_path, "*.whl"))
    if match:
        opts.package = match[0]
    else:
        raise InstallRuntimeError(
            f"No .whl file found in {dist_path} after running command {' '.join(cmd)}. "
            f"\nCommand returned stdout:\n{output}")

    # TODO: does pipenv handle this. Does whl contain requirements.txt
    # assert opts.connection, "Connection must have been created to access this feature."
    #
    # if not opts.skip_requirements:
    #     install_requirements(opts.install_path)
    #

    if not opts.vip_identity:
        agent_default_id_file = Path(opts.install_path).joinpath("IDENTITY")
        if agent_default_id_file.is_file():
            with open(str(agent_default_id_file)) as fin:
                opts.vip_identity = fin.read().strip()

    _send_and_intialize_agent(opts, publickey, secretkey)


def _send_and_intialize_agent(opts, publickey, secretkey):

    # Verify and load agent_config up from the opts.  agent_config will
    # be a yaml config file.
    agent_config = opts.agent_config
    if agent_config is None:
        agent_config = {}

    # if not a dict then config should be a filename
    if not isinstance(agent_config, dict):
        config_file = agent_config
        if not Path(config_file).exists():
            raise InstallRuntimeError(f"Config file {config_file} does not exist!")
    else:
        cfg = tempfile.NamedTemporaryFile()
        with open(cfg.name, "w") as fout:
            fout.write(yaml.safe_dump(agent_config))
        config_file = cfg.name

    try:
        with open(config_file) as fp:
            config_dict = yaml.safe_load(fp)
    except Exception as exc:
        raise InstallRuntimeError(exc)

    agent_uuid = send_agent(
        opts.connection,
        opts.package,
        opts.vip_identity,
        publickey,
        secretkey,
        opts.force,
        config_dict,
    )

    if not agent_uuid:
        raise ValueError(f"Agent was not installed properly.")

    if isinstance(agent_uuid, AsyncResult):
        agent_uuid = agent_uuid.get()

    output_dict = dict(agent_uuid=agent_uuid)

    if opts.tag:
        _log.debug(f"Tagging agent {agent_uuid}, {opts.tag}")
        opts.connection.call("tag_agent", agent_uuid, opts.tag)
        output_dict["tag"] = opts.tag

    if opts.enable or opts.priority != -1:
        output_dict["enabling"] = True
        if opts.priority == -1:
            opts.priority = "50"
        _log.debug(f"Prioritinzing agent {agent_uuid},{opts.priority}")
        output_dict["priority"] = opts.priority

        opts.connection.call("prioritize_agent", agent_uuid, str(opts.priority))

    try:

        if opts.start:
            gevent.sleep(2)
            _log.debug(f"Staring agent {agent_uuid}")
            opts.connection.call("start_agent", agent_uuid)
            output_dict["starting"] = True

            _log.debug(f"Getting agent status {agent_uuid}")
            gevent.sleep(opts.agent_start_time)
            status = opts.connection.call("agent_status", agent_uuid)
            if status[0] is not None and status[1] is None:
                output_dict["started"] = True
                output_dict["pid"] = status[0]
            else:
                output_dict["started"] = False
            _log.debug(f"Status returned {status}")
    except Exception as e:
        _log.error(e)

    if opts.json:
        sys.stdout.write("%s\n" % jsonapi.dumps(output_dict, indent=4))
    else:
        if output_dict.get("started"):
            sys.stdout.write(f"Agent {agent_uuid} installed and started [{output_dict['pid']}]\n")
        else:
            sys.stdout.write(f"Agent {agent_uuid} installed\n")
    if opts.csv:
        keylen = len(output_dict)
        keyline = ""
        valueline = ""
        keys = list(output_dict.keys())
        for k in range(keylen):
            if k < keylen - 1:
                keyline += "%s," % keys[k]
                valueline += "%s," % output_dict[keys[k]]
            else:
                keyline += "%s" % keys[k]
                valueline += "%s" % output_dict[keys[k]]
        sys.stdout.write("%s\n%s\n" % (keyline, valueline))


def install_agent_vctl(opts, publickey=None, secretkey=None, callback=None):
    """
    The `install_agent_vctl` function is called from the volttron-ctl or vctl install
    sub-parser.
    """
    try:
        install_path = opts.install_path
    except AttributeError:
        install_path = opts.wheel

    # TODO move to server
    # if opts.vip_identity:
    #     # First check to see if we have an identity already if it does and force is specified
    #     # then we can send things across and it will be handled on the server side.
    #     if opts.connection.call("identity_exists", opts.vip_identity):
    #         if not opts.force:
    #             opts.connection.kill()
    #             raise InstallRuntimeError("Identity already exists.  Pass --force option to re-install.")
    pip_download_dir = None
    if os.path.isdir(install_path):
        install_agent_directory(opts, publickey, secretkey)
        if opts.connection is not None:
            opts.connection.kill()
    else:
        opts.package = opts.install_path
        if not os.path.exists(opts.package):
            if os.path.dirname(opts.package) == "":
                # no path prefix only a name and name is not a local file.
                # check if you can download from pip
                pip_download_dir = tempfile.mkdtemp()
                try:
                    execute_command([
                        "pip",
                        "download",
                        "--no-deps",
                        "--dest",
                        pip_download_dir,
                        opts.package,
                    ])
                    # there should be a single wheel file in dir
                    opts.package = os.path.join(pip_download_dir, os.listdir(pip_download_dir)[0])
                except RuntimeError as r:
                    raise InstallRuntimeError(
                        f" Invalid wheel {opts.package}. It is not a local wheel file. Error"
                        f"downloading {opts.package} from pip")

            else:
                opts.connection.kill()
                raise FileNotFoundError(f"Invalid file {opts.package}")
        _send_and_intialize_agent(opts, publickey, secretkey)
        if pip_download_dir:
            shutil.rmtree(pip_download_dir)


def send_agent(
    connection: "ControlConnection",
    wheel_file: str,
    vip_identity: str,
    publickey: str,
    secretkey: str,
    force: bool,
    agent_config: dict,
):
    """
    Send an agent wheel from the client to the server.

    The `ControlConnection` uses a protocol to send the wheel across the wire to the 'ControlService`.
    """
    path = wheel_file
    peer = connection.peer
    server = connection.server
    _log.debug(f"server type is {type(server)} {type(server.core)}")

    wheel = open(path, "rb")
    _log.debug(f"Connecting to {peer} to install {path}")
    channel = None
    rmq_send_topic = None
    rmq_response_topic = None

    if server.core.messagebus == "zmq":
        channel = server.vip.channel(peer, "agent_sender")
    elif server.core.messagebus == "rmq":
        rmq_send_topic = "agent_sender"
        rmq_response_topic = "request_data"
    else:
        raise ValueError("Unknown messagebus detected")

    def send_rmq():
        nonlocal wheel, server

        sha512 = hashlib.sha512()
        protocol_message = None
        protocol_headers = None
        response_received = False

        def protocol_requested(peer, sender, bus, topic, headers, message):
            nonlocal protocol_message, protocol_headers, response_received

            protocol_message = message
            protocol_message = base64.b64decode(protocol_message.encode("utf-8"))
            protocol_headers = headers
            response_received = True

        try:
            first = True
            op = None
            size = None
            _log.debug(f"Subscribing to {rmq_response_topic}")
            server.vip.pubsub.subscribe(
                peer="pubsub",
                prefix=rmq_response_topic,
                callback=protocol_requested,
            ).get(timeout=5)
            gevent.sleep(5)
            _log.debug(f"Publishing to {rmq_send_topic}")
            while True:
                if first:
                    _log.debug("Waiting for a fetch")
                    # Wait until we get the first request.
                    with gevent.Timeout(30):
                        while not response_received:
                            gevent.sleep(0.1)

                    first = False
                    resp = jsonapi.loads(protocol_message)
                    _log.debug(f"Got first response {resp}")

                    if len(resp) > 1:
                        op, size = resp
                    else:
                        op = resp[0]

                    if op != "fetch":
                        raise ValueError(f"First channel response must be fetch but was {op}")
                response_received = False
                if op == "fetch":
                    chunk = wheel.read(size)
                    if chunk:
                        _log.debug(f"Op was fetch sending {size}")
                        sha512.update(chunk)
                        # Needs a string to go across the messagebus.
                        message = base64.b64encode(chunk).decode("utf-8")
                        server.vip.pubsub.publish(
                            peer="pubsub",
                            topic=rmq_send_topic,
                            message=message,
                        ).get(timeout=10)
                    else:
                        _log.debug(f"Op was fetch sending complete")
                        message = base64.b64encode(b"complete").decode("utf-8")
                        server.vip.pubsub.publish(
                            peer="pubsub",
                            topic=rmq_send_topic,
                            message=message,
                        ).get(timeout=10)
                        gevent.sleep(10)
                        break
                elif op == "checksum":
                    _log.debug(f"sending checksum {sha512.hexdigest()}")
                    message = base64.b64encode(sha512.digest()).decode("utf-8")
                    server.vip.pubsub.publish("pubsub", topic=rmq_send_topic,
                                              message=message).get(timeout=10)

                _log.debug("Waiting for next response")

                with gevent.Timeout(30):
                    while not response_received:
                        gevent.sleep(0.1)
                _log.debug(f"Response received bottom of loop {protocol_message}")
                # wait for next response
                resp = jsonapi.loads(protocol_message)

                # [fetch, size] or checksum
                if len(resp) > 1:
                    op, size = resp
                else:
                    op = resp[0]

        finally:
            _log.debug("Closing wheel and unsubscribing.")
            wheel.close()
            server.vip.pubsub.unsubscribe(
                peer="pubsub",
                prefix="rmq_response_topic",
                callback=protocol_requested,
            )

    def send_zmq():
        nonlocal wheel, channel
        sha512 = hashlib.sha512()
        try:
            first = True
            op = None
            size = None
            while True:
                if first:
                    first = False
                    # Wait for peer to open compliment channel
                    resp = jsonapi.loadb(channel.recv())
                    _log.debug(f"Got first response {resp}")

                    if len(resp) > 1:
                        op, size = resp
                    else:
                        op = resp[0]

                    if op != "fetch":
                        raise ValueError(f"First channel response must be fetch but was {op}")

                if op == "fetch":
                    chunk = wheel.read(size)
                    if chunk:
                        _log.debug(f"Op was fetch sending {size}")
                        sha512.update(chunk)
                        _log.debug(f"Sending chunk:\n{chunk}")
                        channel.send(chunk)
                    else:
                        _log.debug(f"Op was fetch sending complete")
                        channel.send(b"complete")
                        gevent.sleep(10)
                        break
                elif op == "checksum":
                    _log.debug(f"sending checksum {sha512.hexdigest()}")
                    channel.send(sha512.digest())

                _log.debug("Waiting for next response")
                # wait for next response
                resp = jsonapi.loadb(channel.recv())

                if len(resp) > 1:
                    op, size = resp
                else:
                    op = resp[0]

        finally:
            _log.debug("Closing wheel and channel.")
            wheel.close()
            channel.close(linger=0)
            del channel

    if server.core.messagebus == "rmq":
        _log.debug(f"calling install_agent on {peer} sending to topic {rmq_send_topic}")
        task = gevent.spawn(send_rmq)
        # TODO: send config
        result = server.vip.rpc.call(
            peer,
            "install_agent_rmq",
            os.path.basename(path),
            rmq_send_topic,
            vip_identity,
            publickey,
            secretkey,
            force,
            agent_config,
            rmq_response_topic,
        )
    elif server.core.messagebus == "zmq":
        _log.debug(f"calling install_agent on {peer} using channel {channel.name}")
        task = gevent.spawn(send_zmq)
        result = server.vip.rpc.call(
            peer,
            "install_agent",
            os.path.basename(path),
            channel.name,
            vip_identity,
            publickey,
            secretkey,
            force,
            agent_config,
        )

    else:
        raise ValueError("Unknown messagebus detected!")

    result.rawlink(lambda glt: task.kill(block=False))
    # Allows larger files to be sent across the message bus without
    # raising an error.
    gevent.wait([result], timeout=300)
    _log.debug("Completed sending of agent across.")
    _log.debug(f"After wait result is {result}")
    return result


# def send_agent(connection, wheel_file, vip_identity, publickey, secretkey, force):

#     #for wheel in opts.wheel:
#     #uuid = _send_agent(connection.server, connection.peer, wheel_file).get()
#     result = _send_agent(connection.server, connection.peer, wheel_file,
#                          vip_identity, publickey, secretkey, force)

#     _log.debug(f"Returning {result} from send_agent")
#     return result


def add_install_agent_parser(add_parser_fn):
    install = add_parser_fn(
        "install",
        help="install agent from wheel",
        epilog="Optionally you may specify the --tag argument to tag the "
        "agent during install without requiring a separate call to "
        "the tag command. ",
    )
    install.add_argument(
        "--skip-requirements",
        help=
        "Skip installing requirements from a requirements.txt if present in the agent directory.",
    )
    install.add_argument(
        "install_path",
        help="path to agent wheel or directory for agent installation",
    )
    install.add_argument("--tag", help="tag for the installed agent")
    install.add_argument(
        "--vip-identity",
        help="VIP IDENTITY for the installed agent. "
        "Overrides any previously configured VIP IDENTITY.",
    )
    install.add_argument("--agent-config", help="Agent configuration!")
    install.add_argument(
        "-f",
        "--force",
        action="store_true",
        help=
        "agents are uninstalled by tag so force allows multiple agents to be removed at one go.",
    )
    install.add_argument(
        "--priority",
        default=-1,
        type=int,
        help="priority of startup during instance startup",
    )
    install.add_argument(
        "--start",
        action="store_true",
        help="start the agent during the script execution",
    )
    install.add_argument(
        "--enable",
        action="store_true",
        help="enable the agent with default 50 priority unless --priority set",
    )
    install.add_argument(
        "--csv",
        action="store_true",
        help="format the standard out output to csv",
    )
    install.add_argument(
        "--json",
        action="store_true",
        help="format the standard out output to json",
    )
    install.add_argument(
        "-st",
        "--agent-start-time",
        default=5,
        type=int,
        help="the amount of time to wait and verify that the agent has started up.",
    )

    install.set_defaults(func=install_agent_vctl, verify_agents=True)
