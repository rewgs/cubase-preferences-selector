# TODO: 
# - This is still deleting user files!!
# - Looks like Generic Remotes end up in the prefs folder too once imported...will need to account for those as well 
#   maybe link to them in cubase-preferences/Generic Remotes folder (for sns)...will that work? Also, note that 
#   Generic Remote #1 is always called Generic Remote.xml.


import os
import sys
# import shutil
from pathlib import Path
from pathlib import PurePath

import cli
import configs


def main():

    stock_cofig = configs.get_stock_config()
    print(stock_cofig)


if __name__ == "__main__":
    main()
