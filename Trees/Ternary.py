#program:       Ternary
#purpose:       
#progamer:      Themadhood Pequot 1/30/2024

_FILE = "Trees.Ternary"
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
A Ternary Tree is a tree data structure in which each node has at most three
child nodes, usually distinguished as “left”, “mid” and “right”.
"""

class Node(Tree_Foundation.Node):
    
    Search = None
    RemoveNode = None
    AddNode = None
    
    Traversal = None

    def __init__(self,**kwargs):
        Tree_Foundation.Node.__init__(self,**kwargs)
        self._children = {"Left":None,
                          "Middle":None,
                          "Right":None}

try:
    pass

except Exception as e:
    if self._Error:
        raise
    Error.UploadError([_FILE,_VERSION,"class","def",
                                f"mesage",e],"Functions")





if __name__ == "__main__":
    pass
















