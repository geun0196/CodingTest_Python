def solution(nums):
    answer = 0
    
    temp = []
    for num in nums:
        if len(temp) < len(nums)/2 and num not in temp:
            temp.append(num)
    return len(temp)