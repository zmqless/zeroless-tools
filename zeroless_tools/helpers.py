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

def add_sender_command(subparser, name, callback):
    subparser = subparser.add_parser(name)
    subparser.set_defaults(socket_executor=callback)
    return subparser

def add_receiver_command(subparser, name, callback):
    subparser = subparser.add_parser(name)
    subparser.set_defaults(socket_executor=callback)
    return subparser

def add_sub_commands(parser):
    parser.add_argument('port', action='store', type=int,
                        choices=range(1024,65535), metavar="[a port between 1024 and 65535]",
                        help='an open port in the provided IP')

    parser.add_argument('-n', '--numParts', type=int, default=1)

    subparsers = parser.add_subparsers(title='pattern',
                                       description='available pattern')

    parser_pub = add_sender_command(subparsers, 'pub', pub)
    parser_pub.add_argument('-t', '--topic', type=bytes, default=b'')

    parser_sub = add_receiver_command(subparsers, 'sub', sub)
    parser_sub.add_argument('-t', '--topics', type=list, default=[b''])

    parser_push = add_sender_command(subparsers, 'push', push)
    parser_pull = add_receiver_command(subparsers, 'pull', pull)
    parser_req = add_sender_command(subparsers, 'req', req)
    parser_rep = add_receiver_command(subparsers, 'rep', rep)

    parser_pair = subparsers.add_parser('pair')
    pair_subparsers = parser_pair.add_subparsers(title='pattern',
                                       description='available pattern')

    parser_write_only_pair = add_sender_command(pair_subparsers,
                                                'write-only',
                                                write_only_pair)

    parser_read_only_pair = add_receiver_command(pair_subparsers,
                                                 'read-only',
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