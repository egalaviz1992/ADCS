def isMultiple_h(num, check, doPrint, oddEven):
	"""
		Description:
			Checks if num is multiple of check.
			The output depends on variables doPrint and oddEven.
			doPrint defines whether the output will be printed or if a boolean
			test is being issued
			oddEven defines whether we're doing an odd/even check or if we're
			doing a -divides evenly- check
		Input
			num(number) number to evaluate
			check(number) number to divide by
			doPrint(boolean) print result?
			oddEven(boolean) oddEven test?
		Output
			True/False if !doPrint
			relationship among numbers if doPrint
	"""
	if (num % check == 0):
		if doPrint == True:
			if oddEven == True:
				if num % 4 == 0:
					return 'divisible by 4';
				else:
					return 'even'
			else:
				return 'divides evenly'
		else:
			return True
	else:
		if doPrint == True:
			if oddEven == True:
				return 'odd'
			else:
				return 'does not divide evenly'
		else:
			return False
		
def isMultiple(num, check):
	"""
		Description:
			Checks if num is multiple of check
		Input
			num(number) number to evaluate
			check(number) number to divide by
		Output
			divides evenly/does not divide evenly
	"""
	return isMultiple_h(num, check, True, False)

def isOddOrEven(num):
	"""
		Description:
			Checks if num is odd, even, or divisible by 4 (implicitly even)
		Input
			num(number) number to evaluate
		Output
			odd/even/divisible by 4
	"""
	return isMultiple_h(num, 2, True, True)
	
def isPrime(num):
	"""
		Description:
			Checks is num is a prime number
		Input
			num(number) number to evaluate
		Output
			prime number/not a prime number
	"""
	for n in range(2, num):
		if isMultiple_h(num, n, False, False):
			return 'not a prime number'
			break
	else:
		return 'prime number'