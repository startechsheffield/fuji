from fuji.generalclass import checkRoot, pythonVersion
from fuji.settingsclass import set
from os import mkdir, umask
from os.path import exists
from sys import exit, argv
if __name__ == "__main__":
	silent = False
	force = False
	reset = False
	def tPrint(txt):
		if silent == False:
			print(txt)
		return
	if len(argv) > 1:
		for a in range(len(argv)):
			if a > 0:
				argv[a] = argv[a].lower()
				if argv[a] == "--silent":
					silent = True
				elif argv[a] == "--force":
					force = True
				elif argv[a] == "--reset":
					
				elif argv[a] == "-sf" or argv[a] == "-fs":
					silent = True
					force = True
				else:
					argv[a] = argv[a].replace("-","")
					for c in range(len(argv[a]):
						if argv[a][c] == "s":
						       silent = True
						elif argv[a][c] == "f":
						       force = True
						elif argv[a][c] == "r":
							reset = True
						else:
							tPrint("Unknown option: "+argv[a])
							exit(1)
	tPrint("Performing first-time setup...")
	if pythonVersion() < "3":
		tPrint("ERR: Unsupported Python version")
		if force == False:
			exit(1)
		tPrint("  Continuing")
	if checkRoot() == False:
		tPrint("ERR: Permission denied")
		tPrint("This function requires root access")
		exit(1)
	paths = ["/usr/share/fuji","/usr/share/fuji/api"]
	umask(0)
	for p in range(len(paths)):
		tPrint("Creatng directory: "+paths[p])
		if exists(paths[p]) == False:
			mkdir(paths[p],mode=0o777)
			tPrint("  Done")
		else:
			tPrint("  Skipped")
	tPrint("Creating template: blacklist.txt")
	if exists("/usr/share/fuji/api/blacklist.txt") == False or reset == True:
		f = open("/usr/share/fuji/api/blacklist.txt","w")
		f.write("# This is the blacklist file for the fuji python module\n")
		f.write("# Layout: list the tokens one per line, no markup necasary.\n")
		f.close()
		tPrint("  Done")
	else:
		tPrint("  Skipped")
	tPrint("Creating template: log.txt")
	if exists("/usr/share/fuji/api/log.txt") == False or reset == True:
		f = open("/usr/share/fuji/api/log.txt","w")
		f.write("# This is the logfile for fuji python module\n")
		f.write("# LAYOUT: token: DATE @ TIME: Message.\n")
		f.close()
		tPrint("  Done")
	else:
		tPrint("  Skipped")
	tPrint("Process complete")
	exit(0)
