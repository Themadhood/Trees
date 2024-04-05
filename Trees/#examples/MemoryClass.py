#Program:       MemoryClass
#Purpose:       Organize Memory Data
#Programer:     Themadhood Pequot 3/30/23

_FILE = "AI.Memory.MemoryClass"
_VERSION = "0.0.1"

from THEMADHOOD.Library import Error

"""except Exception as e:
    if self._Error:
        raise
    Error.UploadError([_FILE,_VERSION,"class","def",
                                f"mesage",e],"error sheet")"""

try:
    from .MemoryPeapleClass import *
    from .ReadWright import *
except:
    from MemoryPeapleClass import *
    from ReadWright import *
    


class Memory:
    def __init__(self,**kwgs):
        self.memory = {"Likes":[],
                       "Peaple":[],
                       "Dislikes":[],
                       "Places":dict(),
                       "Favorits":dict(),
                       "Discrioption":Des(kwgs),
                       "Functions":dict()}
        self._Persondct = Person
        self._ReadWright = ReadWright

    def _AddMemOption_(self,name,data=None):
        """Add A memory option"""
        if data == None:
            data = dict()
        self.memory.update({name:data})

    def _AddMemOptSub_(self,MemOpt,name,data=None):
        """add a sub memory option"""
        if data == None:
            data = dict()
        self.memory[MemOpt].update({name:data})

    def _NewPerson_(self,**kw):
        """Returns a class object containing info given"""
        return self._Persondct(**kw)

    def Save(self

















if __name__ == "__main__":
    M=Memory



