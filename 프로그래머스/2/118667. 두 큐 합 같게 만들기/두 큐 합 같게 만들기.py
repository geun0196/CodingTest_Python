from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    goal = sum_queue1 + sum_queue2
    init_len = len(queue1)

    # 같은 수를 만들 수 없을때 (case 1)
    if goal % 2 != 0:
        return -1
    
    while True:
        # 같은 수를 만들 수 없을때 (case 2)
        if answer >= init_len * 4:
            return -1
        
        if sum_queue1 > sum_queue2:
            pop = queue1.popleft()
            queue2.append(pop)
            sum_queue1 -= pop
            sum_queue2 += pop
            answer += 1

        elif sum_queue2 > sum_queue1:
            pop = queue2.popleft()
            queue1.append(pop)
            sum_queue2 -= pop
            sum_queue1 += pop
            answer += 1
        
        else:
            break    

    return answer