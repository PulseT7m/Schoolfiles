class TNode:
    def __init__(self,data):
        self.data=data
        self.childs=[]
hans = TNode("Hans")
hans.child = [walter,brigitte]
print(hans.child,".",hans.data)
walter = TNode("Walter")
brigitte = TNode("Brigitte")