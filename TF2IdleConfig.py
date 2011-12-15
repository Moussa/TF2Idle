# -*- coding: utf-8 -*-
config = {
	'SteamLocation': r'C:/Program Files (x86)/Steam', # Normal Steam installation location
	'SecondarySteamLocation': r'', # Secondary Steam location, if you're using a single Steam install for each account (some users face errors with this, hence using seperate installs per account)
	'SecondarySteamapps': r'', # Secondary Steamapps folder, seperate variable in case of a shared Steamapps folder.
	'SandboxieLocation': r'C:/Program Files/Sandboxie', # Sandboxie installation location
	'Steam API Key': r'', # Steam API key (If you wish to use the item logging function)
	'BackpackViewer': r'', # Backpack viewer site. Options = OPTF2, Steam, TF2B, TF2Items
	'IdleAccounts': [
		{'username': r'MyAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'MySandboxName',
		 'steaminstall': r'G:/Sandboxie/Steam/1',
		 'premium': False
		},
		{'username': r'MySecondAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'MySandboxName',
		 'steaminstall': r'G:/Sandboxie/Steam/2',
		 'premium': True
		},
		{'username': r'MyThirdAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'MySandboxName',
		 'premium': True
		}
	]
}