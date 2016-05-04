#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def uniqueQ(word):
	s = sorted(word)
	for i in xrange(len(s)-1):
		if s[i] == s[i+1]:
			return False
	return True

#run time O(nlogn)
print "Some tests with no extra ds. Expected: False, True, True, False"
print uniqueQ('hello')
print uniqueQ("asdf")
print uniqueQ("12kf9e d")
print uniqueQ("   ")


def uniqueQWithHashBrowns(word):
	letters = dict()
	for c in word:
		if c in letters:
			return False
		else:
			letters[c] = "potato"
	return True

#run time O(n)
print "Some tests with hash table. Expected: False, True, True, False"
print uniqueQWithHashBrowns('hello')
print uniqueQWithHashBrowns("asdf")
print uniqueQWithHashBrowns("12kf9e d")
print uniqueQWithHashBrowns("   ")


def uniqueQWithSet(word):
	s = set(word)
	return len(s) == len(word)

#run time O(n)
print "Some tests with set. Expected: False, True, True, False"
print uniqueQWithSet('hello')
print uniqueQWithSet("asdf")
print uniqueQWithSet("12kf9e d")
print uniqueQWithSet("   ")


