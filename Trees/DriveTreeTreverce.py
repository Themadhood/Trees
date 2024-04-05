#program:       DriveTreeTreverce
#purpose:       
#progamer:      Themadhood Pequot 1/30/2024

_FILE = "Trees.DriveTreeTreverce"
_VERSION = "0.0.1"

try:
    from . import Generic
except:
    import Generic
    
import sys
Error = Generic.Error
os = Error.os
io = Error.io

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

#get file path
if getattr(sys, 'frozen', False):
    _FP = os.path.dirname(sys.executable)
elif __file__:
    _FP = os.path.dirname(__file__)

    

##########################################################################
############################### Node #####################################
##########################################################################

class Node(Generic.Node):
    def __init__(self,path,**kwargs):
        Generic.Node.__init__(self,**kwargs)
        self.name = self._path = path

    def SearchNodePath(self):
        try:
            if os.path.isdir(self._GetPath()):
                files = os.listdir(self._GetPath())
                for file in files:
                    self._AddNode(file)
                    self._children[file].SearchNodePath()
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"_Node","SearchNodePath",
                               f"failed to search path",e],"Small Apps")

    def _GetPath(self):
        path = ""
        try:
            if self._path != None:
                path += self._path
                if self._value != None:
                    path += "/"
                
            if self._value != None:
                path += self._value
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"_Node","_GetPath",
                               f"failed to construct path",e],"Small Apps")

        return path

    def _AddNode(self,file):
        self._children.update({file:Node(path=self._GetPath(),
                                         value=file,parent=self,
                                         error=self._Error)})

    def WriteTxtStr(self,WriteFile,lvl=0):
        s = self._TreeStrPrefix(lvl)

        if self._value != None:
            self.WriteTxt(WriteFile,f"{s}{self._value}\n")
        else:
            self.WriteTxt(WriteFile,f"{self._path}\n")

        files = list(self._children)
        for file in files:
            self._children[file].WriteTxtStr(WriteFile,lvl+1)

    def WriteTxt(self,file,value):
        with io.open(file, "a", encoding='utf-8') as F:
            F.write(value)
            F.close()
        



    

##########################################################################
############################### Root #####################################
##########################################################################

class Root(Node):
    def __init__(self,**kwargs):
        Node.__init__(self,**kwargs)
        
        self.SearchNodePath()
        self.Print()
        #self.WriteTxtStr(f"{self._path}/TreeStructure.txt")

    def WriteTxt(self,file,value):
        with io.open(file, "w", encoding='utf-8') as F:
            F.write(value)
            F.close()
        



if __name__ == "__main__":
    T = Root(path=_FP,error=True)
    print()
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
















