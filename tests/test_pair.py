import io
import sys
import pytest

import zeroless_tools

from zeroless_tools import helpers
from zeroless_tools import server
from zeroless_tools import client
from zeroless_tools import SocketExecutor

class TestPair:
    def test_executors(self):
        server_socket_executor = zeroless_tools.server.zeroserver('7731 pair read-only'.split())
        client_socket_executor = zeroless_tools.client.zeroclient('7731 pair write-only'.split())

        assert isinstance(server_socket_executor, SocketExecutor.ReadOnlyPairExecutor)
        assert isinstance(client_socket_executor, SocketExecutor.WriteOnlyPairExecutor)

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

            server_socket_executor = zeroless_tools.server.zeroserver('7732 pair read-only'.split())
            client_socket_executor = zeroless_tools.client.zeroclient('7732 pair write-only'.split())

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

            server_socket_executor = zeroless_tools.server.zeroserver('7733 pair write-only'.split())
            client_socket_executor = zeroless_tools.client.zeroclient('7733 pair read-only'.split())

            helpers.run(server_socket_executor)
            helpers.run(client_socket_executor)

            output.seek(0)
            received_msgs = output.readlines()

        finally:
            sys.stdin = stdin_old
            sys.stdout = stdout_old

        assert msg == received_msgs