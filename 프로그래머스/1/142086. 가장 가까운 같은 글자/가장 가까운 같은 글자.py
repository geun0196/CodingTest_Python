def solution(s):
    answer = []

    d = dict()
    count = 0
    for char in s:
        if char in d:
            # value 가져오고
            value = d[char]
            print(value)
            answer.append(count - value)
            # value(count) 최신화
        else:
            answer.append(-1)

        d[char] = count
        count += 1
    
    return answer