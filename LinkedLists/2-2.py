""" Problem 2-2: Find kth to last element in a singly-linked list"""

from node import *

# I am operating under the assumption that k=0 should be the last member of the list (aka it's zero indexed essentially)
'''def findKthToLastElement(head, k):
	""" Iterative Solution 
		Time complexity: O(N)
		Space complexity: O(1) """

	leadNode = head
	trailNode = head

	for i in range(0,k):
		leadNode = leadNode.next
		if not leadNode:
			raise(IOError("List is too short"))

	while leadNode.next:
		leadNode = leadNode.next
		trailNode = trailNode.next
	
	return trailNode'''
class Counter:
	count = 0

	def __init__(self):
		self.count = 0

def findKthToLastElement(head, k, counter):
	""" Recursive Solution 
		Time complexity: O(N)
		Space complexity O(N) due to function call overhead """
	if not head:
		return
	node = findKthToLastElement(head.next, k, counter)
	counter.count += 1

	if (counter.count == k):
		return head

	return node

head = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)

head.next = n1
n1.next = n2
n2.next = n3
counter = Counter()

print findKthToLastElement(head, 0, counter).data # Should have value of 4 (the last member)
print findKthToLastElement(head, 3, counter).data # Should have value of 1 (the last member)

try:
	print findKthToLastElement(head, 4, counter).data # Should raise an exception due to being out of range
except:
	print "Error thrown"