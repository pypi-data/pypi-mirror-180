import argparse

from panoptisch.lib_resolver import get_stdlib_dir
from panoptisch.scanner import run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'module',
        action='store',
        help='Name of module or file you wish to scan.',
    )
    parser.add_argument(
        '--show-stdlib-dir',
        action='store_true',
        help='Prints the automatically resolved stdlib directory.',
    )
    parser.add_argument(
        '--max-depth',
        type=int,
        action='store',
        help='Maximum dependency depth.',
        default=3,
    )
    parser.add_argument(
        '--out',
        action='store',
        help='File to output report.',
        default='out.json',
    )
    parser.add_argument(
        '--auto-stdlib-dir',
        action='store_true',
        help='Ignore stdlib modules by automatically resolving their path. MAY BE BUGGY. Try running panoptisch <module_name> --show-stdlib-dir to see the directory before using this.',  # noqa E501
    )
    parser.add_argument(
        '--stdlib-dir',
        type=str,
        action='store',
        help='Ignore stdlib modules by providing their path',
    )
    parser.add_argument(
        '--omit-not-found',
        action='store_true',
        help='Do not include modules that could not be resolved in report',
    )
    args = parser.parse_args()
    if args.show_stdlib_dir:
        print(get_stdlib_dir())
    else:
        if args.auto_stdlib_dir:
            args.stdlib_dir = get_stdlib_dir()
        run(args)


__all__ = ['main']
