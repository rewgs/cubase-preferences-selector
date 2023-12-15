from __init__ import __app_name__, __version__
import argparse

parser = argparse.ArgumentParser(
                    prog=__app_name__
)
parser.add_argument("--version", action="version", version=f"{__app_name__} v{__version__}")
# subparsers = parser.add_subparsers()

# hello_parser = subparsers.add_parser('hello')
# goodbye_parser = subparsers.add_parser('goodbye')
