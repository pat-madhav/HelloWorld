#my_list = ['tesla', 'apple', 'lulu', 'melin']
x = 0
while x < 10:
    if x == 6:
        continue
    print(str(x) + ' < 10')
    x += 3
else:
    print('broken code')