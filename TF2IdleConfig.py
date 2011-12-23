# -*- coding: utf-8 -*-
config = {
	'SteamLocation': r'C:/Program Files (x86)/Steam', # Normal Steam installation location
	'SecondarySteamapps': r'', # Secondary Steamapps folder that's shared between multiple instances of Steam, if you're using multiple instances. If not, set it to the steamapps folder of your secondary Steam installation.
	'SandboxieLocation': r'C:/Program Files/Sandboxie', # Sandboxie installation location
	'Steam API Key': r'', # Steam API key (If you wish to use the item logging function)
	'BackpackViewer': r'', # Backpack viewer site. Options = OPTF2, Steam, TF2B, TF2Items
	'IdleAccounts': [
		{'displayname': r'Account #1',
		'username': r'MyAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'MySandboxName', # Sandbox name in Sandboxie
		 'steaminstall': r'G:/Sandboxie/Steam/1', # Directory that contains Steam.exe
		 'group': [r'Premium']
		},
		{'username': r'MySecondAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'MySandboxName',
		 'steaminstall': r'G:/Sandboxie/Steam/2',
		 'group': [r'F2P',r'Premium'] # DEAR GOD HOW IS THIS POSSIBUL!
		},
		{'username': r'MyThirdAccount',
		 'password': r'MyPassword',
		 'steamID': r'MySteamID',
		 'sandboxname': r'MySandboxName',
		 'steaminstall': r'G:/Sandboxie/Steam/3'
		}
	]
}