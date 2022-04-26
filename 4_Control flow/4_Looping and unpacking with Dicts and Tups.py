emp_earnings = {'john': 40000, 'pat': 105000, 'DP': 70000}

for entry in emp_earnings:
    print(entry)

# unpacking dictionaries
for (key, value) in emp_earnings.items():
    print(key)
    print(value)

# unpacking LIST
peo_dtls = [('Nithin', 130, 33), ('pat', 105, 33), ('DP', 70, 30)]
print('\n')
for (name, sal, age) in peo_dtls:
    print('\nPerson details:\nName: ' + name + '\nSalary: ' + str(sal) + '\nAge: ' + str(age))
