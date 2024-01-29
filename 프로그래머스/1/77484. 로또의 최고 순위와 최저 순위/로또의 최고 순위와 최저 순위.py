def solution(lottos, win_nums):
    #{맞은개수: 등수}
    answer = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    count = 0
    for num in win_nums:
        if num in lottos:
            lottos.remove(num)
            count += 1
    
    max_pride = count + lottos.count(0)
    min_pride = count

    return [answer[max_pride], answer[min_pride]]