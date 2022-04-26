# ZIP fxn

my_nums = [1, 2, 3, 4]
curse_words = ['donga', 'puku', 'sale', 'faltu', 'muddi']

combined_Items = zip(my_nums, curse_words)

print(combined_Items)  # will only give address in storage

for item in combined_Items:  # will print tuple lists
    print(item)