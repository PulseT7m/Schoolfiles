class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
depth=1
class BinaryTree():
    def __init__(self):
        self.root = None

    def add_root(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            raise Exception("Es gibt bereits einen Wurzel-Knoten.")
        
    def add_child(self, data, node=None): 
        if node is None:
            node = self.root
        if data < node.data: 
            if node.left is None: 
                node.left = TreeNode(data) 
            else:
                self.add_child(data, node.left) 
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.add_child(data, node.right)
                
    def in_order(self,node=None):
        if node is None:
            node=self.root
        if node.left:
            self.in_order(node.left)
        print(node.data)
        if node.right:
            self.in_order(node.right)
    def search(self,data,depth,node=None):
        if node is None:
            node = self.root
        print(node.data,end=",")
        if data==node.data:
            print()
            print(depth)
        else:
            depth+=1
            if data < node.data:
                print("left",end=",")
                self.search(data,depth,node.left)
            else:
                print("right",end=",")
                self.search(data,depth,node.right)
            
        


#Teste deine Methode mit dem folgendem Test-Case:

bst = BinaryTree()
bst.add_root(8)
bst.add_child(3)
bst.add_child(11)
bst.add_child(1)
bst.add_child(5)
bst.add_child(9)
bst.add_child(13)
bst.in_order()
bst.search(5,depth)
