__Program__     = "Individual_Relations_Suport.SearchDefs"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/23/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""


import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

        
def Search(self,value=None,valueType="First Name"):
    if self._printed:
        return []
    self._printed = True
    
    resalt = self._Search(value,valueType)
    
    childrenTypes = list(self._children)
    for childType in childrenTypes:
        if self._children[childType] != None:
            
            children = list(self._children[childType])
            for child in children:
                if self._children[childType][child] != None:
                    
                    resalt += self._children[childType][child].Search(value,valueType)
            
    if self.IsRoot():
        self._AfterPrint()
        
    return resalt

def _Search(self,value=None,valueType="First Name"):
    return []
        

"""
try:
    pass
except Exception as e:
    if self._Error:
        raise
    Error.UploadError([__Program__,__version__,"Node","Print",
                       f"failed to construct tree structur Prefix",e],
                      "Functions")
                          """



if __name__ == "__main__":
     root = Node(name="root",error=True)
     root.Print()
     print(root.GetHight())
     print(root.GetSize())
















