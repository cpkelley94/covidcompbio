# Eric's handy `vim` commands
- `w` move through word by word
- `j` move down a line
- `k` move up a line
- `dd` delete a whole line
  - hit "p" to paste this line that we deleted
- `shift-v` highlight whole line (visual block)
- `ctrl-v` highlight single character (visual block)
  - use "j" and "k" to highlight more
  - use "d" to cut
  - use "x" to delete
  - use "p" to paste
- `u` undo the last step
- `cmd-r` redo the last undone step
- `yy` "yank" (copy) a whole line for pasting with "p"
- `r` replace character in place (follow it by the new character)
- `/` search a query string
- `i` start text insersion
- `a` start appending text
- `shift-i` insert text across multiple lines 
- `shift-a` append text across multiple lines
- `ctrl-d` page down
- `ctrl-u` page up
- `shift-g` to end of file

## colon commands
- `:s/<find>/<replace>/g` - find and replace on this line
  - add "%" after the colon to replace on all lines
- `:<line number>` - go to line number