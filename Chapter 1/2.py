def rev(s):
	word = list(s)
	l = len(word)
	for i in xrange(l/2):
		word[i], word[l-1-i] = word[l-1-i], word[i]
	return "".join(word)

#run time: O(n)
print "Test cases: abcdefg, 123456789, 1234, 0, ''"
print rev("abcdefg")
print rev("123456789")
print rev("1234")
print rev("0")
print rev("")