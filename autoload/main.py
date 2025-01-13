from ply import lex
from ply import yacc
import sys

ret = 0
E   = 2.7182818284
PI  = 3.1415926535

# My Implementations of functions
# TODO: ln, sin, cos, tan, sec, csc, cot, asin, acos, atan, asec, acsc, acot, sinh, cosh, tanh, asinh, acosh, atanh
# TODO: complex numbers implementation?

class Fn:
    def ln(self, x: float) -> float:
            print("UNDEFINED")
            return -1.0

    def sin(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def cos(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def tan(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def asin(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def acos(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def atan(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def sec(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def csc(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

    def cot(self, x: float) -> float:
        print("UNDEFINED")
        return -1.0

fn = Fn()

tokens = [
    'FLOAT',
    'INT',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'POW',
    'LBRAC',
    'RBRAC',
    'E',
    'PI',
    'SIN'
]

t_ADD   = r'\+'
t_SUB   = r'\-'
t_MUL   = r'\*'
t_DIV   = r'\/'
t_POW   = r'\^'
t_LBRAC = r'\('
t_RBRAC = r'\)'
t_SIN   = r'sin'

t_ignore = r' ' # Ignore Spaces

def t_E(t):
    r'E'
    t.value = 2.7182818284
    return t

def t_PI(t):
    r'PI'
    t.value = 3.1415926535
    return t

# Must check float first
def t_FLOAT(t):
    r'[+-]?(\d*[.])\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'-?\d+' # -? for negative integers
    t.value = int(t.value)
    return t

# Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

precedence = (('left', 'E', 'PI'),
              ('left', 'SIN'),
              ('left', 'ADD', 'SUB'),
              ('left', 'MUL', 'DIV'),
              ('left', 'POW'),
              ('left', 'LBRAC', 'RBRAC'))

def p_calc(p):
    ''' calc : expression
        | empty '''
    global ret
    ret = run(p[1])

def p_unary_expression(p):
    ''' expression : SIN expression '''
    p[0] = (p[1], p[2])

def p_bin_expression(p):
    '''expression : expression ADD expression
                | expression SUB expression
                | expression MUL expression
                | expression DIV expression
                | expression POW expression
                '''

    # Generating syntax tree
    p[0] = (p[2], p[1], p[3])

def p_expression_brac(p):
    '''expression : LBRAC expression RBRAC '''
    p[0] = p[2]

def p_expression_int(p):
    ''' expression : INT
                    | FLOAT
                    | E
                    | PI'''
    p[0] = p[1]

def p_empty(p):
    ''' empty :'''
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input at:", end="")
    print(p)

def run(p):
    if type(p) == tuple:
        if len(p) == 3: # Binary Expression
            if p[0] == '+':
                return run(p[1]) + run(p[2])
            elif p[0] == '-':
                return run(p[1]) - run(p[2])
            elif p[0] == '*':
                return run(p[1]) * run(p[2])
            elif p[0] == '/':
                return run(p[1]) / run(p[2])
            elif p[0] == '^':
                return run(p[1]) ** run(p[2])
        elif len(p) == 2: # Unary Expression
            if p[0] == 'sin':
                return fn.sin(run(p[1]))
    else:
        return p

# This function will change the current line in the vim editor
# Takes in expr to calculate
def evalExpr(line: str):
    global ret
    lexer = lex.lex()
    parser = yacc.yacc()
    parser.parse(line)
    if ret == None:
        return line
    return str(ret)

if __name__ == "__main__":
    print(evalExpr(input("calc: ")))

