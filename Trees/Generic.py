#program:       Generic
#purpose:       
#progamer:      Themadhood Pequot 1/30/2024

_FILE = "trees.Generic"
_VERSION = "0.0.1"

try:
    from . import Tree_Foundation
except:
    import Tree_Foundation

Error = Tree_Foundation.Error


"""
Generic trees are a collection of nodes where each node is a data
structure that consists of records and a list of references to its
children(duplicate references are not allowed). Unlike the linked
list, each node stores the address of multiple nodes.
"""

class Node(Tree_Foundation.Node):
    RemoveNode = None
    Traversal = None

    def __init__(self,**kwargs):
        Tree_Foundation.Node.__init__(self,**kwargs)


    def AddNode(self,name="",value=None,parent=""):
        if name == "":
            name = value
            
        if self.name == parent:
            if name in list(self._children):
                print(f"{name} alredy exists in {parent}'s Children")
            else:
                self._children.update({name:self._MakeNode(name,value)})
                
        children = list(self._children)
        for child in children:
            self._children[child].AddNode(name,value,parent)


    def _MakeNode(self,name="",value=None):
        if type(value) == Node:
            return value
        else:
            return Node(name=name,value=value,parent=self,root=self._root,
                        error=self._Error)


    def Search(self,value=None):
        st = Error.time.time()
        retar = []
        
        try:
            if self.name == value:
                retar.append(self)
                
            children = list(self._children)
            for child in children:
                lst = self._children[child].Search(value)
                while lst > []:
                    retar.append(lst.pop())
                    
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Node","Search",
                               f"Failed to Find: {value}",e],
                              "Functions")
        
        Error.Log(f"Search Runtime: {Error.LenTime(st)}","Log.txt")
        return retar






if __name__ == "__main__":
    root = Node(name="shame",value="shame")

    root.AddNode("conscience","conscience","shame")
    root.AddNode("selfdisgust","selfdisgust","shame")
    root.AddNode("embarrassment","embarrassment","shame")

    root.AddNode("selfconsciousness","selfconsciousness","embarrassment")
    root.AddNode("shamefacedness","shamefacedness","embarrassment")
    root.AddNode("chagrin","chagrin","embarrassment")
    root.AddNode("discomfiture","discomfiture","embarrassment")
    root.AddNode("abashment","abashment","embarrassment")
    root.AddNode("confusion","confusion","embarrassment")

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
















