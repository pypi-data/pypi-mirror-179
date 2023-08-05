import argparse
import logging

from visionaire4 import export, restore

class VersionAction(argparse.Action):
    """Shows version and exits."""

    def __call__(self, parser, namespace, values, option_string=None):
        import sys
        from visionaire4.version import __version__
        print(__version__)
        sys.exit(0)

def get_main_parser():
    parent_parser = argparse.ArgumentParser(add_help=False)

    log_level_group = parent_parser.add_mutually_exclusive_group()
    log_level_group.add_argument(
        "-v", "--verbose", action="count", default=0,
        help="Increase verbosity. Option is additive up to 3 times, e.g. `-vv`"
    )
    log_level_group.add_argument(
        "-q", "--quiet", action="count", default=0,
        help="Be more quiet. Option is additive up to 2 times."
    )

    parser = argparse.ArgumentParser(
        prog="visionaire4",
        description="Visionaire4 maintenance tools.",
        parents=[parent_parser],
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--version", nargs=0, action=VersionAction, help="Show tool version.")

    subparser = parser.add_subparsers(
        title="Available Commands",
        metavar="COMMAND",
        dest="cmd",
        help="Use `visionaire4 COMMAND --help` for command-specific help."
    )
    subparser.required = True
    subparser.dest = "cmd"

    export.add_parser(subparser, parent_parser)
    restore.add_parser(subparser, parent_parser)
    return parser

def main():
    parser = get_main_parser()
    args = parser.parse_args()

    level = logging.INFO
    if args.quiet == 1:
        level = logging.WARNING
    elif args.quiet >= 2:
        level = logging.ERROR
    elif args.verbose == 1:
        level = logging.DEBUG
    logging.basicConfig(
        level=level,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    args.func(args)

if __name__ == "__main__":
    main()
