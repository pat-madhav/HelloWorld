"""
---------------------------------------
Creating a utility to shorten items to 3 elements
    ITEMS can include
    > Dictionaries
    > Lists
    > String
---------------------------------------
Parent Class =  Shortener()
Sub-Classes =   ListAndCharShortener()
                DictShortener()
---------------------------------------
Usage
var1 = ListAndCharShortener(ListOrString)
var1.print_original_item()
var1.print_shortened_item()
---------------------------------------
"""

class Shortener:
    def __init__(self, item, short_item_len):
        self.original_item = item
        self.short_item_len = short_item_len

    def print_original_item(self):
        print(self.original_item)


class ListAndCharShortener(Shortener):
    def print_shortened_item(self):
        print(self.original_item[0:self.short_item_len])


class DictShortener(Shortener):
    def print_shortened_item(self):
        # original_item = {1: 'pat', 2: 'dp', 3: 'loki', 4: 'guest 1', 5: 'guest 2'}
        dict = self.original_item
        cntr = 0
        new_dict = {}
        for (k, v) in dict.items():
            cntr += 1
            if cntr <= self.short_item_len:
                new_dict.update({k: v})
            else:
                break
        print(new_dict)

'''
print('----------------------')
my_shortener = ListAndCharShortener([10, 20, 30, 40, 50], 2)
my_shortener.print_original_item()
my_shortener.print_shortened_item()

print('----------------------')
my_shortener = ListAndCharShortener('Fuck! all the shit', 5)
my_shortener.print_original_item()
my_shortener.print_shortened_item()

print('----------------------')
my_dict = {1: 'pat', 2: 'dp', 3: 'loki', 4: 'guest 1', 5: 'guest 2'}
new_shortener = DictShortener(my_dict, 1)
new_shortener.print_original_item()
new_shortener.print_shortened_item()
'''