class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

    #Traverse preorder
    def traversePreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traversePreOrder()#recursive
        if self.right:
            self.right.traversePreOrder()

    #Traverse inorder
    def tranverseInOrder(self):
        if self.left:
            self.left.tranverseInOrder()  # recursive
        print(self.data, end=' ')
        if self.right:
            self.right.tranverseInOrder()



    #Tranverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()  # recursive
        if self.right:
            self.right.traversePostOrder()
        print(self.data, end=' ')




if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)

    print("Pre order Traversal : ",end= " ")
    root.traversePreOrder()
    print("\nIn order Traversal : ", end=" ")
    root.tranverseInOrder()
    print("\nPostorder Traversal : ", end=" ")
    root.traversePostOrder()