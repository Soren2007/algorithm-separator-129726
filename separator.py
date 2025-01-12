def separator(ls):
    odd = []
    even = []
    for number in ls:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd
