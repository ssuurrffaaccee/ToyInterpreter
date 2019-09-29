#--encoding:utf-8--
#Denotation
def NumberToVal(Int):
    return {"DenotationType":"INT","Value":Int}
def BoolToVal(Bool):
    return {"DenotationType":"BOOL","Value":Bool}
def ValToBool(ExpVal):
    assert ExpVal["DenotationType"]=="BOOL"
    return ExpVal["Value"]
def ValToNumber(ExpVal):
    assert ExpVal["DenotationType"]=="INT"
    return ExpVal["Value"]
