from ply import lex
from ply import yacc
import sys

ret = 0

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

# will work after more ioerators are implemented
#precedence = (('left', 'ADD', 'SUB')) # Mul and Div will go after

ret = 0

def p_calc(p):
    ''' calc : expression
        | empty '''
    global ret
    ret = run(p[1])

def p_expression(p):
    '''expression : expression ADD expression
                | expression SUB expression'''

    # Starting to generate syntax tree
    p[0] = (p[2], p[1], p[3])

def p_expression_int(p):
    ''' expression : INT'''
    p[0] = p[1]

def p_empty(p):
    ''' empty :'''
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return p[1] + p[2]
        elif p[0] == '-':
            return p[1] - p[2]
    else:
        return p

# This function will change the current line in the vim editor
# Takes in expr to calculate
def evalExpr(line: str):
    global ret
    lexer = lex.lex()
    parser = yacc.yacc()
    parser.parse(line)
    return str(ret)

if __name__ == "__main__":
    print(evalExpr("12 + 24"))

