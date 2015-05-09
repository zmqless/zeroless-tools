import io
import sys
import pytest

import zeroless_tools

from zeroless_tools import helpers
from zeroless_tools import server
from zeroless_tools import client
from zeroless_tools import SocketExecutor

class TestPushPull:
    def test_executors(self):
        server_socket_executor = zeroless_tools.server.zeroserver('7891 pull'.split())
        client_socket_executor = zeroless_tools.client.zeroclient('7891 push'.split())

        assert isinstance(server_socket_executor, SocketExecutor.PullExecutor)
        assert isinstance(client_socket_executor, SocketExecutor.PushExecutor)

    def test_client_to_server(self):
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

            server_socket_executor = zeroless_tools.server.zeroserver('7892 pull'.split())
            client_socket_executor = zeroless_tools.client.zeroclient('7892 push'.split())

            helpers.run(client_socket_executor)
            helpers.run(server_socket_executor)

            output.seek(0)
            received_msgs = output.readlines()

        finally:
            sys.stdin = stdin_old
            sys.stdout = stdout_old

        assert msg == received_msgs

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

            server_socket_executor = zeroless_tools.server.zeroserver('7892 push'.split())
            client_socket_executor = zeroless_tools.client.zeroclient('7892 pull'.split())

            helpers.run(server_socket_executor)
            helpers.run(client_socket_executor)

            output.seek(0)
            received_msgs = output.readlines()

        finally:
            sys.stdin = stdin_old
            sys.stdout = stdout_old

        assert msg == received_msgs