import re

def solution(new_id):
    # 1단계
    level_one = new_id.lower()

    # 2단계
    p = re.compile("[a-zA-Z0-9-_.]")
    level_two =  ''.join(re.findall(p, level_one))

    # 3단계
    level_three = ""
    dot_count = 0
    for char in level_two:
        if char == '.':
            dot_count += 1
            if dot_count > 1:
                char = ''
                dot_count -= 1
            else:
                level_three += char
        else:
            level_three += char
            dot_count = 0

    # 4단계
    level_three = list(level_three)
    if level_three[0] == '.':
        level_three[0] = ''
    if level_three[-1] == '.':
        level_three[-1] = ''
    level_four = ''.join(level_three)

    # 5단계
    if len(level_four) == 0:
        level_five = "a"
    else:
        level_five = level_four

    # 6단계
    if len(level_five) > 15:
        level_six = level_five[:15]
        if level_six[-1] == ".":
           level_six = level_six[:-1]
    else:
        level_six = level_five
    
    # 7단계
    level_seven = ""
    if len(level_six) < 3:
        level_seven = level_six
        while len(level_seven) < 3:
            level_seven += level_six[-1]
    else:
        level_seven = level_six

    return level_seven