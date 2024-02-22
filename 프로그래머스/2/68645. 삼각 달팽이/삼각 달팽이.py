def solution(n):
    # 삼각형 구조
    answer = []    
    for i in range(1, n+1):
        tmp_list = []
        for _ in range(1, i+1):
            tmp_list.append(0)
        answer.append(tmp_list)

    num = 1
    x = -1
    y = 0

    # n번만큼 값이 입력됨 -> n이 5일 때: (1,2,3,4,5), (6,7,8,9), (10,11,12), (13,14), (15)
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0: # 아래방향
                x+=1
            elif i % 3 == 1: # 오른방향
                y+=1
            else: #윗방향
                x-=1
                y-=1
            
            answer[x][y] = num
            num+=1   

    return sum(answer, [])