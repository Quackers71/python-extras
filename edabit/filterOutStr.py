def filter_list(lst):
    for n in lst:
        if isinstance(n, int) and n > 0:
            return n
