import os

print(os.getcwd())
# Change dir
os.chdir('/Users/pattabhimadhavaram/Desktop')

# Get current working directory
print(os.getcwd())

# list files
print(os.listdir())

print('--------------------------')
try:
    # create folder only if not present
    if 'my_folder' not in os.listdir():
        # make single dir
        # os.mkdir('my_folder')

        # Create multiple dirs
        os.makedirs('my_folder/sub_folder/ding-dong')

    # remove dirs
    # os.rmdir('my_folder/sub_folder/ding-dong')
    os.removedirs('my_folder/sub_folder/ding-dong')
    print('Folders created')
except IOError as e:
    print('Error details are:\n'
          '\t'.format(e.strerr))
except FileNotFoundError as e:
    print('File not found')
# except as e:
#     print('Some error occurred')
#     print(dir(e))
finally:
    print('Dengu')

# Creating a file in sub_folder
with open('/Users/pattabhimadhavaram/Desktop/my_folder/sub_folder/my_file.txt', mode='w') as my_file:
    pass

#
os.remove('/Users/pattabhimadhavaram/Desktop/my_folder/sub_folder/my_file.txt')
os.rename('my_file.txt', 'renamed.txt')

