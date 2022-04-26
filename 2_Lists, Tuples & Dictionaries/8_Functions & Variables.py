#Basic dunction defination
def greet_person():
    '''
    This is a fucking amazing way to comment
    :return: NULL
    '''
    print("Suck it...!")
greet_person()

#Function defination - passing arguments
def faggot(x1):
    print('Fuck off ' + str(x1) + '!')
faggot('pichi')

#Function def - Default value for Arguments
def function_1(x2='fucker'):
    print(x2 + ' is an asshole')
function_1()
function_1('test')

#Function def - Returning a value
def function_2():
    return 'returned fuck!'
returned_str = function_2()
print(returned_str)

#assignment function
def return_remainder(v1=1,v2=1):
    '''
    :param v1: Number to be divided
    :param v2: Number to divide
    :return: Returns reminder
    '''
    return v1 % v2
print(return_remainder(15,6))