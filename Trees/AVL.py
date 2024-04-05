#program:       AVL
#purpose:       
#progamer:      Themadhood Pequot 1/30/2024

_FILE = "Trees.AVL"
_VERSION = "0.0.1"

try:
    from . import Binary
except:
    import Binary

Error = Binary.Error
st = Error.time.time()
Error.LenTime(st)
Error.Log(f"","Log.txt")

"""
AVL tree is a self-balancing Binary Search Tree (BST) where the difference
between heights of left and right subtrees for any node cannot be more than
one.
"""

class Node(Binary.Node):
    def __init__(self,**kwargs):
        Binary.Node.__init__(self,**kwargs)

    def _Balenced(self):
        Lhight = Rhight = 0
        
        if self._children["Left"] != None:
            Lhight = self._children["Left"].GetHight()
            
        if self._children["Right"] != None:
            Rhight = self._children["Right"].GetHight()

        return Lhight - Rhight

    def Balence(self):
        for child in self._children:
            if self._children[child] != None:
                self._children[child].Balence()

        balence = self._Balenced()
        if balence > 1:
            self._RotateRight()
            self.Balence()
            return True
        elif balence < -1:
            self._RotateLeft()
            self.Balence()
            return True
        return False
    
    def _RotateRight(self):
        #     A              A
        #   /   \          /   \
        #  B     G        B     C
        # / \   /        / \   / \
        #D   E C        D   E F   G
        #     / \                /
        #    F   H              H
        
    #parent Chang
        #set left cilds parent to selfs parent
        self._children["Left"]._CangeParent(self._parent)
        #change parent child to left child
        self._parent._CangeChild(self,self._children["Left"])
        #set self parent to left child
        self._parent = self._children["Left"]
    #child chang
        #C.R = G
        newchild = self._children["Left"]._ChangeRightChild(self)
        #G.L = H
        self._children["Left"] = newchild
        
    
    def _RotateLeft(self):
        #     A              A
        #   /   \          /   \
        #  B     F        B     C
        # / \     \      / \   / \
        #D   E     C    D   E F   G
        #         / \          \
        #        H   G          H
        
    #parent Chang
        #set right cilds parent to selfs parent
        self._children["Right"]._CangeParent(self._parent)
        #change parent child to right child
        self._parent._CangeChild(self,self._children["Right"])
        #set self parent to right child
        self._parent = self._children["Right"]
    #child chang
        #C.L = F
        newchild = self._children["Right"]._ChangeLeftChild(self)
        #F.R = H
        self._children["Right"] = newchild

    def _CangeParent(self,parent):
        self._parent = parent
        
    def _CangeChild(self,child,new):
        if self._children["Left"] is child:
            self._children["Left"] = new
            
        elif self._children["Right"] is child:
            self._children["Right"] = new

    def _ChangeRightChild(self,new):
        oldChild = self._children["Right"]
        self._children["Right"] = new
        return oldChild

    def _ChangeLeftChild(self,new):
        oldChild = self._children["Left"]
        self._children["Left"] = new
        return oldChild


##############################################################################
################################## Root ######################################
##############################################################################

class Root:
    def __init__(self,**kwargs):
        self._root = Node(parent=self,**kwargs)
    def Balence(self):
        if self._root.Balence():
            self.Balence()
    def GetHight(self):
        self._root.GetHight()
    def GetSize(self):
        self._root.GetSize()
    def _CangeChild(self,child,new):
        self._root = new
    

try:
    pass

except Exception as e:
    if self._Error:
        raise
    Error.UploadError([_FILE,_VERSION,"class","def",
                                f"mesage",e],"Functions")




if __name__ == "__main__":
    class _node(Node):
        def __init__(self,**kwargs):
            Node.__init__(self,**kwargs)

        def AddNode(self,value):
            if self._children[list(self._children)[0]] != None:
                self._children[list(self._children)[0]].AddNode(value)
            else:
                node = _node(value=value,parent=self,error=self._Error)
                self._children[list(self._children)[0]] = node

        """def Print(self,lvl=0):
            s = self._TreeStrPrefix(lvl)

            if self._value != None:
                print(f"{s}{self._value}")
            else:
                print("root", list(self._children)[0])

            files = list(self._children)
            for file in files:
                if self._children[file] != None:
                    self._children[file].Print(lvl+1)"""

    class _root(Root):
        def __init__(self,**kwargs):
            Root.__init__(self,**kwargs)
            self._root = _node(parent=self,value=9,**kwargs)
        def AddNode(self,value):
            self._root.AddNode(value)
        def Print(self):
            self._root.Print()

    root = _root(error=True)
    
    for i in range(0,5):
        root.AddNode(i)

    root.Print()
    root.Balence()
    print()
    root.Print()

    print()
    print("Vars(root)")
    print("Defs(root)")

    def Vars(p):
        print()
        vardct = vars(p)
        varlst = list(vardct)
        for v in varlst:
            print(f"{v}: {vardct[v]}")

    def Defs(p):
        print()
        lst = dir(p)
        for d in lst:
            print(d)



# R             R           R          R            R
#  \             \           \          \            \
#   0             0           0          3            3
#    \             \           \        / \          / \
#     1             1           3      0   4        1   4
#      \             \         / \      \          / \
#       2             3       1   4      1        0   2
#        \           / \       \          \
#         3         2   4       2          2
#          \
#           4












