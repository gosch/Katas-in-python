def seatsInTheater(nCols, nRows, col, row):
    total = nCols*nRows
    cols = (col-1) * nRows
    down = (nCols - col+1) * (nRows - (nRows-row))
    return total - cols - down


print(seatsInTheater(16, 11, 5, 3))
