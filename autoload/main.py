from ply import lex
from ply import yacc

tokens = [
    'INT',
    'ADD',
    'SUB',
]

# This function will change the current line in the vim editor
# Takes in expr to calculate
def evalExpr(var: str):
    return "HelloWorld"

if __name__ == "__main__":
    print(evalExpr("5+5"))

