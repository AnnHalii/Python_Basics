# age = 53
# if age <= 2:
#     print('младенец')
# elif 2 < age <= 4:
#     print('малыш')
# elif 4 < age <= 13:
#     print('ребенок')
# elif 13 < age <= 20:
#     print('подросток')
# elif 20 < age <= 65:
#     print('взрослый')
# else:
#     print('пожилой человек')
#
#
# fruits = ['banana']
# if fruits:
#     for fruit in fruits:
#         if fruit == 'cherry':
#             print('You really like cherry!')
#         elif fruit == 'banana':
#             print('You really like bananas!')
# else:
#     print('Error')
#
#
# names = ['anna', 'eugene', 'vitalii', 'admin', 'dima']
# if names:
#     for name in names:
#         if name == 'admin':
#             print(f'Hello {name.title()}, would you like to see a status report?')
#         else:
#             print(f'Hello {name.title()}, thank you for logging again!')
# else:
#     print('We need to ind some users')
#
#
# current_users = ['anna', 'eugene', 'suzie', 'marta', 'alex']
# new_users = ['irina', 'eugene', 'ANNA', 'anna', 'mary', 'john']
# upper_current_users = [i.upper() for i in current_users]
# for new_user in new_users:
#     if new_user.lower() in current_users or new_user.upper() in upper_current_users:
#         print(f'{new_user.title()}, смените имя, такое имя уже существует!')
#     else:
#         print(f'Имя {new_user.title()} доступно')
#
#
# numbers = list(range(1, 10))
# for number in numbers:
#     if number == 1:
#         print('1st')
#     elif number == 2:
#         print('2nd')
#     elif number == 3:
#         print('3rd')
#     else:
#         print(f'{number}th')
#
#
# human = {
#     'first_name': 'Ann',
#     'last_name': 'Halii',
#     'age': 19,
#     'city': 'Severodonetsk'
#     }
# print(human['first_name'])
# print(human['last_name'])
# print(human['age'])
# print(human['city'])
#
#
# favorite_number = {
#     'anna': 7,
#     'dima': 3,
#     'vitalii': 12,
#     'john': 5,
#     'mari': 2
#     }
# for name, number in favorite_number.items():
#     print(f"{name.title()}'s favorite number is {number}.")
#
#
# rivers_in_countries = {
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     'yangtze': 'china',
#     'mississippi': 'usa'
#     }
# for river, country in rivers_in_countries.items():
#     print(f"\nThe {river.title()} runs through {country.title()}.")
# for river in rivers_in_countries.keys():
#     print(f"{river.title()}")
# for country in rivers_in_countries.values():
#     print(f"\t{country.title()}")

# peoples = []
# anna = {
#     'name': 'ann',
#     'teach': 'python',
#     'city': 'severodonetsk',
#     'graduation': 'nure'
#     }
# ilia = {
#     'name': 'ilia',
#     'teach': 'c#',
#     'city': 'kharkiv',
#     'graduation': 'nure'
# }
# peoples.append(anna)
# peoples.append(ilia)
#
# for people in peoples:
#     print(people)

# pets = []
# timoshka = {
#     'master': 'ann',
#     'kind': 'cat'
# }
# zheltok = {
#     'master': 'olya',
#     'kind': 'ferret'
# }
# pets.append(timoshka)
# pets.append(zheltok)
#
# for pet in pets:
#     print(pet['master'], pet['kind'])


# favourite_places = {
#     'ann': ['centr', 'sargin yar', 'sushipapa'],
#     'ilia':  ['smog', 'centr'],
#     'eugene': ['smog', 'kfc']
#     }
# for name, places in favourite_places.items():
#     print(f"Любимое место: {name.title()}")
#     for place in places:
#         print(place)


# cities = {
#     'NY': {
#         'country': 'usa',
#         'population': '5 million',
#         'fact': 'coolest city ever'
#     },
#     'LA': {
#         'country': 'usa',
#         'population': '3 million',
#         'fact': 'there Hollywood'
#     }
# }
# for city_name, city_info in cities.items():
#     print(city_name)
#     print(f"Country: {city_info['country'].title()}")
#     print(f"Population: {city_info['population']}")
#     print(f"Fact: {city_info['fact'].title()}")

message = 'Choose pizza topping'
message += "\nFor exit choose 'quite'"

active = True
while active is True:
    choose = input(message)
    if choose == 'quite':
        active = False
    else:
        print(choose)
