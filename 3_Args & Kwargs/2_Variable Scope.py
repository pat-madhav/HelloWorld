#scope = ?

age = 27   #'''#GLOBAL scope'''
print(age)

def increase_age():
    age = 30 #'''#FUNC level LOCAL scope'''
print(age)

increase_age()
print(age)

#scope in nested funcs
def increase_age():
    age = 30 #'''#FUNC level LOCAL scope'''
    #defining NESTED function
    def add_4_to_age(age):
        age = age + 4 #'''#NESTED FUNC level LOCAL scope'''
        print('Nested method age: ' + str(age))
    #calling the nested function
    #nested functions can't be accessed GLOBALLY
    add_4_to_age(100)
    add_4_to_age(age)
    print('method age: ' + str(age))

increase_age()