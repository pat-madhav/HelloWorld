def sum(num1, num2):
    try:
        print(num1 + num2)
    except:
        print("There was an error!")

number1 = input('Enter a number : ')
# input() takes everything as a string
# this throws a type error

sum(number1, 12)

# -----------------------------------
def good_sum(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        print(num1 + num2)
    else:
        print('Datatype was not a number for parameters')
