def solution(number, k):
    stack = []

    for num in number:
        if len(stack) == 0:
            stack.append(num)
            continue
        
        if stack[-1] < num:
            while k > 0 and stack and stack[-1] < num:
                stack.pop()
                k -= 1

                if k < 0:
                    break
            stack.append(num)

        else:
            stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    return ''.join(stack)