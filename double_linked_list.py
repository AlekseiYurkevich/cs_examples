class Node:
    def __init__(self, value):

        self.value = value

        self.prev = None

        self.next = None


class DoublyLinkedList:
    def __init__(self):

        self.head = None

        self.tail = None

    # O(1) time | O(1) space

    def setHead(self, node):

        if self.head is None:

            self.head = node

            self.tail = node

            return

        self.insertBefore(self.head, node)

    # O(1) time | O(1) space

    def setTail(self, node):

        if self.tail is None:

            self.setHead(node)

            return

        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space

    def insertBefore(self, node, nodeToInsert):

        if nodeToInsert == self.head and nodeToInsert == self.tail:

            return

        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev

        nodeToInsert.next = node

        if node.prev is None:

            self.head = nodeToInsert

        else:

            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

    # O(1) time | O(1) space

    def insertAfter(self, node, nodeToInsert):

        if nodeToInsert == self.head and nodeToInsert == self.tail:

            return

        self.remove(nodeToInsert)

        nodeToInsert.prev = node

        nodeToInsert.next = node.next

        if node.next is None:

            self.tail = nodeToInsert

        else:

            node.next.prev = nodeToInsert

        node.next = nodeToInsert

