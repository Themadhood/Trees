__Program__     = "IndividualRelations"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/22/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""


try:
    from . import Generic
    from . import Individual_Relatons_Suport as _SuportDefs
except:
    import Generic
    import Individual_Relatons_Suport as _SuportDefs

Error = Generic.Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

class Node(Generic.Node):
    _node = Generic.Node
    _alive = True

    _AfterPrint = _SuportDefs.AfterPrint_
    Print = _SuportDefs.Print
    
    def __init__(self,**kwargs):
        Generic.Node.__init__(self,**kwargs)

        
        self.name = {"First":self.name,
                     "Middle":[],
                     "Last":None}
        
        self._parents = {"Birth":{"Mother":None,"Father":None},
                         "Step":None,
                         "Inlaws":None,
                         "Adopted":None}

        self._children = {"Birth":None,
                          "Adopted":None,
                          "Pet":None}

        self._friends = []

        self._signifacantOthers = {"Married":[],
                                   "Datting":[],
                                   "EX":[]}

        #day info = {"Date":None,"Time":None,"Cause":}
        self._info = {"birth":None,
                      "Death":None,

                      "Likes":[],
                      "Dislikes":[],
                      "Medical":{"Ilneses":None},

                      "Pronowns":None,

                      "Adresses":None,
                      #Name{zip,contry,city,state,adress,apartment #}
                      "Phone Numbers":None,#{Name:number}
                      "Emailes":None}

        self._fisicaldiscription = {"Gender":{"Birth":None,
                                              "Current":None},
                                    "Ethisity/Race":None,
                                    "Hair":{"head":None,
                                            "Fashal":{"Under Jaw":None,
                                                      "Chin":None,
                                                      "Lower Lip":None,
                                                      "Upper Lip":None,
                                                      "Side":None}},
                                    "Mesurments":{"Hight":None,
                                                  "Weight":None,
                                                  "Solder Whith":None,
                                                  "Arm Lenth":None},
                                    "Eye Color":None,
                                    "Skin Tone":None,
                                    "fisical identifiers":[]}
        #hair{"Origanal color":None,"Current color":None,"Lenth":None}

        self._Imployment = None
        #prymary ...
            #company
            #job description
            #title
            #adress
            #phone #
            #salery


    def GetHight(self):
        if self._printed:
            return 0
        self._printed = True
        
        hight = 0
        
        childrenTypes = list(self._children)
        for childType in childrenTypes:
            if self._children[childType] != None:
                
                children = list(self._children[childType])
                for child in children:
                    if self._children[childType][child] != None:
                        
                        chHight = self._children[childType][child].GetHight()
                        if chHight > hight:
                            hight = chHight
                
        if self.IsRoot():
            self._AfterPrint()

        hight += 1  
        return hight


    def GetSize(self):
        if self._printed:
            return 0
        
        self._printed = True
        size = 1
        
        childrenTypes = list(self._children)
        for childType in childrenTypes:
            if self._children[childType] != None:
                
                children = list(self._children[childType])
                for child in children:
                    if self._children[childType][child] != None:
                        
                        size += self._children[childType][child].GetSize()
                
        if self.IsRoot():
            self._AfterPrint()
            
        return size


    def _MakeNode(self,firstName):
        new = Node(name=firstName, error=self._Error)
        return new


    def AddChild(self,firstName,childType="Birth",node=None):
        if node == None:
            node = self._MakeNode(firstName)

        childType = childType.capitalize()
        if childType in list(self._children):
            if self._children[childType] == None:
                self._children[childType] = dict()

            if firstName in list(self._children[childType]):
                for i in range(0,len(self._children[childType])):
                    name = f"{firstName}{i}"
                    if name not in list(self._children[childType]):
                        break
            else:
                name = firstName

            self._children[childType].update({name:node})
            
        else:
            print(f"Child type {childType} not in {list(self._children)}")

        
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
        





if __name__ == "__main__":
     root = Node(name="root",error=True)
     root.Print()
     print(root.GetHight())
     print(root.GetSize())
















