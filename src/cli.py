import argparse
from types import NoneType

from __init__ import __app_name__, __version__
from cpm import Cubase


__all__ = [
    "parse"
]


def __create_parser(cb: Cubase):
    """
    Returns a parser object with defined arguments.
    """
    parser = argparse.ArgumentParser(prog=__app_name__, 
                                     description="Enables easy switching between multiple Cubase preferences folders.")

    parser.add_argument("-v", "--version", 
                        action="version", 
                        version=f"{__app_name__} v{__version__}")

    parser.add_argument("-V", "--cubase-version", 
                        help="Specifies the Cubase version, the preferences of which will be replaced by custom preferences. If not supplied, the most recent version of Cubase will be targetted.",
                        choices=[str(a.version) for a in cb.apps],
                        default=None, 
                        required=False)

    parser.add_argument("-c", "--list-cubase-versions",
                        help="Lists which versions of Cubase are installed and exits (* specifies currently-selected).",
                        default=None,
                        action="store_true",
                        required=False)

    # TODO: subparsers:
    #   -c, --custom: Lists only custom configs.
    #   -s, --stock: Lists only stock configs.
    parser.add_argument("-p", "--list-cubase-preferences", 
                        help="Lists available Cubase preferences (* specifies active).",
                        action="store_true",
                        required=False)

    # TODO:
    parser.add_argument("-a", "--set-active",
                        help="Specify which preferences to use (requires path to new config, or name of already-stored config). If `--cubase-version` is not supplied, latest version is chosen.",
                        default=cb.latest,
                        required=False)

    # TODO:
    parser.add_argument("-s", "--store",
                        help="Store a new config to disk (requires path and name).",
                        default=None,
                        required=False)

    # TODO:
    parser.add_argument("-i", "--import",
                        help="Imports a new config from disk to store (requires path or name)",
                        required=False)

    # TODO:
    parser.add_argument("-d", "--delete-from-store",
                        help="Deletes a config from store (requires path or name)",
                        required=False)

    # TODO:
    parser.add_argument("-D", "--delete-from-disk",
                        help="Deletes a config from store and disk (requires path or name)",
                        required=False)

    return parser


def parse(cb: Cubase) -> Exception | NoneType:
    """
    Handles any actions specified by CLI flags.
    """
    parser = __create_parser(cb)
    args = parser.parse_args()
    # print(args)

    target_cubase_version = ""
    if args.cubase_version is not None:
        target_cubase_version = args.cubase_version
        target_cubase_app = cb.get_by_version(int(target_cubase_version))
        # print(target_cubase_app)
        if cb.is_open(target_cubase_app.version):
            print(f"Cubase {target_cubase_version} is open!")
            print("Please close it before altering preferences.")
        # print(f"Specified Cubase version: {target_cubase_version}")
    else:
        target_cubase_version = cb.latest.version
        # print(f"Specified Cubase version: {target_cubase_version}")

    if args.list_cubase_versions:
        cb.list_cubase_versions()

    # TODO:
    # if args.list_cubase_preferences:
