import shutil, os, subprocess, time, datetime, webbrowser, sys
import curses, tf2
from TF2IdleConfig import config

backpackViewerDict = {'optf2': 'http://optf2.com/tf2/user/%(ID)s',
					  'steam': 'http://steamcommunity.com/id/%(ID)s/inventory',
					  'tf2b': 'http://tf2b.com/?id=%(ID)s',
					  'tf2items': 'http://www.tf2items.com/id/%(ID)s'
					  }
					  
def copyfiles():
	gcfs = ['team fortress 2 content.gcf','team fortress 2 materials.gcf','team fortress 2 client content.gcf']
	print '\nPlease wait, copying GCFs over...'
	try:
		for file in gcfs:
			print '\nCopying ' + file + '...'
			shutil.copy(config['SteamLocation'] + os.sep + 'steamapps' + os.sep + file, config['SecondarySteamapps'])
		print '\nDone'
		print '\nDon\'t forget to run Steam unsandboxed to finish the update'
	except:
		print 'Error, something messed up while copying'

def getChoice(options=True):
	if options:
		print '\nPlease select an option:'
		print '\n[1] Start idling'
		print '\n[2] Start idling unsandboxed'
		print '\n[3] Start TF2(s) normally'
		print '\n[4] Start Steam(s) normally'
		print '\n[5] Log item drops'
		print '\n[6] View backpacks'
		print '\n[7] Update TF2 GCFs'
		print '\n[8] Delete sandbox contents\n'
		
	choice = str(raw_input(''))
	
	if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
		print 'That\'s not a valid choice, try again:\n'
		choice = getChoice(options=False)
	return choice
	
def getAccountGroups(accounts):
	groups = {}
	for account in accounts:
		if 'group' in account:
			for group in account['group']:
				group = group.lower()
				if group not in groups:
					groups[group] = [account]
				else:
					groups[group].append(account)
	return groups
	
def chooseAccountGroups(options=True):
	groups = getAccountGroups(config['IdleAccounts'])
	noOfGroups = len(groups)
	
	if noOfGroups == 0:
		print '\nYou have no groups set up. Please create some first.'
		return chooseAccounts(options=True) 
	
	if options:
		print '\nPlease select which group(s) in comma separated values (e.g. 1,2,3):\n'
		n = 0
		for group in groups:
			groupmembers = ''
			for user in groups[group]:
				groupmembers += (user['username'] if 'displayname' not in user else user['displayname']) + ', '
			groupmembers = groupmembers[:-2] # Get rid of trailing comma
			print '[%s] %s (%s)' % (str(n+1), group, groupmembers)
			n += 1
		print ''
	
	choices = str(raw_input('')).replace(' ','').split(',')
	
	accounts = []
	
	try:
		for choice in choices:
			if int(choice) > noOfGroups or int(choice) < 1:
				raise Exception
			else:
				accounts.extend(groups.items()[int(choice)-1][1])
	except:
		print 'Invalid input, try again:\n'
		accounts = chooseAccountGroups(options=False)
	
	return accounts
	
def chooseAccounts(options=True):
	noOfAccounts = len(config['IdleAccounts'])
	if options:
		print '\nPlease select which account(s) in comma separated values (e.g. 1,2,3):\n'
		n = 0
		
		print '[A] All accounts'
		print '[G] Group'
		print '' # A blank line between pre-set options and dynamic options
		
		for account in config['IdleAccounts']:
			print '[' + str(n+1) + ']', (account['username'] if 'displayname' not in account else account['displayname'])
			n += 1
		print ''
	
	choices = str(raw_input('')).replace(' ','').replace('.',',').split(',')
	
	accounts = []
	
	if len(choices) == 1 and choices[0].lower() == 'a':
		n = 0
		for account in config['IdleAccounts']:
			accounts.append(account)
			n += 1
	elif len(choices) == 1 and choices[0].lower() == 'g':
		accounts.extend(chooseAccountGroups())
	else:
		try:
			for choice in choices:
				if int(choice) > noOfAccounts or int(choice) < 1:
					raise Exception
				else:
					accounts.append(config['IdleAccounts'][int(choice)-1])
		except:
			print 'Invalid input, try again:\n'
			accounts = chooseAccounts(options=False)

	return accounts
	
def idleTF2(username, password, steamlocation, sandboxname=None):
	steamlaunchcommand = r'"%s/Steam.exe" -login %s %s -applaunch 440 +exec idle.cfg -textmode -nosound -low -novid -nopreload -nojoy -sw +sv_lan 1 -width 640 -height 480 +map itemtest' % (steamlocation, username, password)
	command = r'"%s/Start.exe" /box:%s %s' % (config['SandboxieLocation'], sandboxname, steamlaunchcommand)
	
	if sandboxname is not None:
		returnCode = subprocess.call(command)
	else:
		returnCode = subprocess.call(steamlaunchcommand)

