Allows a user to dynamically switch between different `~/Library/Preferences/Cubase {version}` folders.
Assumes that above location contains a *stock* Cubase config directory. If you would like to your 
current Cubase config, back it up somewhere, and then specify its user name and path in `main.py`.

Then run `python main.py {user}`, where `{user}` is equal to the user name specified above.

Example: `python main.py rewgs` to switch to my personal config; `python main.py sns` to switch to the Sparks and Shadows config.

Currently Mac-only.
