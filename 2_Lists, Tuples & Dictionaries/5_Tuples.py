my_tuple = (1, 2, 3, "Some data", [1, 2, 3])

print(my_tuple[4])

#Tuples are IMMUTABLE
# my_tuple[3] = "Other data"

#Lists indide of a Tuple are MUTABLE
my_tuple[4][0] = "New value"

print(my_tuple[4])