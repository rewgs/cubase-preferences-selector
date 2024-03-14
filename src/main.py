import cli
from cpm import Cubase


def main():
    cb = Cubase()
    print(cb.is_open(12))
    # cli.parse(cb)


if __name__ == "__main__":
    main()
