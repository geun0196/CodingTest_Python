def solution(dartResult):
    answer_list = []
    index = -1
    num = ''
    for char in dartResult:
        if char.isalpha():
            num = int(num)            
            if char.upper() == 'D':
                num = num**2
            elif char.upper() == 'T':
                num = num**3
            answer_list.append(num)
            index += 1
            num = ''

        elif char.isdecimal():
            num += char
    
        else:
            if char == '*':
                if index > 0:
                    answer_list[index-1] *= 2
                    answer_list[index] *= 2
                else:
                    answer_list[index] *= 2
            else:
                answer_list[index] *= (-1)
    return sum(answer_list)