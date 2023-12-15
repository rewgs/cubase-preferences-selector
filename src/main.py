import cli, configs


def main():
    cli.parser.parse_args()
    configs.get_stock_config()



if __name__ == "__main__":
    main()
