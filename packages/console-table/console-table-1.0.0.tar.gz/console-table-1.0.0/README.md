# table
make tables of data in the console
## example
test.csv
```csv
1,2,3
2,4,6
3,6,9
```
`C:\Users\User>py -m table test.csv --style 5`  
output:
```
╭───┬───┬───╮
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 2 │ 4 │ 6 │
├───┼───┼───┤
│ 3 │ 6 │ 9 │
╰───┴───┴───╯
```