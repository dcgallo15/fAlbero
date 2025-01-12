let s:script_dir = fnamemodify(resolve(expand('<sfile>', ':p')), ':h')

function! fAlbero#HelloWorld()
python3 << EOF

import sys
import vim

# Ensures Path works correctly so can import
script_dir = vim.eval('s:script_dir')
sys.path.insert(0, script_dir)

import main

vim.current.line = main.helloWorld(vim.current.line)
EOF
endfunction

function! fAlbero#GetCurrentFile()
    echo ls
endfunction
