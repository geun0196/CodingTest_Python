jipyo = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}

def solution(survey, choices):
    answer = ''

    for i in zip(survey, choices):
        if i[1] == 1:
            jipyo[i[0][0]] += 3
        elif i[1] == 2:
            jipyo[i[0][0]] += 2
        elif i[1] == 3:
            jipyo[i[0][0]] += 1
        elif i[1] == 5:
            jipyo[i[0][1]] += 1
        elif i[1] == 6:
            jipyo[i[0][1]] += 2
        elif i[1] == 7:
            jipyo[i[0][1]] += 3

    if jipyo['R'] < jipyo['T']:
        answer += "T"
    else:
        answer += "R"

    if jipyo['C'] < jipyo['F']:
        answer += 'F'
    else:
        answer += 'C'
    
    if jipyo['J'] < jipyo['M']:
        answer += 'M'
    else:
        answer += 'J'

    if jipyo['A'] < jipyo['N']:
        answer += 'N'
    else:
        answer += 'A'

    return answer