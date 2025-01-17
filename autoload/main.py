from ply import lex
from ply import yacc
from math import atan
from complex import *
from func import Fn

fn = Fn()

ret = 0

tokens = [
    'COMPLEXNUM',
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
    'SIN',
    'COS',
    'TAN',
    'LN'
]

# Check before +/-, NOTE: this will not match integers with no im part, also will not match float coefficents
# FIXME: will not work with negative imaginary part, regex issue
# Use: https://regex101.com/
def t_COMPLEXNUM(t):
    #r'[-]?(\d+)*[i]'
    r'(-?\d+)*([+-])*(-?\d+)*([i])' # Complex Number integer coefficents
    #print(lex.lexer.lexmatch.group(1)) # Whole expr
    print(lex.lexer.lexmatch.group(2)) # Real Part
    print(lex.lexer.lexmatch.group(3)) # (+/-)
    print(lex.lexer.lexmatch.group(4)) # Im Part
    print(lex.lexer.lexmatch.group(5)) # i
    # No real part
    if lex.lexer.lexmatch.group(3) == None:
        t.value = ComplexNum(0.0, float(lex.lexer.lexmatch.group(2)))
        return t
    if lex.lexer.lexmatch.group(4) == None: # no i coefficent
        t.value = ComplexNum(float(lex.lexer.lexmatch.group(2)), 1.0)
    else:
        if lex.lexer.lexmatch.group(3) == '+':
            t.value = ComplexNum(float(lex.lexer.lexmatch.group(2)), float(lex.lexer.lexmatch.group(4)))
        else:
            t.value = ComplexNum(float(lex.lexer.lexmatch.group(2)), -1.0*float(lex.lexer.lexmatch.group(4)))

    #print(t.value)
    return t

t_ADD   = r'\+'
t_SUB   = r'\-'
t_MUL   = r'\*'
t_DIV   = r'\/'
t_POW   = r'\^'
t_LBRAC = r'\('
t_RBRAC = r'\)'
t_SIN   = r'sin'
t_COS   = r'cos'
t_TAN   = r'tan'
t_LN    = r'ln'

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
    r'[-]?(\d*[.])\d+'
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
              ('left', 'SIN', 'COS', 'TAN', 'LN'),
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
    ''' expression : SIN expression
                    | COS expression
                    | TAN expression
                    | LN expression'''
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
                    | PI
                    | COMPLEXNUM'''
    p[0] = p[1]

def p_empty(p):
    ''' empty :'''
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input at:", end="")
    print(p)

def run(p):
    global fn
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
            elif p[0] == 'cos':
                return fn.cos(run(p[1]))
            elif p[0] == 'tan':
                return fn.tan(run(p[1]))
            elif p[0] == 'ln':
                return fn.ln(run(p[1]))
    else:
        return p

# This function will change the current line in the vim editor
# Takes in expr to calculate
def evalExpr(line: str):
    global ret, lexer, parser
    lexer = lex.lex()
    parser = yacc.yacc()
    parser.parse(line)
    if ret == None:
        return line
    return str(ret)

if __name__ == "__main__":
    print(evalExpr(input("calc: ")))

