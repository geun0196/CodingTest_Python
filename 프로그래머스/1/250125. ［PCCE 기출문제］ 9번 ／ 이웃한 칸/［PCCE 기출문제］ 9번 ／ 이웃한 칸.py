def solution(board, h, w):
    count = 0
    board_len = len(board)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0 , -1]

    for i in range(4):
        h_check = dh[i]
        w_check = dw[i]

        if 0 <= h + h_check < board_len and  0 <= w + w_check < board_len:
            if board[h][w] == board[h + h_check][w + w_check]:
                count += 1
    
    return count