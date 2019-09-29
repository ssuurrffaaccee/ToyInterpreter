#--encoding:utf-8--
from Denotation import *
from Environment import ApplyEnv,ExtendEnv,EmptyEnv

def ValueOf(Exp,Env):
    def ConstExpHandler(ConstExp,Env):
        assert ConstExp["ExpType"]=="Const"
        return NumberToVal(int(ConstExp["Load"]))
    def DiffExpHandler(DiffExp,Env):
        assert DiffExp["ExpType"]=="Diff"
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
        #print(VarExp["Load"])
        #print(ValueOf(Exp,Env))
        NewEnv=ExtendEnv(VarExp["Load"],ValueOf(Exp,Env),Env)
        return ValueOf(Body,NewEnv)
    def AddExpHandler(AddExp,Env):
        assert AddExp["ExpType"]=="Add"
        Children=AddExp["Children"]
        Exp1=Children[0]
        Exp2=Children[1]
        return NumberToVal(ValToNumber(ValueOf(Exp1,Env))+ValToNumber(ValueOf(Exp2,Env)))
    def MulExpHandler(MulExp,Env):
        assert MulExp["ExpType"]=="Mul"
        Children=MulExp["Children"]
        Exp1=Children[0]
        Exp2=Children[1]
        return NumberToVal(ValToNumber(ValueOf(Exp1,Env))*ValToNumber(ValueOf(Exp2,Env)))
    ProductionHandlerDict={"Const":ConstExpHandler,
                            "Var":VarExpHandler,
                            "If":IfExpHandler,
                            "Diff":DiffExpHandler,
                            "Zero":ZeroExpHandler,
                            "Let":LetExpHandler,
                            "Add":AddExpHandler,
                            "Mul":MulExpHandler
                            }
    Handler=ProductionHandlerDict[Exp["ExpType"]]
    return Handler(Exp,Env)   
    
def ValueOfProgram(Program):
    assert Program["ExpType"]=="Program"
    return ValueOf(Program["Children"][0],EmptyEnv)

