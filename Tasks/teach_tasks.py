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
new_users = ['irina', 'eugene', 'anna', 'mary', 'john']
for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user.title()}, смените имя, такое имя уже существует!')
    else:
        print(f'Имя {new_user.title()} доступно')