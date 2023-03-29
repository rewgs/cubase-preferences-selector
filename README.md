Allows a user to dynamically switch between different `~/Library/Preferences/Cubase {version}` folders.
Assumes that above location contains a *stock* Cubase config directory. If you would like to your 
current Cubase config, back it up somewhere, and then specify its name and path in `main.py`.

Then run `python {name}`, where `{name}` is equal to the name specified above.

Example: `python rewgs` to switch to my personal config; `python sns` to switch to the Sparks and Shadows config.

Currently Mac-only.
