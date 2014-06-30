class PE55:
	
	def getPalindrome(self, original,DEBUG=False ):
		
		theSum = original
		if DEBUG:
			print('original: ' + str(theSum))
		
		for i in range(50):
			orig = theSum
			reverse = str(theSum)[::-1]
			theSum = theSum + int(reverse)
			
			if DEBUG:
				print(orig)
				print(reverse)
				print(theSum)
				print
			
			if(str(theSum) == str(theSum)[::-1]):
				return theSum
			
		return -1

	def countLychrelNumbers(self,underThisValue):
	
		count = 0;
		for i in range(underThisValue+1):
			if -1 == self.getPalindrome(i):
				count += 1
		
		return count
