import io
import sys
import pytest

import zeroless_tools

from zeroless_tools import helpers
from zeroless_tools import server
from zeroless_tools import client
from zeroless_tools import SocketExecutor

class TestReqRep:
    def test_executors(self):
        server_socket_executor = zeroless_tools.server.zeroserver('7896 rep'.split())
        client_socket_executor = zeroless_tools.client.zeroclient('7896 req'.split())

        assert isinstance(server_socket_executor, SocketExecutor.RepExecutor)
        assert isinstance(client_socket_executor, SocketExecutor.ReqExecutor)