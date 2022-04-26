'''
*args = arguments
**kwargs = key word arguments
'''
#inbuilt func
#my_sum = sum(1, 2, 3) #will throw error since args not a tuple
#print(my_sum)
my_sum = sum((1, 2, 3)) #will work
print(my_sum)

#sum function
def my_sum1(a, b, c):
    return a+b+c
print(my_sum1(1, 2, 3))
#print(my_sum1(1,2,3,4)) #wont work

#sum function with unlimited *args
def my_sum2(*args):
    return sum(args)
print(my_sum2(10,20,30,40,50,60))

#sum func using **kwargs
def kwargs_test(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.get('weight'))
    print(kwargs.get('address'))
kwargs_test(name='fucker', weight=165, age=33)