from ply import lex
from ply import yacc

tokens = [
    'INT',
    'ADD',
    'SUB',
]

t_ADD = r'\+'
t_SUB = r'\-'

t_ignore = r' ' # Ignore Spaces

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def tokenise(lexer, line: str):
    # Tokenise:
    tokens = []
    lexer.input(line)
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        tokens.append(tok)
    return tokens


# This function will change the current line in the vim editor
# Takes in expr to calculate
def evalExpr(line: str):
    lexer = lex.lex()
    tokens = tokenise(lexer, line)
    print(tokens)
    return "FUNCTION NOT YET FINISHED RETURN VAL OF evalExpr"

if __name__ == "__main__":
    print(evalExpr("5+5"))

