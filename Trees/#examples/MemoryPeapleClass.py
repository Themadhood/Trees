#Program:       MemoryPeapleClass
#Purpose:       Organize Memory Data
#Programer:     Themadhood Pequot 3/30/23



def Person(self,FName=None,LName=None,Mother=None,Father=None,
                 Favs=None,Other=None, **kwgs):
    """Return a dict of details about a purson"""
    return {"FirstName":FName,
            "LastName":LName,
            "Mother":Mother,
            "Father":Father,
            "Favorits":Favs,
            "Discription":_Des(kwgs),
            "Other":Other}

def _Des(eyecolor=None,hairlen=None,haircolor=None,skincolor=None,
        hight=None,Wheght=None):
    """return a dict of apirance"""
    return {"eyecolor":eyecolor,"hairlen":hairlen,"haircolor":haircolor,
            "skincolor":skincolor,"hight":hight,"Wheght":Wheght}

        

if __name__ == "__main__":
    P=Person


