# Constants for Bedtime
MIN_CURRENT_TIME = 2000
MAX_HOMEWORK_DUE = 0

current_time = int(input('Enter the current time: '))
homework_due = int(input('Enter how many uncompleted homework assignments are due tomorrow: ')) 

if current_time >= MIN_CURRENT_TIME and homework_due <= MAX_HOMEWORK_DUE:
    print("Great job! It's time for bed.")
else:
# Multi-line with f-string
    print(f'''
Sorry, in order to go to bed it needs to be:

- late enough, at least {MIN_CURRENT_TIME}
- the amount of uncompleted homework assignments is: {MAX_HOMEWORK_DUE}
''')