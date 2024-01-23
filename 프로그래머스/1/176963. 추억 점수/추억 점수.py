def solution(names, yearnings, photos):
    answer = []
    
    info = dict(zip(names,yearnings))
    for photo in photos:
        count = 0
        for person in photo:
            if person in info:
                count += info[person]
            else:
                continue
        answer.append(count)    

    return answer