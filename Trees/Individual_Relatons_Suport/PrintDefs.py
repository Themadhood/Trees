__Program__     = "Individual_Relations_Suport.PrintDefs"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/22/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""

import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

def AfterPrint_(self):
    try:
        if self._printed:
            self._printed = False
            #check for children != none
            validChildren = []
            childrenTypes = list(self._children)
            for childType in childrenTypes:
                if self._children[childType] != None:
                    children = list(self._children[childType])
                    
                    for child in children:
                        if self._children[childType][child] != None:
                            validChildren.append(child)

                    #call children to print
                    for child in validChildren:
                        if child == validChildren[-1]:
                            self._children[child]._AfterPrint()
                        else:
                            self._children[child]._AfterPrint()
                
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"Node","_AfterPrint",
                           f"failed to reset print",e],"Functions")

def Print(self,prefix="",end=False):
    try:
        if self._printed:
            print(f"{prefix}({self.name})")
            return
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
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"Node","Print",
                           f"failed to construct tree structur Prefix",e],
                          "Functions")

    try:
        #check for children != none
        children = list(self._children)
        validChildren = []
        childrenTypes = list(self._children)
        for childType in childrenTypes:
            if self._children[childType] != None:
                children = list(self._children[childType])
                
                for child in children:
                    if self._children[childType][child] != None:
                        validChildren.append(child)

                #call children to print
                for child in validChildren:
                    if child == validChildren[-1]:
                        self._children[childType][child].Print(prefix + "└ ",True)
                    else:
                        self._children[childType][child].Print(prefix + "├ ")
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"Node","Print",
                           f"failed to construct tree structur Prefix",e],
                          "Functions")

    if self.IsRoot():
        self._AfterPrint()
















