# This lesson teaches the importance of ordering your elif statements.

age =101
if age < 4:    # Be sure you include the colon
    print('Admission is $0')
elif age < 18:
    print('Admission is $25')
elif age > 100:
    print('Admission is $0 and you get a free beer!')
else:
    print('Admission is $40')

#Here is doesn't work because the order is messed up
    age =101
if age < 4:    
    print('Admission is $0')
elif age < 18:
    print('Admission is $25')
elif age > 60:
    print('Admission is $35')
elif age > 100:
    print('Admission is $0 and you get a free beer!')
else:
    print('Admission is $40')