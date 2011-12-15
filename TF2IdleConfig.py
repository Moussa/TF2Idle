# -*- coding: utf-8 -*-
config = {
	'SteamLocation': r'C:/Program Files (x86)/Steam', # Normal Steam installation location
	'SecondarySteamapps': r'', # Secondary Steamapps folder that's shared between multiple instances of Steam, if you're using multiple instances.  If not, set it to the steamapps folder of your secondary Steam installation.
	'SandboxieLocation': r'C:/Program Files/Sandboxie', # Sandboxie installation location
	'Steam API Key': r'', # Steam API key
	'BackpackViewer': r'', # Backpack viewer site (OPTF2, Steam, TF2B or TF2Items)
	'IdleAccounts': [
		{'username': r'MyAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'MySandboxName',
		 'steaminstall': r'', # Which steam install to use for this account.  If you're launching all accounts from a single Steam install, set this to the same value for all accounts.  E.g. C:\Program Files (x86)\SecondarySteam\
		 'premium': False # Whether this particular account owns a premium copy of TF2.  F2P = False, Premium = True.
		},
		{'username': r'MySecondAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'MySandboxName',
		 'steaminstall': r'', # Which steam install to use for this account.  If you're launching all accounts from a single Steam install, set this to the same value for all accounts.  E.g. C:\Program Files (x86)\SecondarySteam\
		 'premium': True # Whether this particular account owns a premium copy of TF2.  F2P = False, Premium = True.
		}
	]
}