def combine(l1,l2):
	if not type(l1) == list or not type(l2) == list:
		return([])
	for a in range(len(l2)):
		found = False
		for b in range(len(l1)):
			if type(l2[a]) == type(l1[b]) and l2[a] == l1[b]:
				found = True
				break
		if found == False:
			l1.append(l2[a])
	return(l1)
def align(li):
	if not type(li) == list or len(li) < 2:
		return([])
	olist = []
	for i in range(len(li)):
		if type(li[i]) == str:
			if not li[i] == "":
				olist.append(li[i])
		elif type(li[i]) == list:
			if not li[i] == []:
				olist.append(li[i])
		else:
			olist.append(li[i])
	return(olist)
def insert(li,val,pos):
	if not type(li) == list or not type(pos) == int or 0 > pos > len(li):
		return([])
	olist = []
	for l in range(len(li)):
		if l == pos:
			olist.append(val)
		olist.append(li[l])
	return(olist)
def split(li,pos):
	if not type(li) == list or not type(pos) == int:
		return([])
	newList = False
	olist1 = []
	olist2 = []
	for l in range(len(li)):
		if l == pos:
			newList = True
		if newList == False:
			olist1.append(li[l])
		else:
			olist2.append(li[l])
		return(olist1,olist2)
def removeDuplicates(li):
	return(combine([],li))
def snip(li,mul):
	if not type(li) == list or not (type(mul) == str or type(mul) == int):
		return([])
	for l in range(len(li)):
		if type(mul) == int and l == mul:
			lines[l] == ""
			break
		elif lines[l] == mul:
			lines[l] == ""
			break
	return(align(lines))
