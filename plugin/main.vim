if exists("g:loaded_fAlbero")
    finish
endif

let g:loaded_fAlbero = 1

command! -nargs=0 EvalExpr call fAlbero#EvalExpr()
