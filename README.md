Allows a user to dynamically switch between different Cubase configurations.

    ```
    -h, --help: Displays this menu.
    -v, --version: Show program's version number and exit
    -V, --cubase-version: Specify current version of Cubase targetted by program
    ```

# Intended usage
* Keep stock preferences intact -- do not change or edit them in any way.
* Custom preferences files should live in their own directory. The directory can be named anything, and they can either be complete or contain only a partial list of Cubase preferences files.

# TODO
## MVP
- most recent version of Cubase only:
    - symlink files
        - CubasePreferences.add_custom()
    - refuse to do so if Cubase is open
