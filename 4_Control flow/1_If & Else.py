# if - elif - else
def compare_nums(x, y):
    if x < y:
        print('{0} < {1}'.format(x, y))
    elif x > y:
        print('{0} > {1}'.format(x, y))
    elif x == y:
        print('{0} = {1}'.format(x, y))
    else:
        print('This is fucked up shit!')

# Running func
compare_nums(10, 20)
compare_nums(40, int('10'))
compare_nums(40, 4)
compare_nums(1, int(True))
compare_nums(0, int(False))

# Another example - unreachable code
if False:
    # This code isn't reachable, hover mouse on highlight
    print('it''ll always come here')
else:
    print('this will never print')