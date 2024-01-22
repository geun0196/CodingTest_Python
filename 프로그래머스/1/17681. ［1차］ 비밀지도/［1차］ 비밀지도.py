def solution(n, arr1, arr2):
    answer = []
    
    temp_list_arr1 = []
    temp_list_arr2 = []

    for arr1_num in arr1:
        arr_binary_1 = change2binary(arr1_num, n)
        temp_list_arr1.append(arr_binary_1)

    for arr2_num in arr2:
        arr_binary_2 = change2binary(arr2_num, n)
        temp_list_arr2.append(arr_binary_2)


    for i in range(len(temp_list_arr1)):
        temp_str = ''
        for j in temp_list_arr1[i]:
            if j == '0':
                temp_str += ' '
            else:
                temp_str += '#'
        temp_list_arr1[i] = temp_str

    for i in range(len(temp_list_arr2)):
        temp_str = ''
        for j in temp_list_arr2[i]:
            if j == '0':
                temp_str += ' '
            else:
                temp_str += '#'
        temp_list_arr2[i] = temp_str

    for i in range(n):
        temp = ''
        for j in range(len(temp_list_arr1)):
            if temp_list_arr1[i][j] == '#' or temp_list_arr2[i][j] == '#':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer

def change2binary(n, digit):
    num = ""

    while n > 0:
        num += str(n % 2)
        n //= 2
    
    return num[::-1].zfill(digit)