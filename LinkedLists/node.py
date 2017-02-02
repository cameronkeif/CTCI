class Node:
	data = 0
	next = None
	
	def __init__(self, data):
		self.data = data

	def __str__(self):
		returnString = ""
		node = self
		while node:
			if node.next:
				returnString += str(node.data) + " -> "
			else:
				returnString += str(node.data)

			node = node.next
		return returnString