# Sample FOR loop
animals = ['dog', 'cat', 'horse', 'piggu']
cnt = 0
for x in animals:
    cnt = cnt + 1
    print('animal ' + str(cnt) + ' = ' + x)
print('End of code!')

# For loop
# BREAK and CONTINUE keywords
cnt = 0
for animal in animals:
    cnt = cnt + 1
    print('Animal ' + str(cnt))
    if animal == 'dog':
        print('Loki is a ' + animal)
    elif animal == 'piggu':
        continue
    elif animal == 'cow':
        break
    else:
        print("I don't have a " + animal)
print('Done!')

# FOR loops
# PASS keyword - Placeholder for later code; Python cant interpret an empty loop
for x in animals:
    pass
