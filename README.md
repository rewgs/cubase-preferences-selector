Allows a user to dynamically switch between different `~/Library/Preferences/Cubase {version}` folders.
Assumes that above location contains a *stock* Cubase config directory. If you would like to your 
current Cubase config, back it up somewhere, and then specify its user name and path in `main.py`.

Then run `python main.py {user}`, where `{user}` is equal to the user name specified above.

Example: `python main.py rewgs` to switch to my personal config; `python main.py sns` to switch to the Sparks and Shadows config.

Currently Mac-only.

# TO FIX

- Key commands aren't switching properly. Selecting the rewgs config and then the associated key commands does not load them -- instead key commands remain custom. Might be an issue with the key commands file itself, though? 
    - Updates: 
        - The AR.xml key commands file definitely isn't formatted correctly...that may have something to do with it.
        - Definitely something wrong with that file ^. The sns key commands load correctly. That's great, it's not a bug with the code, the file is just fucked. I guess that's one reason to keep this all in a git repo...
