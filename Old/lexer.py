#--encoding:utf-8--
import copy as cp
def Scan(ProgramString):
    ProgramString=ProgramString.lower()
    SubStrings=[]
    SubString=""
    State="#"
    for Char in ProgramString:
        #print(Char)
        if Char.isalpha():
            #状态不变
            #print("alpha")
            if State=="alpha" or State=="#":
                SubString+=Char
            #状态变
            else:
                SubStrings.append(SubString)
                SubString=Char
            #更新状态
            State="alpha"
        elif Char.isdigit():
            #状态不变
            #print("digit")
            if State=="digit" or State=="#":
                SubString+=Char
            #状态变
            else:
                SubStrings.append(SubString)
                SubString=Char
            #更新状态
            State="digit"
        elif Char==" ":
            #print("blank")
            #状态不变
            if State=="blank" or State=="#":
                SubString+=Char
            #状态变
            else:
                SubStrings.append(SubString)
                SubString=Char
            #更新状态
            State="blank"
        else:
            #print("Other")
            #状态不变
            if State=="Other" or State=="#":
                SubString+=Char
            #状态变
            else:
                SubStrings.append(SubString)
                SubString=Char
            #更新状态
            State="Other"
    SubStrings.append(SubString)
    
    NewSubStrings=[] 
    for Item  in SubStrings:
        if Item.strip()!="":
            NewSubStrings.append(Item)
    Tokens=[]
    for Item in SubStrings:
        if Item =="let":
            Tokens.append({"TokenType":"let","Content":[]})
        elif Item =="in":
            Tokens.append({"TokenType":"in", "Content":[]})
        elif Item=="if":
            Tokens.append({"TokenType":"if","Content":[]})
        #elif Item=="then":
        #    Tokens.append({"TokenType":"then","Content":[]})
        #elif Item=="else":
        #    Tokens.append({"TokenType":"else","Content":[]})
        elif Item=="=":
            Tokens.append({"TokenType":"EQU","Content":[]})
        elif Item=="-":
            Tokens.append({"TokenType":"DIF","Content":[]})
        elif Item.isdigit():
            Tokens.append({"TokenType":"digit","Content":int(Item)})
        elif Item.isalpha():
            Tokens.append({"TokenType":"VAR","Content":Item}) 
    return Tokens

if __name__ == "__main__":
    #Test
    ProgramString="    let a = 10 in let b=10 in -b a"
    print(Scan(ProgramString))
    #ProgramString="    let a = 10 in let b=10 in if - b a then - a b else -b a"
    #print(Scan(ProgramString))