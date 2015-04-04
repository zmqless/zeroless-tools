import sys
import io

import pytest

from zeroless import (Server, Client)
from zeroless_tools import (helpers)

@pytest.fixture(scope="module")
def listen_for_push():
    return Server(port=7892).pull()

@pytest.fixture(scope="module")
def push():
    client = Client()
    client.connect_local(port=7892)
    return client.push()

class TestReqRep:
    def test_communication(self, push, listen_for_push):
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
            helpers.wait_and_write(push, 1)
            helpers.read_and_print(listen_for_push)
            output.seek(0)
            received_msgs = output.readlines()

        finally:
            sys.stdin = stdin_old
            sys.stdout = stdout_old

        assert msg == received_msgs

    def test_multipart_communication(self, push, listen_for_push):
        msgs = ['msg1' + str(i) + '\n' for i in range(10)]

        stdin_old = sys.stdin
        stdout_old = sys.stdout

        try:
            input = io.StringIO()
            output = io.StringIO()

            sys.stdin = input
            sys.stdout = output

            input.writelines(msgs)
            input.seek(0)
            helpers.wait_and_write(push, len(msgs))
            helpers.read_and_print(listen_for_push, len(msgs))
            output.seek(0)
            received_msgs = output.readlines()

        finally:
            sys.stdin = stdin_old
            sys.stdout = stdout_old

        assert msgs == received_msgs