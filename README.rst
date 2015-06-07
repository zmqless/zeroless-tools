Zeroless Tools
==============

Most people used to networking programming are aware that NetCat is a very useful tool
to establish and test TCP/UDP connections on the fly. The ZeroMQ community, however, do
not provide an equivalent application. So that, in order to test your ZMQ sockets, you
would have to code your own solution. For tackling that issue, the Zeroless Command
Line Interface (CLI) was created.

So that you can test your 0MQ connections in a language agnostic fashion, despite the
used messaging pattern.

Installation
------------

.. _install_content_start:

.. code-block:: bash

    $ pip install zeroless_tools

.. _install_content_end:

Usage
-----

.. _usage_content_start:

.. code-block:: bash

    $ zeroserver -h

    usage: Zeroless Server Cli [-h] [-n amount of parts]
                               [a port between 1024 and 65535]
                               {rep,push,sub,pair,req,pub,pull} ...

    The Zeroless Server Cli shall create an endpoint for accepting connections
    and bind it to the chosen ØMQ messaging pattern

    positional arguments:
      [a port between 1024 and 65535]
                            the open port to bind/connect to

    optional arguments:
      -h, --help            show this help message and exit
      -n amount of parts, --numParts amount of parts
                            the amount of parts (i.e. frames) per message
                            (default=1)

    messaging pattern:
      The ØMQ API implements several messaging patterns, each one defining a
      particular network topology

      {rep,push,sub,pair,req,pub,pull}
                            Choose among Publish/Subscribe (Pub/Sub),
                            Request/Reply (Req/Rep), Pipeline (Push/Pull) and
                            Exclusive Pair (Pair)

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version

.. code-block:: bash

    $ zeroclient -h

    usage: Zeroless Client Cli [-h] [-i IP] [-n amount of parts]
                               [a port between 1024 and 65535]
                               {sub,push,pair,pull,req,rep,pub} ...

    The Zeroless Client Cli shall connect to the specified endpoint using the
    chosen ØMQ messaging pattern

    positional arguments:
      [a port between 1024 and 65535]
                            the open port to bind/connect to

    optional arguments:
      -h, --help            show this help message and exit
      -i IP, --ip IP        the IP of the endpoint to connect to
                            (default=127.0.0.1)
      -n amount of parts, --numParts amount of parts
                            the amount of parts (i.e. frames) per message
                            (default=1)

    messaging pattern:
      The ØMQ API implements several messaging patterns, each one defining a
      particular network topology

      {rep,push,sub,pair,req,pub,pull}
                            Choose among Publish/Subscribe (Pub/Sub),
                            Request/Reply (Req/Rep), Pipeline (Push/Pull) and
                            Exclusive Pair (Pair)

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version

.. _usage_content_end:

Testing
-------

.. _testing_content_start:

To run individual tests:

.. code-block:: bash

    $ py.test tests/test_desired_module.py

To run all the tests:

.. code-block:: bash

    $ python setup.py test

Alternatively, you can use tox:

.. code-block:: bash

    $ tox

.. _testing_content_end:

License
-------

.. _license_content_start:

Copyright 2014 Lucas Lira Gomes x8lucas8x@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

.. _license_content_end: