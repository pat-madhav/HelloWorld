# ------------------------------------------------------------------
my_file = open('/Users/pattabhimadhavaram/Downloads/sample.txt')

file_content = my_file.read()
file_data = my_file.read()
print('File content : \n{0}'.format(file_content))
print('-------------------------')
print('File data : \n{0}'.format(file_data))
'''
file_data won't print anything
since cursor is at the end after the file is read first time into file_content variable
we need to reset cursor as followa
'''
my_file.seek(0)
file_data = my_file.read()
print('-------------------------')
print('File data : \n{0}'.format(file_data))

# ------------------------------------------------------------------
# read lines separately
my_file.seek(0)
file_content_list = my_file.readlines()
print('-------------------------')
print('File data line list : \n{0}'.format(file_content_list))
# always close opened resource
my_file.close()

# ------------------------------------------------------------------
# Succinct way of reading file
# with _______ as  - automatically closes file
with open('/Users/pattabhimadhavaram/Downloads/sample.txt') as my_file1:
    new_content = my_file1.read()
print('-------------------------')
print('new_content : \n{0}'.format(new_content))

# ------------------------------------------------------------------
# file read modes
# append
with open('/Users/pattabhimadhavaram/Downloads/sample.txt', mode='a') as my_file2:
    my_file2.write('\nLine added from PyScript')
appended_file = open('/Users/pattabhimadhavaram/Downloads/sample.txt')
print('-------------------------')
print('Appended file : \n{0}'.format(appended_file.read()))
appended_file.close()

# ------------------------------------------------------------------
# file read modes
# write - overwrites file
with open('/Users/pattabhimadhavaram/Downloads/sample1.txt', mode='w') as my_file2:
    my_file2.write('\nLine added from PyScript')
overWritten_file = open('/Users/pattabhimadhavaram/Downloads/sample1.txt')
print('-------------------------')
print('OverWritten file : \n{0}'.format(overWritten_file.read()))
overWritten_file.close()

# ------------------------------------------------------------------
# file read modes
# write - creates new file; by giving a file name that doesnt exist
with open('/Users/pattabhimadhavaram/Downloads/sample2.txt', mode='w') as my_file2:
    my_file2.write('\nCreating new file')
created_file = open('/Users/pattabhimadhavaram/Downloads/sample2.txt')
print('-------------------------')
print('Created file : \n{0}'.format(created_file.read()))
created_file.close()

# ------------------------------------------------------------------
# file read modes
# read and write - "r+" : in place update from beginning and leaves rest of content as is
with open('/Users/pattabhimadhavaram/Downloads/sample2.txt', mode='r+') as x:
    x.write('Fuck!')
    x.seek(0)
    temp_read = x.read()
print('-------------------------')
print('ReadWritten file : \n{0}'.format(temp_read))

# ------------------------------------------------------------------
# file read modes
# (Create new file/overwrite) and read - "w+" : in place update from beginning and leaves rest of content as is
with open('/Users/pattabhimadhavaram/Downloads/sample3.txt', mode='w+') as x:
    x.write('Create and read')
    x.seek(0)
    temp_read2 = x.read()
print('-------------------------')
print('Create read file : \n{0}'.format(temp_read2))
