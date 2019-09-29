import lexer
import parser
import interpreter

def test(ProgramString):
    Tokens=lexer.Scan(ProgramString)
    Program=parser.ParserProgram(Tokens)
    print(Program)
    print(interpreter.ValueOfProgram(Program))
if __name__ == "__main__":
    ProgramString="    let a = 10 in let b=10 in -b a"
    test(ProgramString)
    print(interpreter.Run(ProgramString))
    ProgramString="    let a = 10 in let b=20 in let c = - b a in   if c 1 2"
    test(ProgramString)
    print(interpreter.Run(ProgramString))