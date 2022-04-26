my_dict = {'k1':'some data'}
extracted = my_dict['k1']
print(extracted)

#Dictionaries - Slicing using indexes
my_dict = {'k1':'some data', '7':'other data'}
extracted = my_dict['7']
print(extracted)

#Dictionaries - MUTABLE
my_dict = {'k1':'some data', '7':'other data'}
my_dict['7'] = "NEW VALUE"
print(my_dict)

people_weight_dict = {'john':250, 'pattu':160, 'DP':120}
print(people_weight_dict['pattu'])
people_weight_dict['pattu'] = 150
print(people_weight_dict['pattu'])

#append values to dictionaries
people_weight_dict['99'] = 'fuck'
print(people_weight_dict)

#complex_dict
complex_dict = {'1': "First Value", 'mike':'fag',
                'my_list':[1, {'k1':'1st val', 'k2':'2nd val'}],
                'my_tup':(1, 2, 3)}
print(complex_dict['my_list'][1]['k2'])