# Eric's handy `vim` commands

## navigation
- `w` move through word by word
- `j` move down a line
- `k` move up a line
- `ctrl-d` page down
- `ctrl-u` page up
- `shift-g` move to end of file
- `:<line number>` go to line number

## clipboard commands
- `shift-v` highlight whole line (visual block)
- `ctrl-v` highlight single character (visual block)
  - use `j` and `k` to highlight more
  - use `d` to cut
  - use `x` to delete
  - use `p` to paste
- `dd` delete/cut a whole line
  - `p` paste this line that we deleted
- `yy` "yank" (copy) a whole line for pasting with `p`

## text insertion mode
- `i` start text insersion
- `a` start appending text
- `shift-i` insert text across multiple lines 
- `shift-a` append text across multiple lines
- `esc` exit text insertion mode

## find and replace
- `/` search a query string
- `r` replace character in place (follow it by the new character)
- `:s/<find>/<replace>/g` find and replace on this line
  - add `%` after the colon to replace on all lines

## undo and redo
- `u` undo the last step
- `ctrl-r` redo the last undone step

## saving and exiting
- `:w` save the file
- `:wq` save the file and exit
- `:q!` exit without saving changes
