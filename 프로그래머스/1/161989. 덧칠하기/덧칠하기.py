def solution(n, m, section):
    answer = 1
    temp = section[0]
    for sec in section:
        if sec > temp+m-1:
            temp = sec
            answer += 1

    return answer