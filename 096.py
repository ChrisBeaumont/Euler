from random import shuffle
from numpy import argsort

#solve board by using backtracking guess-and-check
#invariant: We never place a tile that immediately creates
#           a conflict
def sudoku(board, start=0):

    if start == 81: return True

    if board[start] != 0: 
        return sudoku(board, start+1)

    for m in valid_moves(board, start):
        board[start] = m
        if sudoku(board, start):
            return True
        board[start] = 0
    return False

def valid_moves(board, pos):
    if board[pos] != 0: 
        return []
    row = pos / 9
    col = pos % 9
    block = ((row / 3) % 3) + 3 * (row / 3)
    valid = [True] * 10

    #remove moves that cause conflicts
    for i in range(9):
        #col
        j = row * 9 + i
        #row
        k = col + i * 9
        #block
        l = (i % 3) + 9 * (i / 3) + \
            3 * (col / 3) + 27 * (row / 3)
        for p in (j,k,l):
            if p == pos: continue
            valid[board[p]] = False

    result = [i for i in range(1, 10) if valid[i]]
    return result

def get_boards():
    result = []
    data = open('sudoku.txt').readlines()
    for i in range(1, len(data), 10):
        b = data[i:i+9]
        b = ''.join([x.strip() for x in b])
        result.append(b)        
    return result
        

answer = 0
for b in get_boards():
    board = map(int, b)
    assert sudoku(board)
    answer += board[0] * 100 + board[1] * 10 + board[2]

print answer
