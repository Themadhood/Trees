#program:       PrintDefs
#purpose:       
#progamer:      Themadhood Pequot 1/30/2024

_FILE = "Trees.Tree_Foundation.PrintDefs"
_VERSION = "0.0.1"

import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")


def Print(self,prefix="",end=False):
    try:
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
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([_FILE,_VERSION,"Node","Print",
                           f"failed to construct tree structur Prefix",e],
                          "Functions")

    try:
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
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([_FILE,_VERSION,"Node","Print",
                           f"failed to construct tree structur Prefix",e],
                          "Functions")

    if self.IsRoot():
        self._AfterPrint()

def AfterPrint_(self):
    try:
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
                
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([_FILE,_VERSION,"Node","_TreeStrPrefix",
                           f"failed to construct tree structur Prefix",e],
                          "Functions")
                

def TreeStrPrefix_(self,lvl=0):
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
















