class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
depth=1
backtrackNumber=[]
backtrackDirection=[]
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
            backtrackDirection.append("root")
        backtrackNumber.append(node.data)
        if data==node.data:
            print()
            print(depth)
            print(backtrackNumber)
            print(backtrackDirection)
        elif data < node.data:
            depth+=1
            backtrackDirection.append("left")
            self.search(data,depth,node.left)
        elif data > node.data:
            depth+=1
            backtrackDirection.append("right")
            self.search(data,depth,node.right)
            
    def deleteNode(self, data, depth, node=None):
        if node is None:
            node = self.root
            backtrackDirection.append("root")
        backtrackNumber.append(node.data)
        if data < node.data:
            depth+=1
            backtrackDirection.append("left")
            self.search(data,depth,node.left)
        elif data > node.data:
            depth+=1
            backtrackDirection.append("right")
            self.search(data,depth,node.right)
        elif data==node.data:
            #print()
            #print(depth)
            #print(backtrackNumber)
            #print(backtrackDirection)
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self.min_node(node.right)
            node.data = temp.data
            node.right = self.delete(temp.data, depth, node.right)
            
            
    def min_node(self,node=None):
        if node is None:
            node = self.root
        min_node(node.left)
    def max_node(self,node=None):
        if node is None:
            node = self.root
        max_node(node.right)
            
        
        
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
#bst.deleteNode(5)
#bst.in_order()