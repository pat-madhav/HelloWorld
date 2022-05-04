import re

txt = 'fucking fuck, Python is amazing'

result = re.search('is', txt)
print(result)

# --------------------------------------
# search if the "statement" starts with 'fuck' and ends with 'ing'
x = re.search("^fuck.*ing$", txt)  # boolean method
if (x):
    print("Yes!, it's a match")
else:
    print('No match...!')

# --------------------------------------
# find all positions where 'is' occurs in a "sentance"
txt = 'easter wester is a gister fucking is is is fuck is'
y = re.findall('is', txt)
print(y)
