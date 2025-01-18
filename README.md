# fAlbero
## Evaluates calculation expressions in vim

### Usage and setup:
With **vim-plug**: \
`Plug 'dcgallo15/fAlbero'` 

#### Run `:EvalExpr` while being on the line you want evaluated. 
#### More commands are on the way! `:EvalExprAppend` is ready!

e.g: \
![image](https://github.com/user-attachments/assets/3dd5309b-e44a-4513-8f47-aa0f93cf2b40) \
![image](https://github.com/user-attachments/assets/8d64f8d0-2cbf-4006-b544-92d9035d1001)

### Complex Number Support:
- Complex Numbers are treated as a single number e.g: \
  ![image](https://github.com/user-attachments/assets/c1e2fec6-2686-4267-836b-7ba9cdf3318d) \
  ![image](https://github.com/user-attachments/assets/d9cde266-1e08-4aa3-8a9a-66bb1d6da528)

Complex Numbers support all operations apart from exponentiation and unary operations __yet__.

### Currently supported input:

#### Binary Operations

| Operator        | Symbol |
| --------        | ------- |
| Exponentiate    | ^       | 
| Multiply        | *       |
| Divide          | /       |
| Add             | +       |
| Subtract        | -       |

Brackets are also supported, along with negative integers. \

#### Unary Operations

| Operator        | Symbol  |
| --------        | ------- |
| sin             | sin     | 
| cos             | cos     |
| tan             | tan     |
| ln (log base e) | ln      |

Trig functions take input in radians.

### TODO:
- More functions
- deg function to convert into degrees
- abs and arg for Complex Numbers
- Expanded Complex Number support to functions and exponentiation

### Depends on:
- python3
- python3-ply

### Sources:
- https://www.dabeaz.com/ply/ply.html
