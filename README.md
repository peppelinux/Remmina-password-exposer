Remmina password exposer
========================

Utility used to decrypt remmina password accounts

`remmina_password_exposer.py`

..runs the game :)

If you have .remmina folder backed up somewhere or another directory:

`REMMINA_FOLDER=~/.local/share/remmina/ ./remmina_password_exposer.py`

`REMMINA_FOLDER` is the `env` variable to define where is the the accounts files (ex: `group_rdp_windows_server.remmina`) and `remmina.pref` file.

If you have the `remmina.pref` in another directory, you can overwrite using `REMMINA_PREF`:

`REMMINA_PREF=~/.config/remmina/remmina.pref ./remmina_password_exposer.py`

Debug mode:

`DEBUG=1 ./remmina_password_exposer.py`