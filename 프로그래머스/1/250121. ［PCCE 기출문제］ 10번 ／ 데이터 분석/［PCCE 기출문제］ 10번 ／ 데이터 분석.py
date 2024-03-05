def solution(data, ext, val_ext, sort_by):    
    index = 0
    if ext == "code":
        index = 0
    elif ext == "date":
        index = 1
    elif ext == "maximum":
        index = 2
    elif ext == "remain":
        index = 3
    
    sort_index = 0
    if sort_by == "code":
        sort_index = 0
    elif sort_by == "date":
        sort_index = 1
    elif sort_by == "maximum":
        sort_index = 2
    elif sort_by == "remain":
        sort_index = 3

    filter = [d for d in data if d[index] < val_ext]

    return sorted(filter, key = lambda x: x[sort_index])