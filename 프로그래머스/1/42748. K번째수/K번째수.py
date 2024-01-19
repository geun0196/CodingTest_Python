def solution(array, commands):
    answer = []

    for command in commands:
        slice_from, slice_to, index = command

        answer.append(sorted(array[slice_from-1:slice_to])[index-1])
    return answer