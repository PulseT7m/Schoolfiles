class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def addChild(self,data,node=None):
        if node is None:
            node = self.root
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.addChild(data.node.left)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.addChild(data, node.right)
    def printInorder(self,root):
        if root:
            root.printInorder(root.left)
            print(root.data, end=" ")
            root.printInorder(root.right)
    def printPreorder(self,root):
        if root:
            print(root.data, end=" ")
            root.printPreorder(root.left)
            root.printPreorder(root.right)
    def printPostorder(self,root):
        if root:
            root.printPostorder(root.left)
            root.printPostorder(root.right)
            print(root.data, end=" ")
    def printLevelOrder(self,root):
        h = root.height(root)
        for i in range(1, h+1):
            root.printCurrentLevel(root, i)
            print()
    def printCurrentLevel(self,root, level):
        if root is None:
            return
        if level == 1:
            print(root.data,end=" ")
        elif level > 1:
            root.printCurrentLevel(root.left, level-1)
            root.printCurrentLevel(root.right, level-1)
    def height(self,root):
        if root is None:
            return 0
        else:
            lheight = root.height(root.left)
            rheight = root.height(root.right)
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1

node1 = Node(50)
node2 = Node(20)
node3 = Node(45)
node4 = Node(11)
node5 = Node(15)
node6 = Node(30)
node7 = Node(78)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

node1.printInorder(node1)
print()
node1.printPreorder(node1)
print()
node1.printPostorder(node1)
print()
node1.printLevelOrder(node1)
