from Production import *
from Interpreter import ValueOfProgram
from DotPrint import PrintProgramToDotFile
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
def CraftProgramProc():
    print("proc(x) -(1,x)")
    Exp1=ConstExp("1")
    Var=VarExp("x")
    Diff=DiffExp(Exp1,Var)
    Parameter=VarExp("x")
    Proc=ProcExp(Parameter,Diff)
    return Program(Proc)
def CraftProgramCall():
    print("let x = proc(x) -(1,x) in (x *(2 3))")
    Const=ConstExp("1")
    Var=VarExp("x")
    Diff=DiffExp(Const,Var)
    Parameter=VarExp("x")
    Proc=ProcExp(Parameter,Diff)
    Const2=ConstExp("2")
    Const3=ConstExp("3")
    Mul=MulExp(Const2,Const3)
    Var1=VarExp("x")
    Call=CallExp(Var1,Mul)
    Var2=VarExp("x")
    Let=LetExp(Var2,Proc,Call)
    return Program(Let)
def CraftProgramLetRec():
    print("letrec d(x) = if zero(x) 1 (d -(x 1)) in d 3")
    #-(x 1)
    Var=VarExp("x")
    Const=ConstExp("1")
    Diff=DiffExp(Var,Const)
    #double -(x 1)
    VarDouble=VarExp("d")
    Call=CallExp(VarDouble,Diff)
    #zero(x)
    Varx=VarExp("x")
    Zero=ZeroExp(Varx)
    Const1=ConstExp("1")
    #if zero(x) 1 (double -(x 1))
    If=IfExp(Zero,Const1,Call)
    #double 3
    Const3=ConstExp("2")
    VarDou=VarExp("d")
    Call1=CallExp(VarDou,Const3)

    #d(x)
    VarD=VarExp("d")
    VarP=VarExp("x")
    
    #whole
    LetRec=LetRecExp(VarD,VarP,If,Call1)

    return Program(LetRec)
def CraftProgramF():
    print("letrec f(x)= if zero(x) 0 +(x,(f -(x 1))) in (f 4)")
    #-(x 1)
    Var=VarExp("x")
    Const=ConstExp("1")
    Diff=DiffExp(Var,Const)
    #f -(x 1)
    VarDouble=VarExp("f")
    Call=CallExp(VarDouble,Diff)
    #+ (x (f -(x 1)))
    VarPlusx=VarExp("x")
    Add=AddExp(VarPlusx,Call)
    #zero(x)
    Varx=VarExp("x")
    Zero=ZeroExp(Varx)
    Const1=ConstExp("0")
    #if zero(x) 1 (double -(x 1))
    If=IfExp(Zero,Const1,Add)
    #f 4
    Const3=ConstExp("4")
    VarDou=VarExp("f")
    Call1=CallExp(VarDou,Const3)

    #d(x)
    VarD=VarExp("f")
    VarP=VarExp("x")
    
    #whole
    LetRec=LetRecExp(VarD,VarP,If,Call1)

    return Program(LetRec)
def RunAndPrint(Program):
    print(Program)
    Result=ValueOfProgram(Program)
    print("--Result--")
    print(Result)
    print("-------------------------------------")
def RunAndExportToDot(Program,FileName):
    RunAndPrint(Program)
    PrintProgramToDotFile(FileName,Program)
if __name__ == "__main__":
    RunAndExportToDot(CraftProgramDiff(),"Diff.gv")
    RunAndPrint(CraftProgramAdd())
    RunAndPrint(CraftProgramMul())
    RunAndPrint(CraftProgramLet())
    RunAndExportToDot(CraftProgramLet(),"Let.gv")
    RunAndPrint(CraftProgramIf())
    RunAndExportToDot(CraftProgramProc(),"Proc.gv")
    RunAndPrint(CraftProgramCall())
    RunAndExportToDot(CraftProgramCall(),"Call.gv")
    RunAndPrint(CraftProgramLetRec())
    RunAndPrint(CraftProgramF())
    RunAndExportToDot(CraftProgramF(),"F.gv")