def launchTF2(username, password, steamlocation, sandboxname):
	steamlaunchcommand = r'"%s/Steam.exe" -login %s %s -applaunch 440' % (steamlocation, username, password)
	command = r'"%s/Start.exe" /box:%s %s' % (config['SandboxieLocation'], sandboxname, steamlaunchcommand)

	returnCode = subprocess.call(command)

def launchSteam(username, password, steamlocation, sandboxname):
	steamlaunchcommand = r'"%s/Steam.exe" -login %s %s' % (steamlocation, username, password)
	command = r'"%s/Start.exe" /box:%s %s' % (config['SandboxieLocation'], sandboxname, steamlaunchcommand)

	returnCode = subprocess.call(command)
	
def deleteSandboxContents(sandboxname):
	command = r'"%s/Start.exe" /box:%s delete_sandbox' % (config['SandboxieLocation'], sandboxname)
	
	returnCode = subprocess.call(command)
	
def openBackpack(vanityID):
	address = backpackViewerDict[config['BackpackViewer'].lower()] % {'ID': vanityID}
	webbrowser.open(address)

def startLog(screen):
	def centreValue(width, text):
		return float(width - len(text))/2.0

	curses.init_pair(1, 10, curses.COLOR_BLACK) #GREEN
	curses.init_pair(2, 11, curses.COLOR_BLACK) #LIGHT BLUE
	curses.init_pair(3, 12, curses.COLOR_BLACK) #RED
	curses.init_pair(4, 14, curses.COLOR_BLACK) #YELLOW
	curses.init_pair(5, 13, curses.COLOR_BLACK) #PINK
	curses.init_pair(6, 9, curses.COLOR_BLACK) #BLUE
	curses.init_pair(7, 15, curses.COLOR_BLACK) #WHITE
	curses.init_pair(8, 8, curses.COLOR_BLACK) #GREY
	curses.init_pair(9, 2, curses.COLOR_BLACK) #FADED GREEN
	curses.init_pair(10, 3, curses.COLOR_BLACK) #FADED LIGHT BLUE
	curses.init_pair(11, 4, curses.COLOR_BLACK) #FADED RED
	curses.init_pair(12, 5, curses.COLOR_BLACK) #FADED PINK
	curses.init_pair(13, 6, curses.COLOR_BLACK) #FADED YELLOW
	curses.init_pair(14, 7, curses.COLOR_BLACK) #FADED WHITE

	accounts = eval(sys.argv[2:][0])
	API = tf2.API(key=config['Steam API Key'])

	lastIDlist = []
	accountcolours = []
	finds = ['','','','','','','','','','','','','','','','','','','','']
	findcount = 0
	cratefindcount = 0
	wy,wx=screen.getmaxyx() # 25, 80

	screen.clear()
	screen.border(0)
	screen.addstr(int(round(float(wy)/2.0)), int(round(centreValue(wx, 'Please wait, loading accounts...'))), 'Please wait, loading accounts...', curses.color_pair(7))
	screen.refresh()

	# Set up initial backpack inventory
	for account in accounts:
		if account['steamID'] != '':
			id = tf2._getSteamID64(account['steamID'])
		else:
			id = tf2._getSteamID64(account['username'])
		API.getProfile(id)
		API.getBackpack(id)
		backpack = API.users[id]['backpack']
		allbackpack = backpack.placed + backpack.unplaced
		templist = []
		for z in allbackpack:
			templist.append(z['id'])
		newestitem = allbackpack[templist.index(max(templist))]
		lastIDlist.append(newestitem['id'])

	while True:
		n = 0
		for account in accounts:
			try:
				if account['steamID'] != '':
					id = tf2._getSteamID64(account['steamID'])
				else:
					id = tf2._getSteamID64(account['username'])
				API.getProfile(id)
				API.getBackpack(id)
				backpack = API.users[id]['backpack']
				allbackpack = backpack.placed + backpack.unplaced
				templist = []
				for z in allbackpack:
					templist.append(z['id'])
				newestitem = allbackpack[templist.index(max(templist))]

				# Check to see if item with highest ID has changed
				if newestitem['id'] != lastIDlist[n]:
					lastIDlist[n] = newestitem['id']
					if newestitem['item_class'] != 'supply crate' and newestitem['item_name'] != 'Salvaged Mann Co. Supply Crate':
						currenttimestr = time.strftime('%H:%M', time.localtime(time.time()))
						output = {'item': newestitem['item_name'].encode('utf8'), 'item_slot': newestitem['item_slot'], 'account': account, 'time': currenttimestr}
						finds.pop(0)
						finds.append(output)
						findcount += 1
					else:
						cratefindcount += 1
			except:
				pass
			n += 1

		curses.cbreak()
		curses.noecho()
		screen.keypad(1)

		def printscreenline(wy, wx, item):
			if item == '':
				screen.addstr(wy, 0, '')
			else:
				if item['item_slot'] == u'head' or item['item_slot'] == u'misc': # Hatte Hatte Hatte
					textformatattribute = curses.color_pair(accounts.index(item['account'])+1) | curses.A_REVERSE
					screen.addstr(wy, 2, ' ' * (wx - 4), textformatattribute) # Paint entire line
				else:
					textformatattribute = curses.color_pair(accounts.index(item['account'])+1)
				screen.addstr(wy, int(round(centreValue(3.0/8.0 * float(wx), item['item']))), item['item'], textformatattribute)
				screen.addstr(wy, int(round(3.0/8.0 * float(wx) + centreValue(3.0/8.0 * float(wx), item['account']['username']))), item['account']['username'], textformatattribute)
				screen.addstr(wy, int(round(6.0/8.0 * float(wx) + centreValue(2.0/8.0 * float(wx), item['time']))), item['time'], textformatattribute)

		screen.clear()
		screen.border(0)

		screen.addstr(0, int(round(centreValue(3.0/8.0 * float(wx), 'Item'))), 'Item', curses.color_pair(7))
		screen.addstr(0, int(round(3.0/8.0 * float(wx) + centreValue(3.0/8.0 * float(wx), 'Account'))), 'Account', curses.color_pair(7))
		screen.addstr(0, int(round(6.0/8.0 * float(wx) + centreValue(2.0/8.0 * float(wx), 'Time'))), 'Time', curses.color_pair(7))

		# Print lines in drop log
		for n in range(1, 21):
			printscreenline(n, wx, finds[20-n])

		screen.addstr(22, 2, 'Accounts:', curses.color_pair(7))
		legendstringlength = len('Accounts:') + 3
		for account in accounts:
			displayName = account['username'] if 'displayname' not in account else account['displayname']
			screen.addstr(22, legendstringlength, displayName, curses.color_pair(accounts.index(account)+1))
			legendstringlength += len(displayName) + 1
		screen.addstr(23, 2, '# of items: %s (+ %s crates)' % (str(findcount), str(cratefindcount)), curses.color_pair(7))

		screen.refresh()

		time.sleep(60)

