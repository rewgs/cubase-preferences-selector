from pathlib import Path, PurePath

from cubase import PreferencesManager


def main():
    # cli.parser.parse_args()

    # cubase = Cubase()
    # cubase_13 = cubase.get_by_version(13)
    # print(cubase_13)

    cb_prefs = PreferencesManager()
    cb_prefs.add_custom(name = "SNS Bear",
                        path = Path(PurePath.joinpath(Path.home(), "work", "sns", "development", "cubase-preferences")).resolve(strict=True),
                        description = "Bear McCreary's custom preferences. Widely used for most if not all of Sparks and Shadows."
                        )
    print(cb_prefs.custom_preferences)


if __name__ == "__main__":
    main()
