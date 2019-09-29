
Head="digraph {\n"
Tail="}\n"

class Name:
    def __init__(self):
        self.Count=0
    def GetName(self):
         Name="N"+str(self.Count)
         self.Count=self.Count+1
         return Name
GlobalNameGen=Name()
    


def PointToHelpler(Children,ParentName):
    ParentString=""
    DefineString=""
    Names=[GlobalNameGen.GetName() for Child in Children]
    #don't define self ,parent already defined 
    for ChildrenWithName in zip(Names,Children):
        if ChildrenWithName[1]["ExpType"] in ["Var", "Const"]:
            DefineString=DefineString+ChildrenWithName[0]+"[label=\""+ChildrenWithName[1]["ExpType"]+"_"+ChildrenWithName[1]["Load"]+"\"];\n"
        else:
            DefineString=DefineString+ChildrenWithName[0]+"[label=\""+ChildrenWithName[1]["ExpType"]+"\"];\n"
    for Name in Names:
        ParentString=ParentString+ParentName+"->"+Name+";\n"
    return DefineString+ParentString,Names
def BuildChildrenHelpler(Children,Names):
    ChildrenString=""
    for ChildWithName in zip(Names,Children):
        ChildrenString=ChildrenString+ToDot(ChildWithName[1],ChildWithName[0])
    return ChildrenString
def BuildHelpler(Exp,Name):
    Children=Exp["Children"]
    ExpString,Names=PointToHelpler(Children,Name)
    return ExpString+BuildChildrenHelpler(Children,Names)
def BuildEmtpy(Exp,Names):
    return ""
def ToDot(Exp,Name):
    Handler=None
    if Exp["ExpType"] in ["Var","Const"]:
        Handler=BuildEmtpy
    else:
        Handler=BuildHelpler
    return Handler(Exp,Name)

def PrintProgramToDotFile(FileName,Program):
    OutputString=""
    
    print(ToDot(Program,"Program"))
    OutputString=OutputString+Head+ToDot(Program,"Program")+Tail
    print(type(Head))

    with open(FileName,"w") as fd:
        fd.write(OutputString)

