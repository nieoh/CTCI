#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

def uniqueQ(word):
	s = sorted(word)
	for i in xrange(len(s)-1):
		if s[i] == s[i+1]:
			return False
	return True

print "Some tests. Expected: False, True, True, False"
print uniqueQ('hello')
print uniqueQ("asdf")
print uniqueQ("12kf9e d")
print uniqueQ("   ")

