def generate(numRows: int) -> list[list[int]]:
    rows = [[1]]

    if numRows == 1:
        return rows 


    i = 0
    while i < numRows - 1:
        left = 0
        right = 1
        newRow = [1]
        while right < len(rows[-1]):
            newRow.append(rows[-1][left] + rows[-1][right])
            right += 1
            left += 1
        
        newRow.append(1)
        rows.append(newRow)
        i += 1

    return rows
