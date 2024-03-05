def solution(wallpaper):
    top, bottom = 0, 0
    left, right = 51, 0

    # top 찾기
    for index, w in enumerate(wallpaper):
        if '#' in w:
            top = index
            break

    # left, right 찾기
    for index, w in enumerate(wallpaper):
        # bottom 찾기
        if '#' in w:
            bottom = index + 1
        #left, right    
        for i, char in enumerate(w):
            if char == '#' and left >= i:
                left = i
            if char == '#' and right <= i:
                right = i + 1
    
    return [top, left, bottom, right]