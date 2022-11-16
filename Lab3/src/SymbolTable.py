class SymbolTable:
    def __init__(self):
        self.size = 0
        self.capacity = 200
        self.lls = [None] * self.capacity

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.lls[index]

        if node is None:
            self.lls[index] = Node(key, value)
            return index

        # if collision:
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)
        return index

    def find(self, key):
        index = self.hash(key)
        node = self.lls[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.lls[index]
        prev = None

        if node.key == key:
            self.lls[index] = None
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next

            return result

    def hash(self, key):
        return hash(key) % self.capacity

    def has(self, value):
        for ll in self.lls:
            node = ll
            while node and node.value != value:
                node = node.next
            if node and node.value == value:
                return node.key
        return None


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
