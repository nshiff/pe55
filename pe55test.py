import unittest
from pe55 import PE55

class PE55Test(unittest.TestCase):

	def testHappyCase(self):
		pe55 = PE55()
		assert 2 	== pe55.getPalindrome(1)
		assert 121	== pe55.getPalindrome(47)
		assert 7337	== pe55.getPalindrome(349)
		assert 0	== pe55.getPalindrome(0)
		
	def testSomeLychrelNumbers(self):
		generator = PE55()
		assert -1 == generator.getPalindrome(196)
		assert -1 == generator.getPalindrome(4994)
		
	def testFindLychrelNumbersUnderSomeNumber(self):
		finder = PE55()

		assert 0 == finder.countLychrelNumbers(1)
		assert 0 == finder.countLychrelNumbers(10)
		
		assert 0 == finder.countLychrelNumbers(195)
		assert 1 == finder.countLychrelNumbers(196)
		assert 1 == finder.countLychrelNumbers(197)
		
		assert 1 == finder.countLychrelNumbers(294)
		assert 2 == finder.countLychrelNumbers(295)
		assert 2 == finder.countLychrelNumbers(296)

	def testTheAnswer(self):
		finder = PE55()

		assert 249 == finder.countLychrelNumbers(10000)



if __name__ == "__main__":
	print("start")
	unittest.main()
