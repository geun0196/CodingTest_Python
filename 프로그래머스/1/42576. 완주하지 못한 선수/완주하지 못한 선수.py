def solution(participant, completion):
    my_dic = {}
    
    for part in participant:
        if part in my_dic:
            my_dic[part] += 1
        else:
            my_dic[part] = 1
        
    for com in completion:
        my_dic[com] -= 1
    
    return max(my_dic, key=my_dic.get)