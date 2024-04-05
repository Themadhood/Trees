#program:       Tree_Foundation
#purpose:       
#progamer:      Madison Arndt 1/30/2024

_FILE = "Trees.Tree_Foundation"
_VERSION = "0.0.1"

from THEMADHOOD.Library import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

class Node:
    Search = None
    AddNode = None
    RemoveNode = None
    Traversal = None
    _printed=False
    
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
        children = list(self._children)
        for child in children:
            if self._children[child] != None:
                chHight = self._children[child].GetHight()
                if chHight > hight:
                    hight = chHight
                
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


    def Print(self,prefix="",end=False):
        if self._printed:
            if type(self._value) in [str,int]:
                print(f"{prefix}({self._value})")
            else:
                print(f"{prefix}({self.name})")
            return
        elif type(self._value) in [str,int]:
            print(f"{prefix}{self._value}")
        else:
            print(f"{prefix}{self.name}")

        self._printed = True

        #change Prefix
        if end and '└' in prefix:
            prefix = prefix.replace('└ ',"  ")
        elif '└' in prefix:
            prefix = prefix.replace('└ ',"│ ")
        elif end and '├' in prefix:
            prefix = prefix.replace('├ ',"  ")
        elif '├' in prefix:
            prefix = prefix.replace('├ ',"│ ")

        #check for children != none
        children = list(self._children)
        validChildren = []
        for child in children:
            if self._children[child] != None:
                validChildren.append(child)

        #call children to print
        for child in validChildren:
            if child == validChildren[-1]:
                self._children[child].Print(prefix + "└ ",True)
            else:
                self._children[child].Print(prefix + "├ ")

        if self.IsRoot():
            self._AfterPrint()

    def _AfterPrint(self):
        if self._printed:
            self._printed = False
            #check for children != none
            children = list(self._children)
            validChildren = []
            for child in children:
                if self._children[child] != None:
                    validChildren.append(child)

            #call children to print
            for child in validChildren:
                if child == validChildren[-1]:
                    self._children[child]._AfterPrint()
                else:
                    self._children[child]._AfterPrint()
                    
    
    def _TreeStrPrefix(self,lvl=0):
        s = ""
        '├ '
        try:
            i = 0
            while i < lvl:
                s += "│ "
                i+=1

            if lvl >= 1: 
                s = s.removesuffix("│ ")
                s += "└ "
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Node","_TreeStrPrefix",
                               f"failed to construct tree structur Prefix",e],
                              "Functions")

        return s




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
















