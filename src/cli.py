from __init__ import __app_name__, __version__
import argparse
# import configs

# stock_cubase_prefs = configs.get_stock_cubase_prefs()
# cubase_version_nums = configs.get_cubase_version_nums(stock_cubase_prefs)


parser = argparse.ArgumentParser(
    prog=__app_name__,
    description="Enables easy switching between multiple Cubase preferences folders.",
)

parser.add_argument(
    "-v", "--version", action="version", version=f"{__app_name__} v{__version__}"
)

parser.add_argument(
    "-V",
    "--cubase-version",
    action="store_const",
)

# subparsers = parser.add_subparsers()
# goodbye_parser = subparsers.add_parser('goodbye')
