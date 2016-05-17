#Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not. FOLLOW UP Write the test cases for this method.
def f(l):
	s = list(l)
	m = len(s)
	x = 0
	for i in xrange(m):
		for j in xrange(x):
			if s[i] == s[j]:
				break
		else:
			s[x] = s[i]
			x += 1
	return ''.join(s[:x])

print "expected: abcd. Actual:", f("abbcabad")

#This is O(n^2) since worst case you must compare each element to every other element. 

def testcases():
	n = 0
	#empty array
	if f("") != "":
		print "Failed empty array test"
		n += 1
	#array of one element
	if f("a") != "a":
		print "Failed one element array test"
		n += 1
	#constant array > 1
	if f("aaaaa") != "a":
		print "Failed constant array test"
		n += 1
	#completely unique array
	if f("abcdefg") != "abcdefg":
		print "Failed unique array test"
		n += 1
	#completely unique up to the last element
	if f("abcdefa") != "abcdef":
		print "Failed unique up to last element test"
		n += 1
	#order preservedness (not convinced this is needed...)
	if f("abcdcba") != "abcd":
		print "Failed order preservedness"
		n += 1
	if n > 0:
		return "Number of tests failed: %d" %n
	else:
		return "Passed all tests. Good job!"

print testcases()
				

