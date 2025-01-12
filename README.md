# fAlbero
## Calculates expressions in vim

### Usage and setup:
In **vim-plug**: \
`Plug 'dcgallo15/fAlbero'` 

#### Run `:EvalExpr` while being on the line you want evaluated.

e.g: \
![image](https://github.com/user-attachments/assets/3dd5309b-e44a-4513-8f47-aa0f93cf2b40) \
![image](https://github.com/user-attachments/assets/8d64f8d0-2cbf-4006-b544-92d9035d1001)

### Currently supported input:

| Operator        | Symbol |
| --------        | ------- |
| Exponentiate    | ^       | 
| Multiply        | *       |
| Divide          | /       |
| Add             | +       |
| Subtract        | -       |

Brackets are also supported. Along with negative integers.

### TODO:
- Floating point input
- Constants such as: e and pi
- Functions such as: sin and ln

### Depends on:
- python3
- python3-ply

### Sources:
- https://www.dabeaz.com/ply/ply.html
