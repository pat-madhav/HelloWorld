"""
We've created code to shorten any of the following to a given length

Items may consist of:
> Dictionaries
> Lists
> Strings

# Code location
Directory =             PythonPractice/utils/
File =                  utils_stuff.py
Classes to shorten =    ListAndCharShortener
                        DictShortener

Import classes and use
"""

from utils.utility_stuff import ListAndCharShortener, DictShortener


print('----------------------')
my_dict = {1: 'pat', 2: 'dp', 3: 'loki', 4: 'guest 1', 5: 'guest 2'}
new_shortener = DictShortener(my_dict, 1)
new_shortener.print_original_item()
new_shortener.print_shortened_item()