""" Problem 2-1: Remove duplicates from a linked list. Follow up: how would you do it without a temp buffer?"""

from node import *

def removeDuplicates(head):
	"""Solution with a temp buffer. 
	Time complexity: O(N)  - Linear progression through the list in iteration 1, linear progression through the list in iteration 2 = O(2N) = O(N)
	Space complexity: O(N) - the dictionary is the only data structure and it grows linearly = O(N)
	"""
	duplicates = dict()

	node = head

	# Find duplicates and put them in the dictionary
	while node:
		if node.data in duplicates:
			duplicates[node.data] += 1
		else:
			duplicates[node.data] = 1
		
		node = node.next

	# Reset for second iteration
	node = head

	# Remove duplicates
	while node:
		if duplicates[node.data] > 1:
			if node == head:
				head = head.next # Get a new head
			elif node.next:
				node.next = node.next.next
			duplicates[node.data] -= 1
		
		node = node.next

	return head

# Test case: No duplicates
print "No Duplicates"
print "______________________"
head = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)

head.next = n1
n1.next = n2
n2.next = n3

print head

print "-- After removing duplicates --"

head = removeDuplicates(head)
print head

# Test case: Duplicates at end
print "\nDuplicates at end"
print "______________________"
head = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(3)

head.next = n1
n1.next = n2
n2.next = n3

print head

print "-- After removing duplicates --"

head = removeDuplicates(head)
print head

# Test case: Duplicates in middle
print "\nDuplicates in middle"
print "______________________"
head = Node(1)
n1 = Node(2)
n2 = Node(2)
n3 = Node(3)

head.next = n1
n1.next = n2
n2.next = n3

print head

print "-- After removing duplicates --"

head = removeDuplicates(head)
print head

# Test case: Duplicates at beginning
print "\nDuplicates at end"
print "______________________"
head = Node(1)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

head.next = n1
n1.next = n2
n2.next = n3

print head

print "-- After removing duplicates --"

head = removeDuplicates(head)
print head