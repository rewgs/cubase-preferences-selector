Allows a user to dynamically switch between different Cubase configurations.

    ```
    -h, --help: Displays this menu.
    -v, --version: Show program's version number and exit

    -V, --cubase-version: Specify Cubase version for which to configs of.

    -l, --list-configs: Lists configs (shows * next to active). By default lists all.
        -c, --custom: Lists only custom configs.
        -s, --stock: Lists only stock configs.
    -a, --set-active-config: Specifies which config is active (requires path or name)
    -s, --save-config: Saves a new config to disk (requires path and name)
    -i, --import-config: Imports a new config from disk (requires path or name)
    -d, --delete-config: Delete a config (requires path or name)
    ```

# Intended usage
* Keep stock preferences intact -- do not change or edit them in any way.
* Custom preferences files should live in their own directory. The directory can be named anything, and they can either be complete or contain only a partial list of Cubase preferences files.
* Only a specific subset of files will be symlinked as needed. Files such as e.g. those having to do with plugins should not be touched.
* Configurations should be saved on a per-machine basis.
