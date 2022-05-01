original_item = {1: 'pat', 2: 'dp', 3: 'loki', 4: 'guest 1', 5: 'guest 2'}

cntr = 0
new_dict = {}

for (k, v) in original_item.items():
    cntr += 1
    print('itrn# = {0} ; Key = {1} ; Dict item = {2}'.format(cntr, k, v))
    if cntr <= 3:
        new_dict[k] = v
    else:
        break
