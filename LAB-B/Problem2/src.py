from random import randint

def commonMembers_h(a, b, acc):
	"""
		Description
			Helper recursive function to find common members between to lists.
			Base case:
				either a or b are empty, return the accumulated list
			Recursive case:
				compare a[0] and b[0], if they are
				-equal: add a[0] to acc and call recursively on the rest of both lists
				-different (a[0] < b[0]): call recursively on the rest of a and same b
				-different (a[0] > b[0]): call recursively on the rest of b and same a
		Input
			a,b sorted lists
			acc accumulated list, should be [] for external calls
		Output
			list of common members in a and b
	"""
	if not a or not b:
		return acc
	if a[0] == b[0]:
		idx = 0
		acc.append(a[0])
		while(len(a) > idx and a[idx] == b[0]):
			idx = idx + 1
		return commonMembers_h(a[idx:],b[1:],acc)
	elif a[0] < b[0]:
		return commonMembers_h(a[1:], b, acc)
	else:
		return commonMembers_h(a, b[1:], acc)
		
def commonMembers(a,b):
	"""
		Description
			Find common members, without repetition, among list a and list b
			We will sort both lists and call commonMembers_h
		Input
			a,b lists
		Output
			List of common members among a and b
	"""
	a.sort()
	b.sort()
	return commonMembers_h(a, b, [])
	
def commonMembersOneLiner(a,b):
	"""
		Description
			Find common members, among list a and list b, using a one liner
	"""
	return list(set(a).intersection(b))
	
def createLists(listA,listB,listCommon):
	"""
		Description
			Function to create two lists and the list of common members among them.
			This is to be used to test the commonMembers function.
			We will first add some numbers to the three lists (a,b,common) and then 
			different numbers to lists a and b. Finally, we will sort all the lists and
			remove repeated elements in the common list.
	"""
	for n in range(randint(5,10)):
		num = randint(0,10)
		listA.append(num)
		listB.append(num)
		listCommon.append(num)
	for n in range(randint(0,4)):
		num = randint(1,5)
		listA.append(num)
		num = randint(6,10)
		listB.append(num)
	listA.sort()
	listB.sort()
	listCommon = list(set(listCommon))
	listCommon.sort()
	return listA, listB, listCommon

