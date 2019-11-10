from fuji.generalclass import checkToken
from fuji.settingsclass import get, set, unsetAll
def getPath(tkn):
	if checkToken(tkn,True) == False:
		return("")
	return("tfile-"+tkn+".txt")
def writeLines(tkn,lns):
	if checkToken(tkn,True) == False or not type(lns) == list or lns == []:
		return(False)
	try:
		f = open(getPath(tkn),"w")
	except:
		return(False)
	for l in range(len(lns)):
		if lns[l].endswith("\n") == False:
			lns[l] = lns[l] + "\n"
	f.writelines(lns)
	f.close()
	return(True)
def append(tkn,val):
	if checkToken(tkn) == False or not type(val) == str:
		return(False)
	if val.endswith("\n") == False:
		val = val + "\n"
	try:
		f = open(getPath(tkn),"a")
		f.write(val)
		f.close()
	except:
		return(False)
	return(True)
def readLines(tkn,pttrn=""):
	if checkToken(tkn) == False:
		return([])
	if not type(pttrn) == str:
		pttrn = ""
	try:
		f = open(getPath(tkn),"r")
		lines = f.readlines()
		f.close()
	except:
		return([])
	if not pttrn == "":
		olist = []
	for l in range(len(lines)):
		lines[l].replace("\n","")
		if not pttrn == "" and not lines[l].find(pttrn) < 0:
			olist.append(lines[l])
	return(lines)
