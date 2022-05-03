# ----------------------------------------------------------
# trying to open a file that doesn't exist
try:
    with open('/Users/pattabhimadhavaram/Downloads/sample3.txt', mode='r') as my_file:
        print(my_file.read())
        x = 2 + '2'
except FileNotFoundError:
    print("File doesn't exist! : FileNotFoundError")
except TypeError:
    print('Type error you idiot')
except:
    print('Logging unknown error...')
finally:
    print('This code runs no-matter what')

print('Code executed successfully...!')
