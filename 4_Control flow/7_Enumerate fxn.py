# ENUMERATE function
# def: adding numbering to list of items in Lists, Dictionaries, Tuples
# End result is a tuple
curse_words = ['donga', 'puku', 'fellow', 'faltu', 'munda']

for word in enumerate(curse_words):
    print(word)

for word in enumerate(curse_words, 100):  # This starts numbering at the 2nd param
    print(word)