def main():
	while True:
		choice = getChoice()
		# Start idling these TF2 instances in sandboxes
		if choice == '1':
			accounts = chooseAccounts()
			for account in accounts:
				print '\nStarting idle session on %s...' % (account['username'] if 'displayname' not in account else account['displayname'])
				idleTF2(account['username'], account['password'], account['steaminstall'], account['sandboxname'])
				time.sleep(2)
		 # Start idling single TF2 instance unsandboxed
		if choice == '2':
			account = chooseAccounts()
			if len(account) > 1:
				print '\nInvalid choice, please choose a single account'
				continue
			print '\nStarting idle session on %s...' % account[0]['username']
			idleTF2(account[0]['username'], account[0]['password'], account[0]['steaminstall'])
		# Start up these TF2 instances normally in sandboxes
		if choice == '3':
			accounts = chooseAccounts()
			for account in accounts:
				print '\nStarting %s up...' % (account['username'] if 'displayname' not in account else account['displayname'])
				launchTF2(account['username'], account['password'], account['steaminstall'], account['sandboxname'])
				time.sleep(2)	
		# Start up these Steam instances normally in sandboxes
		if choice == '4':
			accounts = chooseAccounts()
			for account in accounts:
				print '\nStarting %s up...' % (account['username'] if 'displayname' not in account else account['displayname'])
				launchSteam(account['username'], account['password'], account['steaminstall'], account['sandboxname'])
				time.sleep(2)
				
		# Open new window to log item drops
		if choice == '5':
			if len(config['Steam API Key']) == 32:
				accounts = chooseAccounts()
				os.system(r'start python -i %s droplog "%s"' % (sys.argv[0], str(accounts)))
			else:
				print '\nError: Please check your Steam API key is present and valid.'
		# Open up these accounts in a backpack viewer
		if choice == '6':
			accounts = chooseAccounts()
			for account in accounts:
				if account['steamID'] != '':
					openBackpack(account['steamID'])
				else:
					openBackpack(account['username'])
		# Copy over upto date GCFs
		if choice == '7':
			copyfiles()
		# Delete sandbox contents
		elif choice == '8':
			accounts = chooseAccounts()
			for account in accounts:
				try:
					print '\nDeleting sandbox %s...' % account['sandboxname']
					deleteSandboxContents(account['sandboxname'])
					time.sleep(3)
				except KeyError:
					print '\n%s has no associated sandbox' % (account['username'] if 'displayname' not in account else account['displayname'])

if len(sys.argv) > 1:
	if sys.argv[1] == 'droplog':
		curses.wrapper(startLog)
else:
	main()