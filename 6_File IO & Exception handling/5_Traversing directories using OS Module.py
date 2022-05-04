import os

for dir_path, sub_dir_names, sub_file_names in os.walk("/Users/pattabhimadhavaram/Desktop/my_folder"):
    # print('dir_path = {0}\n'
    #       'dir_name = {1}\n'
    #       'file_path = {2}'.format(dir_path, sub_dir_names, sub_file_names))
    # print('----------------------------')
    pass

# get home directory of local OS
print(os.environ.get('HOME'))

# add slashes
print(os.path.join(os.environ.get('HOME'), 'my_file.txt'))

# removes path and gets last object name
print(os.path.basename('/Users/pattabhimadhavaram/my_file.txt'))

# gets just path and removes last object name
print(os.path.dirname('/Users/pattabhimadhavaram/my_file.txt'))

# returns dir and object as a tuple
print(os.path.split('/Users/pattabhimadhavaram/my_file.txt'))

# check if path exists on a computer
# bool  function
print(os.path.exists('/Users/pattabhimadhavaram/my_file.txt'))

# check if file exists in a path
# bool function
print(os.path.isfile('/Users/pattabhimadhavaram/my_file.txt'))

# check if file exists in a path
# bool function
print(os.path.isdir('/Users/pattabhimadhavaram/my_file.txt'))

# gets file extension and dir+obj name as a tuple
print(os.path.splitext('/Users/pattabhimadhavaram/my_file.txt'))
