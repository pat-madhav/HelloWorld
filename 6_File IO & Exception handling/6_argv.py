import sys

# argv[0] = path by default
print(sys.argv[0])

# passed arguments start from 1,2,...
print(sys.argv[1])
# this script needs to be invoked from terminal by passing an argument

# this code prints all arguments passed to the PyScript
arg_list = sys.argv[1:]
cntr = 0
for arg in arg_list:
    cntr += 1
    print(arg)

