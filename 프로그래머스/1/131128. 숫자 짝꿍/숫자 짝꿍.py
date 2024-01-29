def solution(X, Y):
    answer = ""
    x_list = [0,0,0,0,0,0,0,0,0,0]
    y_list = [0,0,0,0,0,0,0,0,0,0]

    for x in X:
        index = int(x)
        x_list[index] += 1

    for y in Y:
        index = int(y)
        y_list[index] += 1

    for i in range(9, -1, -1):
        while x_list[i] and y_list[i]:
            answer += str(i)
            x_list[i] -= 1
            y_list[i] -= 1

    if not answer:
        return "-1"
    if(answer[0] == '0'):
        return '0'
              
    return answer