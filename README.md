#Script
## Requirements
* [Python 2.7](http://www.python.org/getit/releases/2.7/) -- Install the 32 bit version (x86)

You will also need to install the following modules.

* [curses](http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses) -- Install the 32 bit version
* [modified tf2.py](http://dl.dropbox.com/u/105828/tf2.py) -- Modified version from the one available at https://github.com/swixel/tf2webappy

##Usage
Configure by editing `TF2IdleConfig.py`
Run from commandline

    python TF2Idle.py
    
#Idling

Quick tl;dr on how to idle.

## Requirements
* [Sandboxie](http://sandboxie.com)
* The ability to read

## Folder structure

You'll want a seperate Steam installation for each of your idle accounts (they'll share a single steamapps folder, so don't worry about disk space), you can do it with a single secondary Steam install - however some users may face errors doing this.  Never use your main Steam install, else you risk corrupting your game files.

* Create a folder
* Copy Steam.exe into that folder and run it so all the necessary files for Steam are downloaded
* Copy paste the hell out of that folder, and rename accordingly so you have a seperate Steam install for each idle account.
* Create a steamapps folder somewhere (Do not use your main Steam installation's steamapps folder).
* Open cmd.exe as an administrator, and for each idle account enter (using my directories as an example): `mklink /d "G:/Sandboxie/Steam/1/Steamapps" "G:/Sandboxie/Steam/Steamapps"` where the first parameter is the idle account's Steam install, followed by `/Steamapps`, and the second parameter is your secondary steamapps folder (Again, not your main Steam installations steamapps).

You should now have a folder structure similar to:

```
G:\Sandboxie\Steam:
    1
        ...
        Steamapps
        ...
    2
        ...
        Steamapps
        ...
    3
        ...
        Steamapps
        ...
    Steamapps
```

## Sandboxie

If you don't own the payed version of Sandboxie, then obtain it - otherwise you'll only be able to idle 1 account at a time.

Create a sandbox for each of your folders, with whatever name you want to give them - I name mine the same as my folder names (so just 1,2,3...).

You'll want to set the settings as follows:

* `Restrictions` -> `Drop Rights` -> Untick `Drop rights from Administrators and Power Users groups`
* `Resource Access` -> `File Access` -> `Full Access` -> Add your idle accounts Steam folder, and your steamapps folder.
  * e.g. `G:\Sandboxie\Steam\1`
  * `G:\Sandboxie\Steam\Steamapps`

## Configure the script

Open up `TF2IdleConfig.py` and start editing...  It's pretty simple, and there are example values for most things... but here's an example configuration with everything filled in, in case you stoopid :3:

```python
# -*- coding: utf-8 -*-
config = {
    'SteamLocation': r'C:/Program Files (x86)/Steam', # Normal Steam installation location
	'SecondarySteamapps': r'G:/Sandboxie/Steam/Steamapps', # Secondary Steamapps folder that's shared between multiple instances of Steam, if you're using multiple instances. If not, set it to the steamapps folder of your secondary Steam installation.
	'SandboxieLocation': r'C:/Program Files/Sandboxie', # Sandboxie installation location
	'Steam API Key': r'abc123', # Steam API key (If you wish to use the item logging function)
	'BackpackViewer': r'OPTF2', # Backpack viewer site. Options = OPTF2, Steam, TF2B, TF2Items
	'IdleAccounts': [
		{'username': r'MyAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'1', # Sandbox name in Sandboxie
		 'steaminstall': r'G:/Sandboxie/Steam/1' # Directory that contains Steam.exe
		},
		{'username': r'MySecondAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'2',
		 'steaminstall': r'G:/Sandboxie/Steam/2',
		 'f2p': True
		},
		{'username': r'MyThirdAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'3',
		 'steaminstall': r'G:/Sandboxie/Steam/3'
		}
	]
}
```

## First launch / what to do after every TF2 update

* Run TF2Idle.py
* Select option 8 to copy the TF2 GCFs from your main Steamapps folder, to your secondary Steamapps folder
* Select option 9 and then option 'a' to delete any contents in each sandbox, this prevents errors.
* Select option 3, and load up **one** of your idle accounts. This is to make sure the backup GCFs are completely up-to-date.
* Close the sandboxed TF2 and Steam (else you'll get errors when launching the other idle accounts).
* And then do whatever you like.