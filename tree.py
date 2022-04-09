class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data != None:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            if data == self.data:
                print("Duplicate data")
        else:
            self.data = data

def test_insert():
    tree = Node(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(0)
    assert tree.right.data == 2
    assert tree.right.right.data == 3
    assert tree.left.data == 0

def main():
    test_insert()

if __name__ == '__main__':
    main()