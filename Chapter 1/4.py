def dictionagram(s1, s2):
	#first compare lengths to cover bases.
	if len(s1) != len(s2):
		# "Lengths are different. Cannot be anagrams."
		return False
	d = dict()
	#take all char of s1 and put it into a dictionary
	for c in s1:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	#take all char of s2 and subtract it out of the dictionary
	for c in s2:
		if c in d:
			d[c] -= 1
		else:
			# "character exists in s2 that is not in s1"
			return False
	#look at the diciontary to make sure everything is at 0
	for x in d:
		if d[x] != 0:
			# "s1 and s2 have different numbers of character %s" %x
			return False
	# "s1 and s2 are anagrams."
	return True


def testcases1():
	n = 0
	#empty strings
	if not dictionagram("",""):
		n += 1
		print "Failed empty strings"
	#single string + empty string
	if dictionagram("", "a"):
		n += 1
		print "Failed single string vs empty string"
	#are anagrams
	if not dictionagram("abc def", "f edcab"):
		n += 1
		print "Failed standard anagram test"
	#not anagrams but have all the same characters, just different #s of them
	if dictionagram("abcddab", "abccdab"):
		n += 1
		print "Failed nonagram, same char, different values"
	#not anagrams have different characters
	if dictionagram("abc ", "xyze"):
		n += 1
		print "Failed nonagram basic"
	#not anagrams s2 has a subset of s1 characters
	if dictionagram("abcdd ", "abcddd"):
		n += 1
		print "Failed nonagram, char(s2) \subset char (s1)"
	#not anagrams different lengths
	if dictionagram("abcd", "dcb"):
		n += 1
		print "Failed nonagram, len(s1) != len(s2)"
	#not anagrams s1 has a subset of s2 characters
	if dictionagram("abc eff", "f edcab"):
		n += 1
		print "Failed nonagram, char(s1) \subset char(s2)"
	if n > 0:
		print "Number of tests failed: %d" %n
		return Failed
	return "Passed"

print testcases1()




