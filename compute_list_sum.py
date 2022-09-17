def compute_list_sum(l: list):
    for item in l:
        if not item.isnummeric():
            raise TypeError("Item must be numeric")
    return sum(l)
    