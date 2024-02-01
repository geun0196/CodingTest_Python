def solution(board, moves):
    answer = 0

    box = []
    for move in moves:
        column = move - 1
        for i in range(len(board)):
            if board[i][column] != 0:
                box.append(board[i][column])
                board[i][column] = 0
                if len(box) > 1 and box[-1] == box[-2]:
                    answer += 2
                    for _ in range(2):
                        del box[-1]
                break      

    return answer