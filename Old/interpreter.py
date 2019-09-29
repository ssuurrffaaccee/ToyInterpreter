#--encoding:utf-8--
#ExpVal
def Num_Val(Int):
    return {"Type":"INT","Value":Int}
def Bool_Val(Bool):
    return {"Type":"BOOL","Value":Bool}
def ExpVal_Num(ExpVal):
    assert ExpVal["Type"]=="INT"
    return ExpVal["Value"]
def ExpVal_Bool(ExpVal):
    assert ExpVal["Type"]=="BOOL"
    return ExpVal["Value"]



#Expression 
def A_Program(Exp):
    return {"ExpType":"Program","Content":Exp}

def Const_Exp(Num):
    return {"ExpType":"Const","Content":Num}

def Diff_Exp(Exp1,Exp2):
    return {"ExpType":"Diff","Content":[Exp1,Exp2]}

def Zero_Exp(Exp):
    return {"ExpType":"Zero","Content":Exp}

def If_Exp(Exp1,Exp2,Exp3):
    return {"ExpType":"If","Content":[Exp1,Exp2,Exp3]}

def Var_Exp(Var):
    return {"ExpType":"Var","Content":Var}

def Let_Exp(Var,Exp,Body):
    return {"ExpType":"Let","Content":[Var,Exp,Body]}


#Environment
import copy as cp
def Empty_Env():
    return {}
def Extend_Env(Var,PY_Value,Env):
    NewEnv=cp.deepcopy(Env)
    NewEnv[Var]=PY_Value
    return NewEnv
def Apply_Env(Env,Var):
    return Env[Var]


#Interpreter
def ValueOfProgram(Program):
    assert Program["ExpType"]=="Program"
    return ValueOf(Program["Content"],Empty_Env())
def ScanAndParse(ProgramString):
    return {}
def Run(ProgramString):
    Program=ScanAndParse(ProgramString)
    return ValueOfProgram(Program)


def ValueOf(Exp1,Env):
    def ConstExpHandler(ConstExp,Env):
        assert ConstExp["ExpType"]=="Const"
        return Num_Val(ConstExp["Content"])
    
    def VarExpHandler(VarExp,Env):
        assert VarExp["ExpType"]=="Var"
        return Apply_Env(Env,VarExp["Content"])
    
    def DiffExpHandler(DiffExp,Env):
        assert DiffExp["ExpType"]=="Diff"
        Val1=ValueOf(DiffExp["Content"][0],Env)
        Val2=ValueOf(DiffExp["Content"][1],Env)
        #print(Env)
        return Num_Val(ExpVal_Num(Val1)-ExpVal_Num(Val2))
    def ZeroExpHandler(ZeroExp,Env):
        assert ZeroExp["ExpType"]=="Zero"
        Val1=ValueOf(ZeroExp["Content"],Env)
        if ExpVal_Num(Val1)==0:
            return Bool_Val(True)
        else:
            return Bool_Val(False)
    def IfExpHandler(IfExp,Env):
        assert IfExp["ExpType"]=="If"
        assert IfExp["Content"][0]["ExpType"]=="Zero"
        Val1=ValueOf(IfExp["Content"][0],Env)#这里存在一个假设:Exp1是ZeroExp
        #print(Val1)
        if ExpVal_Bool(Val1):
            return ValueOf(IfExp["Content"][1],Env)
        else:
            return ValueOf(IfExp["Content"][2],Env)
    def LetExpHandler(LetExp,Env):
        assert LetExp["ExpType"]=="Let"
        LetContent=LetExp["Content"]
        
        return ValueOf(LetContent[2],Extend_Env(LetContent[0],ValueOf(LetContent[1],Env),Env))
    ProductionHandlerDict={"Const":ConstExpHandler,
                            "Var":VarExpHandler,
                            "If":IfExpHandler,
                            "Diff":DiffExpHandler,
                            "Zero":ZeroExpHandler,
                            "Let":LetExpHandler
                            }
    Handler=ProductionHandlerDict[Exp1["ExpType"]]
    return Handler(Exp1,Env)    
#Test
def CraftProgramDiff():
   print("10-20")
   Exp1=Const_Exp(10)
   Exp2=Const_Exp(20)
   Diff=Diff_Exp(Exp1,Exp2)
   return A_Program(Diff)
def CraftProgramLet():
    print("let b=10 in let a=20 in a-b")
    Var1=Var_Exp("a")
    Var2=Var_Exp("b")
    Diff=Diff_Exp(Var1,Var2)
    Let_a=Let_Exp("a",Const_Exp(10),Diff)
    Let_b=Let_Exp("b",Const_Exp(20),Let_a)
    return A_Program(Let_b)
def CraftProgramIf():
    print("let b=10 in let a=20 in if a-b 0 1 ")
    Var1=Var_Exp("a")
    Var2=Var_Exp("b")
    Diff=Diff_Exp(Var1,Var2)
    Zero=Zero_Exp(Diff)
    If=If_Exp(Zero,Const_Exp(0),Const_Exp(1))
    Let_a=Let_Exp("a",Const_Exp(10),If)
    Let_b=Let_Exp("b",Const_Exp(20),Let_a)
    return A_Program(Let_b)
if __name__ == "__main__":
    print(CraftProgramDiff())
    print(ValueOfProgram(CraftProgramDiff()))
    print("--------------------------------")
    print(CraftProgramLet())
    print(ValueOfProgram(CraftProgramLet()))
    print("--------------------------------")
    print(CraftProgramIf())
    print(ValueOfProgram(CraftProgramIf()))
