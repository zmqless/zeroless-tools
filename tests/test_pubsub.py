import io
import sys
import pytest

import zeroless_tools

from time import sleep

from zeroless_tools import helpers
from zeroless_tools import server
from zeroless_tools import client
from zeroless_tools import SocketExecutor

class TestPubSub:
    def test_executors(self):
        server_socket_executor = zeroless_tools.server.zeroserver('7721 pub'.split())
        client_socket_executor = zeroless_tools.client.zeroclient('7721 sub'.split())

        assert isinstance(server_socket_executor, SocketExecutor.PubExecutor)
        assert isinstance(client_socket_executor, SocketExecutor.SubExecutor)

    def test_server_to_client(self):
        msg = ['msg1\n']

        stdin_old = sys.stdin
        stdout_old = sys.stdout

        try:
            input = io.StringIO()
            output = io.StringIO()

            sys.stdin = input
            sys.stdout = output

            input.writelines(msg)
            input.seek(0)

            server_socket_executor = zeroless_tools.server.zeroserver('7722 pub'.split())
            client_socket_executor = zeroless_tools.client.zeroclient('7722 sub'.split())

            sleep(0.1)
            helpers.run(server_socket_executor)
            helpers.run(client_socket_executor)

            output.seek(0)
            received_msgs = output.readlines()

        finally:
            sys.stdin = stdin_old
            sys.stdout = stdout_old

        assert msg == received_msgs