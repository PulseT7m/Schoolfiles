class Node():
    def __init__(self,data,nextNode=None):
        self.data=data
        self.nextNode=nextNode
class LinkedList():
    def __init__(self):
        self.head=None
    def insert_at_start(self,data):
        self.head=Node(data,self.head)
    def print_l1():
        current=self.head
        while current:
            print(current.data)
            current=current.nextNode
            
l1=LinkedList()
l1.insert_at_start("Eis")
l1.insert_at_start("Rum")
print(l1.head.data,end="-->")
print(l1.head.nextNode.data,end="-->")