import interpreter as inter

def Pop(inList):
    try:
        Item=inList.pop(0)
        #print(Item)
        return Item
    except IndexError:
        return {}
def Parser(Tokens):
    Token=Pop(Tokens)
    if Token["TokenType"]=="let": 
        VarToken=Pop(Tokens)
        assert VarToken["TokenType"]=="VAR"
        EQUToken=Pop(Tokens)
        assert EQUToken["TokenType"]=="EQU"
        Exp2=Parser(Tokens)
        InToken=Pop(Tokens)
        assert InToken["TokenType"]=="in"
        Exp3=Parser(Tokens)
        return inter.Let_Exp(VarToken["Content"],Exp2,Exp3)
    elif Token["TokenType"]=="VAR":
        return inter.Var_Exp(Token["Content"])
    elif Token["TokenType"]=="if":
        Exp1=Parser(Tokens)
        ZeroExp1=inter.Zero_Exp(Exp1)
        Exp2=Parser(Tokens)
        Exp3=Parser(Tokens)
        return inter.If_Exp(ZeroExp1,Exp2,Exp3)
    elif Token["TokenType"]=="digit":
        return inter.Const_Exp(Token["Content"])
    elif Token["TokenType"]=="DIF":
        Exp1=Parser(Tokens)
        Exp2=Parser(Tokens)
        return inter.Diff_Exp(Exp1,Exp2)
    else:
        print("Somthing Wrong !")
def ParserProgram(Tokens):
    return inter.A_Program(Parser(Tokens))

if __name__ == "__main__":
    Tokens=[{'TokenType': 'let', 'Content': []}, 
            {'TokenType': 'VAR', 'Content': 'a'},
            {'TokenType': 'EQU', 'Content': []},
            {'TokenType': 'digit', 'Content': 10}, 
            {'TokenType': 'in', 'Content': []}, 
            {'TokenType': 'let', 'Content': []}, 
            {'TokenType': 'VAR', 'Content': 'b'}, 
            {'TokenType': 'EQU', 'Content': []}, 
            {'TokenType': 'digit', 'Content': 10}, 
            {'TokenType': 'in', 'Content': []}, 
            {'TokenType': 'DIF', 'Content': []}, 
            {'TokenType': 'VAR', 'Content': 'b'}, 
            {'TokenType': 'VAR', 'Content': 'a'}]
    print(ParserProgram(Tokens))
