# Return True if s contains all unique characters, false otherwise
# O(N) time complexity
# O(N) space complexity
def isUnique(s):
	chars = {}
	for character in s:
		if character in chars:
			return False;
		chars[character] = 1
	return True

print isUnique("abc")
print isUnique("abbc")
print isUnique("abcc")
print isUnique("aabc")

# Return True if s contains all unique characters, false otherwise. No additional data structure is allowed. Assumes we are allowed to modify s
# O(NLOG(N)) Time Complexity
# O(1) space complexity 
def isUniqueNoDataStructure(s):
	s = sorted(s) # MISTAKE: I used s.sort(), but it's sorted(s) to sort the string
	for i in range(0, len(s) - 1):
		if s[i] == s[i + 1]:
			return False
	return True

print isUniqueNoDataStructure("abc")
print isUniqueNoDataStructure("abbc")
print isUniqueNoDataStructure("abcc")
print isUniqueNoDataStructure("aabc")