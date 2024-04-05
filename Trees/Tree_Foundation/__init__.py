#program:       Tree_Foundation.__init__
#purpose:       
#progamer:      Themadhood Pequot 1/30/2024

_FILE = "Trees.Tree_Foundation.__init__"
_VERSION = "0.0.2"

try:
    from . import PrintDefs as _PrintDefs
except:
    import PrintDefs as _PrintDefs

Error = _PrintDefs.Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

class Node:
    #defs
    Search = None
    AddNode = None
    RemoveNode = None
    Traversal = None
    
    #vars
    _printed=False

    #Print Defs
    _TreeStrPrefix = _PrintDefs.TreeStrPrefix_
    _AfterPrint = _PrintDefs.AfterPrint_
    Print = _PrintDefs.Print
    
    def __init__(self,name="",value=None,parent=None,root=None,nodePath="",
                 error=False):
        self._Error = error 
        self.name = name
        self._value = value
        self._parent = parent
        self._root = root
        if self.name in ["ROOT","root","Root"] and self._root == None:
            self._root = self
        self._children = dict()
        self._NodePath = nodePath


    def GetRoot(self):
        if self._root != None:
            return self._root
        if self._parent != None:
            return self._parent.GetRoot()
        return self

    def IsRoot(self):
        if self._root == None:
            self._root = self.GetRoot()
        if self._root == self:
            return True
        return False

    def Hight(self):
        return self.GetHight()


    def GetHight(self):
        if self._printed:
            return 0
        self._printed = True
        
        hight = 0
        try:
            children = list(self._children)
            for child in children:
                if self._children[child] != None:
                    chHight = self._children[child].GetHight()
                    if chHight > hight:
                        hight = chHight
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Node","GetHight",
                               f"failed to get Hight",e],
                              "Functions")
                
        if self.IsRoot():
            self._AfterPrint()

        hight += 1  
        return hight

    def Size(self):
        return self.GetSize()

    def GetSize(self):
        if self._printed:
            return 0
        
        self._printed = True
        size = 1
        children = list(self._children)
        for child in children:
            if self._children[child] != None:
                size += self._children[child].GetSize()
                
        if self.IsRoot():
            self._AfterPrint()
            
        return size




if __name__ == "__main__":
    class _node(Node):
        def __init__(self,**kwargs):
            Node.__init__(self,**kwargs)

        def AddNode(self,value):
            if len(list(self._children)) > 0:
                self._children[list(self._children)[0]].AddNode(value)
            else:
                node = _node(value=value,error=self._Error)
                self._children.update({value:node})

    root = _node(error=True)
    print("tree Hight:",root.GetHight())
    
    for i in range(0,5):
        root.AddNode(i)

    print("tree Hight:",root.GetHight())
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
















