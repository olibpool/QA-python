mark = float(input('Gimmie an input of a mark yum yum: '))

if 65 < mark < 75:
    print('Pass')
elif 85 > mark >= 75:
    print('Merit')
elif mark >= 85:
    print('Distinction')
else:
    print('Fail')