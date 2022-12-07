class Node:
    def __init__(self, data, parent):
        self._data = data
        self._parent = parent
        self._left = None
        self._right = None

    def getData(self):
        return self._data
    
    def getleft(self):
        return self._left

    def getright(self):
        return self._right
    
    def getparent(self):
        return self._parent

    def isRoot(self):
        return self._parent is None

    def isExternal(self):
        return self._left is None and self._right is None

    def insert(self, data):
        if data < self._data:
            if self._left is None:
                self._left = Node(data, self)
            else:
                self._left.insert(data)
        elif data > self._data:
            if self._right is None:
                self._right = Node(data, self)
            else:
                self._right.insert(data)
        else:
            return False
        return True

class BinaryTree:
    def __init__(self):
        self.root = Node(0,None)
        self._size = 0

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0
    
    def nodes(self):
        self.preOrder(self.root)
    
    def add(self, data):
        if self.root._right is None and data%2 == 0:
            self.root._right = Node(data,self.root)
        elif self.root._left is None and data %2 != 0:
            self.root._left = Node(data,self.root)
        else:
            if data%2 != 0:
                self.root._left.insert(data)
            else:
                self.root._right.insert(data)
    
    #preOrder traversal
    def preOrder(self, node):
        if node is not None:
            print(node.getData(), end = ' ')
            self.preOrder(node.getleft())
            self.preOrder(node.getright())

#Test Case
if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    binaryT.nodes()