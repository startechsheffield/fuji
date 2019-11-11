from datetime import datetime
from os import geteuid
from sys import version
def getVersion():
	return("1.0.0")
def getDate(fmt="uk"):
	now = datetime.now()
	if not type(fmt) == str:
		fmt="uk"
	if fmt.lower() == "uk":
		return(now.strftime("%d/%m/%Y"))
	elif fmt.lower() == "us":
		return(now.strftime("%Y/%m/%d"))
	else:
		return(now.strftime(fmt))
def getTime(fmt="%H:%M:%S"):
	now = datetime.now()
	if not type(fmt) == str:
		fmt="%H:%M:%S"
	return(now.strftime(fmt))
def getDateTime(fmt="uk",jnr="@"):
	now = datetime.now()
	if not type(fmt) == str:
		fmt="uk"
	if not type(jnr) == str:
		jnr="@"
	if fmt.lower() == "uk":
		return(now.strftime("%d/%m/%Y "+jnr+" %H:%M:%S"))
	elif fmt.lower() == "us":
		return(now.strftime("%Y/%m/%d "+jnr+" %H:%M:%S"))
	else:
		return(now.strftime(fmt))
def checkToken(tkn,ibl=False):
	if not type(ibl) == bool:
		ibl = False
	if type(tkn) == str and 3 < len(tkn) < 17:
		badChar = False
		exceptions = "1234567890-_."
		for c in range(len(tkn)):
			if tkn[c].isalpha() == False and exceptions.find(tkn[c]) < 0:
				badChar = True
				break
		if badChar == True:
			return(False)
		if ibl == True:
			return(True)
		try:
			f = open("/usr/share/stech/api/blacklist.txt","r")
			lines = f.readlines()
			f.close()
		except:
			lines = []
		if lines == []:
			return(True)
		found = False
		for l in range(len(lines)):
			if lines[l] == tkn+"\n":
				found = True
				break
		return(not found)
	return(False)
def checkRoot():
	return(geteuid() == 0)
def pythonVersion():
	v = version.split(" ")[0].split(".")
	return(v[0]+"."+v[1])
