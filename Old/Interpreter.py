#--encoding:utf-8--
#Denotation
def NumberToVal(Int):
    return {"DenotationType":"INT","Value":Int}
def BoolToVal(Bool):
    return {"DenotationType":"BOOL","Value":Bool}
def ValToBool(ExpVal):
    assert ExpVal["DenotationType"]=="INT"
    return ExpVal["Value"]
def ValToNumber(ExpVal):
    assert ExpVal["DenotationType"]=="BOOL"
    return ExpVal["Value"]

#Environment
import copy as cp
def EmptyEnv():
    return {}
def ExtendEnv(VarName,DenotationValue,Env):
    NewEnv=cp.deepcopy(Env)
    NewEnv[VarName]=DenotationValue
    return NewEnv
def ApplyEnv(Env,Var):
    return Env[Var]


#BuildExpression
def Program(Exp):
    return {"ExpType":"Program","Children":[Exp]}

def ConstExp(Num):
    return {"ExpType":"Const","Load":Num}

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
       
def ValueOf(Exp,Env):
    def ConstExpHandler(ConstExp,Env):
        assert ConstExp["ExpType"]=="Const"
        return NumberToVal(ConstExp["Load"])
    def DiffExpHandler(DiffExp,Env):
        assert DiffExp["ExpeType"]=="Diff"
        Children=DiffExp["Children"]
        Exp1=Children[0]
        Exp2=Children[1]
        return NumberToVal(ValToNumber(ValueOf(Exp1,Env))-ValToNumber(ValueOf(Exp2,Env)))
    def ZeroExpHandler(ZeroExp,Env):
        assert ZeroExp["ExpType"]=="Zero"
        Children=ZeroExp["Children"]
        Exp=Children[0]
        if ValToNumber(ValueOf(Exp,Env))==0:
            return BoolToVal(True)
        else:
            return BoolToVal(False)
    def IfExpHandler(IfExp,Env):
        assert IfExp["ExpType"]=="If"
        Children=IfExp["Children"]
        Exp1=Children[0]
        Exp2=Children[1]
        Exp3=Children[2]
        assert Exp1["ExpType"]=="Zero"
        if ValToBool(ValueOf(Exp1,Env)):
            return ValueOf(Exp2,Env)
        else:
            return ValueOf(Exp3,Env)
    def VarExpHandler(VarExp,Env):
        assert VarExp["ExpType"]=="Var"
        return ApplyEnv(Env,VarExp["Load"])
    def LetExpHandler(LetExp,Env):
        assert LetExp["ExpType"]=="Let"
        Children=LetExp["Children"]
        VarExp=Children[0]
        Exp=Children[1]
        Body=Children[2]
        assert VarExp["ExpType"]=="Var"
        Env=ExtendEnv(VarExp["Load"],ValueOf(Exp,Env),Env)
        return ValueOf(Body,Env)
    ProductionHandlerDict={"Const":ConstExpHandler,
                            "Var":VarExpHandler,
                            "If":IfExpHandler,
                            "Diff":DiffExpHandler,
                            "Zero":ZeroExpHandler,
                            "Let":LetExpHandler
                            }
    Handler=ProductionHandlerDict[Exp1["ExpType"]]
    return Handler(Exp1,Env)   
    