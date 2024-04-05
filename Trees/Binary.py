#program:       Binary
#purpose:       
#progamer:      Themadhood Pequot 1/30/2024

_FILE = "Trees.Binary"
_VERSION = "0.0.1"

try:
    from . import Tree_Foundation
except:
    import Tree_Foundation

Error = Tree_Foundation.Error
st = Error.time.time()
Error.LenTime(st)
Error.Log(f"","Log.txt")

"""
A binary Tree is defined as a Tree data structure with at most 2 children.
Since each element in a binary tree can have only 2 children, we typically
name them the left and right child.
"""

class Node(Tree_Foundation.Node):
    
    Search = None
    RemoveNode = None
    
    Traversal = None
    _Inorder = None #LSR
    _Preorder = None #SLR
    _Postorder = None #LRS

    
    def __init__(self,**kwargs):
        Tree_Foundation.Node.__init__(self,**kwargs)
        self._children = {"Left":None,
                          "Right":None}

    def _Inorder(self):
        """trverce left self right"""
        #left
        left = None
        if self._children["Left"] != None:
            left = self._children["Left"]._Inorder()
        #self
        value = self._value
        #right
        right = None
        if self._children["Right"] != None:
            right = self._children["Right"]._Inorder()

    def _AddNode(self,R=True,value=None):
        if R:
            if self._children["Right"] != None:
                self._children["Right"].AddNode(value)
            else:
                self._children["Right"] = _Node(value=value,parent=self,
                                                root=self._root,
                                                error=self._Error)
        else:
            if self._children["Left"] != None:
                self._children["Left"].AddNode(value)
            else:
                self._children["Left"] = _Node(value=value,parent=self,
                                               root=self._root,
                                               error=self._Error)
            


try:
    pass

except Exception as e:
    if self._Error:
        raise
    Error.UploadError([_FILE,_VERSION,"class","def",
                                f"mesage",e],"Functions")




if __name__ == "__main__":
    T = Node(error=True)
    print("Vars(T)")
    print("Defs(T)")

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
















