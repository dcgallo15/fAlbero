let s:script_dir = fnamemodify(resolve(expand('<sfile>', ':p')), ':h')

function! fAlbero#EvalExpr()
python3 << EOF

import sys
import vim

# Ensures Path works correctly so can import
script_dir = vim.eval('s:script_dir')
sys.path.insert(0, script_dir)

import main

vim.current.line = main.evalExpr(vim.current.line)
EOF
endfunction


function! fAlbero#EvalExprAppend()
python3 << EOF
import sys
import vim

script_dir = vim.eval('s:script_dir')
sys.path.insert(0, script_dir)

import main

vim.current.line = vim.current.line + " = " + main.evalExpr(vim.current.line)
EOF
endfunction

" FIXME!
function! fAlbero#EvalSelection()
normal gv"xy
let b:context = getreg("x")

python3 << EOF
import sys
import vim

script_dir = vim.eval('s:script_dir')
sys.path.insert(0, script_dir)

import main

b = vim.current.buffer
selectedText = b.vars["context"]
b.vars["context"] = main.evalExpr(selectedText)
EOF

normal gv"_d
put =b:context


endfunction
