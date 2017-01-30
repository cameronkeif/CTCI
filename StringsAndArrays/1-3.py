# Determine if one string is a permutation of the other
# Time complexity: O(N)
# Space complexity: O(N)

# General Algorithm:
# Iterate over both of the strings, create a hash table which maps each character to its count (one hash table for each string)
# Iterate over one string, compare the character counts. If a key is missing or the counts are not equal, return False
# Return True at the end, because after the loop we know the counts are the same which by definition means its a permutation

def isPermutation(s1, s2):
	if len(s1) != len(s2):
		return False

	chars1 = buildCharacterMap(s1)
	chars2 = buildCharacterMap(s2)

	for char in chars1:
		if char not in chars2 or chars1[char] != chars2[char]: # MISTAKE - forgot the first part which threw a KeyError
			return False
	
	return True

def buildCharacterMap(s):
	chars = {}

	for char in s:
		if char in chars:
			chars[char] += 1
		else:
			chars[char] = 1
	
	return chars

print isPermutation('abc','bac')
print isPermutation('abbc','baac')
print isPermutation('abc','ba')
print isPermutation('cam is cool','mac is looc')
print isPermutation('','')
print isPermutation('cam','tgh')

# Remember, if you're unsure whether a hash table will have a key, you need to test to see if it's in there.