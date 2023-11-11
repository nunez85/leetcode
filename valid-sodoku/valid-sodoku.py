from collections import defaultdict

def isValidSudoku(board: list[list[str]]) -> bool:
    row = defaultdict(set)
    col = defaultdict(set)
    squares = defaultdict(set)
    for x, r in enumerate(board):
        for y, number in enumerate(r):
            if number == ".":
                continue
            if (number in row[x] or 
                number in col[y] or 
                number in squares[(x//3, y//3)]):
                return False
            squares[(x//3, y//3)].add(number)
            row[x].add(number)
            col[y].add(number)
    
    return True

input = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

output = isValidSudoku(input)
print(output)