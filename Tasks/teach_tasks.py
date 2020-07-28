age = 53
if age <= 2:
    print('младенец')
elif 2 < age <= 4:
    print('малыш')
elif 4 < age <= 13:
    print('ребенок')
elif 13 < age <= 20:
    print('подросток')
elif 20 < age <= 65:
    print('взрослый')
else:
    print('пожилой человек')


fruits = ['banana']
if fruits:
    for fruit in fruits:
        if fruit == 'cherry':
            print('You really like cherry!')
        elif fruit == 'banana':
            print('You really like bananas!')
else:
    print('Error')


names = ['anna', 'eugene', 'vitalii', 'admin', 'dima']
if names:
    for name in names:
        if name == 'admin':
            print(f'Hello {name.title()}, would you like to see a status report?')
        else:
            print(f'Hello {name.title()}, thank you for logging again!')
else:
    print('We need to ind some users')


current_users = ['anna', 'eugene', 'suzie', 'marta', 'alex']
new_users = ['irina', 'eugene', 'ANNA', 'anna', 'mary', 'john']
upper_current_users = [i.upper() for i in current_users]
for new_user in new_users:
    if new_user.lower() in current_users or new_user.upper() in upper_current_users:
        print(f'{new_user.title()}, смените имя, такое имя уже существует!')
    else:
        print(f'Имя {new_user.title()} доступно')


numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')


human = {
    'first_name': 'Ann',
    'last_name': 'Halii',
    'age': 19,
    'city': 'Severodonetsk'
    }
print(human['first_name'])
print(human['last_name'])
print(human['age'])
print(human['city'])


favorite_number = {
    'anna': 7,
    'dima': 3,
    'vitalii': 12,
    'john': 5,
    'mari': 2
    }
for name, number in favorite_number.items():
    print(f"{name.title()}'s favorite number is {number}.")



