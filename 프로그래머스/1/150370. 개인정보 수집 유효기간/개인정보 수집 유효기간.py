def solution(today, terms, privacies):
    answer = []

    term_dic = {term.split()[0]: term.split()[1] for term in terms}

    for i, p in enumerate(privacies):
        x = p.split()
        term = int(term_dic[x[1]])
        info_get_date = x[0]

        year = int(info_get_date.split('.')[0])
        month = int(info_get_date.split('.')[1])
        day = int(info_get_date.split('.')[2])

        after_month = month + term
        while after_month > 12:
           year += 1
           after_month = after_month - 12

        after_day = day - 1
        while after_day == 0:
            after_month -= 1
            after_day = 28

        result_date = ''.join(map(str, [str(year),str(after_month).zfill(2),str(after_day).zfill(2)]))
        int_today = int(''.join(map(str,today.split('.'))))
        print("result_date: ",result_date, "int_today: ",int_today)

        if int(result_date) < int_today:
            answer.append(i+1)

    return answer