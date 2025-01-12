if exists("g:loaded_fAlbero")
    finish
endif

let g:loaded_fAlbero = 1

command! -nargs=0 Current call fAlbero#GetCurrentFile()
command! -nargs=0 HelloWorld call fAlbero#HelloWorld()
