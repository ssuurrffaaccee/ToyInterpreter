#BuildExpression
def Program(Exp):
    return {"ExpType":"Program","Children":[Exp]}

def ConstExp(NumString):
    return {"ExpType":"Const","Load":NumString}

def DiffExp(Exp1,Exp2):
    return {"ExpType":"Diff","Children":[Exp1,Exp2]}

def ZeroExp(Exp):
    return {"ExpType":"Zero","Children":[Exp]}

def IfExp(Exp1,Exp2,Exp3):
    return {"ExpType":"If","Children":[Exp1,Exp2,Exp3]}

def VarExp(VarName):
    return {"ExpType":"Var","Load":VarName}

def LetExp(VarExp,Exp,Body):
    return {"ExpType":"Let","Children":[VarExp,Exp,Body]}

def AddExp(Exp1,Exp2):
    return {"ExpType":"Add","Children":[Exp1,Exp2]}
    
def MulExp(Exp1,Exp2):
    return {"ExpType":"Mul","Children":[Exp1,Exp2]}

def ProcExp(VarExp,Body):
    return {"ExpType":"Proc","Children":[VarExp,Body]}

def CallExp(VarExp,Exp):
    return {"ExpType":"Call","Children":[VarExp,Exp]}

def LetRecExp(VarExpProc,VarExpParameter,ProcBody,Body):
    return {"ExpType":"LetRec","Children":[VarExpProc,VarExpParameter,ProcBody,Body]}
