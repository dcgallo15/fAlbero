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

def toComplex(x):
    return ComplexNum(x, 0)

# NOTE: this will not match integers with no im part, also will not match float coefficents
# Use: https://regex101.com/
def t_COMPLEXNUM(t):
    #r'([-+])*(\d+)*([-+])*(-?\d+)*([i])' # Complex Number integer coefficents
    r'([-+])*(\d*[.]?\d+)*([-+])*(\d*[.]?\d+)*([i])' # Complex Number floating point coefficents

    #print(lex.lexer.lexmatch.group(1)) # Whole expr
    #print(lex.lexer.lexmatch.group(2)) # (+/-)
    #print(lex.lexer.lexmatch.group(3)) # Real Part
    #print(lex.lexer.lexmatch.group(4)) # (+/-)
    #print(lex.lexer.lexmatch.group(5)) # Im Part
    #print(lex.lexer.lexmatch.group(6)) # i

    # Set Real
    re = 0.0
    if lex.lexer.lexmatch.group(4) != None:
        re = float(lex.lexer.lexmatch.group(3))
        if lex.lexer.lexmatch.group(2) == '-':
            re = -1.0*re
    # Set Im
    im = 0
    if lex.lexer.lexmatch.group(5) == None: # no i coefficent
        if lex.lexer.lexmatch.group(4) == None: # If no real part
            if lex.lexer.lexmatch.group(3) == None:
                im = 1.0
            else:
                im = float(lex.lexer.lexmatch.group(3))
                if lex.lexer.lexmatch.group(2) == '-':
                    im = -1.0*im
        else:
            im = 1.0
    else:
        im = float(lex.lexer.lexmatch.group(5))
        if lex.lexer.lexmatch.group(4) == '-':
            im = -1.0*im

    t.value = ComplexNum(re, im)
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
              ('left', 'ADD', 'SUB', 'COMPLEXNUM'),
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

# Here need to check types to ensure int/floats are not composed with complex numbers
def run(p):
    global fn
    if type(p) == tuple:
        if len(p) == 3: # Binary Expression
            if p[0] == '+':
                tmp = run(p[2])
                if isinstance(tmp, ComplexNum):
                    return toComplex(run(p[1])) + tmp
                else:
                    return run(p[1]) + tmp
            elif p[0] == '-':
                tmp = run(p[2])
                if isinstance(tmp, ComplexNum):
                    return toComplex(run(p[1])) - tmp
                else:
                    return run(p[1]) - tmp
            elif p[0] == '*':
                tmp = run(p[2])
                if isinstance(tmp, ComplexNum):
                    return toComplex(run(p[1])) * tmp
                else:
                    return run(p[1]) * tmp
            elif p[0] == '/':
                tmp = run(p[2])
                if isinstance(tmp, ComplexNum):
                  return toComplex(run(p[1])) / tmp
                else:
                    return run(p[1]) / tmp
            elif p[0] == '^':
                # TODO: Implement complex^complex
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

