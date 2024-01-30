class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

def printInorder(root):
    if root:
        #First recur on left child
        printInorder(root.left)
        #Then print the data of node
        print(root.data, end=" ")
        #Now recur on right child
        printInorder(root.right)

def printPreorder(root):
    if root:
        #Then print the data of node
        print(root.data, end=" ")
        #First recur on left child
        printPreorder(root.left)
        #Now recur on right child
        printPreorder(root.right)
        
def printPostorder(root):
    if root:
        #First recur on left child
        printPostorder(root.left)
        #Now recur on right child
        printPostorder(root.right)
        #Then print the data of node
        print(root.data, end=" ")
#
#
#
#
#
#
#
#
#
#
#
# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
        print()

# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data,end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
        #print(end="|")

# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

# Driver code
if __name__ == "__main__":
    print("Inorder traversal of binary tree is")
    printInorder(node1)
    print()
    print("Preorder traversal of binary tree is")
    printPreorder(node1)
    print()
    print("Postorder traversal of binary tree is")
    printPostorder(node1)
    print()
    print("Level order traversal of binary tree is")
    printLevelOrder(node1)
    
