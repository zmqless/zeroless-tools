import sys

from .SocketExecutor import *

def pub(socket, args):
    return PubExecutor(socket, args.numParts, args.topic)

def sub(socket, args):
    return SubExecutor(socket, args.numParts, args.topics)

def push(socket, args):
    return PushExecutor(socket, args.numParts)

def pull(socket, args):
    return PullExecutor(socket, args.numParts)

def req(socket, args):
    return ReqExecutor(socket, args.numParts)

def rep(socket, args):
    return RepExecutor(socket, args.numParts)

def read_only_pair(socket, args):
    return ReadOnlyPairExecutor(socket, args.numParts)

def write_only_pair(socket, args):
    return WriteOnlyPairExecutor(socket, args.numParts)

def add_sender_command(subparser, name, description, callback):
    subparser = subparser.add_parser(name, description=description)
    subparser.set_defaults(socket_executor=callback)
    return subparser

def add_receiver_command(subparser, name, description, callback):
    subparser = subparser.add_parser(name, description=description)
    subparser.set_defaults(socket_executor=callback)
    return subparser

def add_sub_commands(parser):
    parser.epilog = """This program is free software: you can redistribute it and/or modify it under the terms
                    of the GNU General Public License as published by the Free Software Foundation, either
                    version 3 of the License, or (at your option) any later version"""

    parser.add_argument('port', type=int,
                        choices=range(1024,65535), metavar="[a port between 1024 and 65535]",
                        help='the open port to bind/connect to')

    parser.add_argument('-n', '--numParts', metavar="amount of parts", type=int, default=1,
                        help='the amount of parts (i.e. frames) per message (default=1)')

    subparsers = parser.add_subparsers(title='messaging pattern',
                                       description='''The ØMQ API implements several messaging patterns, each
                                                   one defining a particular network topology''',
                                       help='''Choose among Publish/Subscribe (Pub/Sub), Request/Reply (Req/Rep),
                                            Pipeline (Push/Pull) and Exclusive Pair (Pair)''')

    parser_pub = add_sender_command(subparsers, 'pub', 'This is a data distribution pattern', pub)
    parser_pub.add_argument('-t', '--topic', type=str, default='',
                            help='the topic that messages are published to (default=all)')

    parser_sub = add_receiver_command(subparsers, 'sub', 'This is a data distribution pattern', sub)
    parser_sub.add_argument('-t', '--topics', type=list, default=[''],
                            help='the list of topics to subscribe to (default=all)')

    parser_push = add_sender_command(subparsers, 'push',
                                     'This is a parallel task distribution and collection pattern', push)
    parser_pull = add_receiver_command(subparsers, 'pull',
                                       'This is a parallel task distribution and collection pattern', pull)
    parser_req = add_sender_command(subparsers, 'req',
                                    'This is a remote procedure call and task distribution pattern', req)
    parser_rep = add_receiver_command(subparsers, 'rep',
                                      'This is a remote procedure call and task distribution pattern', rep)

    parser_pair = subparsers.add_parser('pair',
                                        description='This is an advanced low-level pattern for specific use cases')

    pair_subparsers = parser_pair.add_subparsers(title='mode',
                                                 description='the mode of operation of the Exclusive Pair pattern',
                                                 help='Due to a current limitation, you cannot read and write '
                                                      'at the same Exclusive Pair connection')

    parser_write_only_pair = add_sender_command(pair_subparsers,
                                                'write-only', '',
                                                write_only_pair)

    parser_read_only_pair = add_receiver_command(pair_subparsers,
                                                 'read-only', '',
                                                 read_only_pair)

def run(socket_executor):
    try:
        socket_executor.execute()
    except EOFError:
        sys.exit()
    except KeyboardInterrupt:
        print()
        print('You pressed Ctrl+C!')
        sys.exit()