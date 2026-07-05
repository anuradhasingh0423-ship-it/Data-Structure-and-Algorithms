class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


node1 = Node(3)
node2 = Node(5)             
node3 = Node(7)
node4 = Node(9)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

print("\nTraversing the doubly linked list forward:")
currentNode = node1
while currentNode:
    print(currentNode.data, end="")
    currentNode = currentNode.next
print("null")

print("\nTraversing the doubly linked list backward:")
currentNode = node4
while currentNode:
    print(currentNode.data, end="")
    currentNode = currentNode.prev
print("null")    