import cli
from cubase import Cubase


def main():
    cb = Cubase()
    cli.parse(cb)


if __name__ == "__main__":
    main()
