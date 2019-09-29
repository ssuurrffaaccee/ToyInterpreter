#--encoding:utf-8--
#Environment
import copy as cp
def EmptyEnv():
    return {}
def ExtendEnv(VarName,DenotationValue,Env):
    NewEnv={"Parent":Env}
    NewEnv[VarName]=DenotationValue
    print("    --Environment--")
    print(NewEnv)
    return NewEnv
def ApplyEnv(Env,Var):
    try:
         return Env[Var]
    except KeyError:
        return ApplyEnv(Env["Parent"],Var)