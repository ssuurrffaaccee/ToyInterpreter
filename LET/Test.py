from Production import *
from Interpreter import ValueOfProgram

#Test
def CraftProgramDiff():
   print("10-20")
   Exp1=ConstExp("10")
   Exp2=ConstExp("20")
   Diff=DiffExp(Exp1,Exp2)
   return Program(Diff)
def CraftProgramAdd():
    print("1+1")
    Exp1=ConstExp("1")
    Exp2=ConstExp("1")
    Add=AddExp(Exp1,Exp2)
    return Program(Add)
def CraftProgramMul():
    print("3*2")
    Exp1=ConstExp("3")
    Exp2=ConstExp("2")
    Mul=MulExp(Exp1,Exp2)
    return Program(Mul)
def CraftProgramLet():
    print("let b=10 in let a=20 in a-b")
    Var1=VarExp("a")
    Var2=VarExp("b")
    Diff=DiffExp(Var1,Var2)
    Let_a=LetExp(Var1,ConstExp("10"),Diff)
    Let_b=LetExp(Var2,ConstExp("20"),Let_a)
    return Program(Let_b)
def CraftProgramIf():
    print("let b=10 in let a=20 in if a-b 0 1 ")
    Var1=VarExp("a")
    Var2=VarExp("b")
    Diff=DiffExp(Var1,Var2)
    Zero=ZeroExp(Diff)
    If=IfExp(Zero,ConstExp(0),ConstExp(1))
    Let_a=LetExp(Var1,ConstExp("10"),If)
    Let_b=LetExp(Var2,ConstExp("20"),Let_a)
    return Program(Let_b)
def RunAndPrint(Program):
    print(Program)
    Result=ValueOfProgram(Program)
    print("--Result--")
    print(Result)
    print("-------------------------------------")
if __name__ == "__main__":
    RunAndPrint(CraftProgramDiff())
    RunAndPrint(CraftProgramAdd())
    RunAndPrint(CraftProgramMul())
    RunAndPrint(CraftProgramLet())
    RunAndPrint(CraftProgramIf())