# from src import cli, __app_name__
from cb_prefs_select import cli, __app_name__


def main():
    cli.app(prog_name=__app_name__)
    # stock_cofig = configs.get_stock_config()
    # print(stock_cofig)


if __name__ == "__main__":
    main()
