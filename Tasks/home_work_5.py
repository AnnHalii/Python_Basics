# import math
#
#
# def seasons(month):
#     if month in {1,2,12}:
#         return 'Зима'
#     if month in {3,4,5}:
#         return 'Весна'
#     if month in {6,7,8}:
#         return 'Лето'
#     if month in {9,10,11}:
#         return 'Осень'
#     return 'Неправильно введён месяц!'
#
#
# month_num = int(input('Введите месяц:'))
# print(seasons(month_num))
#
#
# def converter(string, delimter):
#     string = string.split(delimter)
#     counter = {}
#     for word in string:
#         counter[word] = string.count(word)
#     return counter
#
#
# string = input('Введите свои слова:')
# delimter = input('Введите свои слова:')
#
#
# print(converter(string, delimter))
#
#
# def get_rectangle_data():
#     a = int(input('Введите сторону квадрата:'))
#     return 4*a, a**2, math.sqrt(2)*a
#
#
# print(get_rectangle_data())

# message = 'Choose pizza topping'
# message += "\nFor exit choose 'quit'"
# active = True
# while active is True:
#     choose = input(message)
#     if choose == 'quit':
#         active = False
#     else:
#         print(choose)

# age = int(input('Enter your age to find out the price:'))
# active = True
# while active:
#     if age < 3:
#         print('Free')
#     elif 4 <= age <= 12:
#         print('10$')
#     elif age >= 13:
#         print('15$')
#     choose = input("For exit choose 'quit'")
#     if choose == 'quite':
#         active = False
#         break


# sandwich_orders = ['tuna', 'scrambler', 'avocado', 'marmalade']
# finished_sandwiches = []
# for sandwich in sandwich_orders:
#     print(f'I made your {sandwich} sandwich.')
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(current_sandwich)
# for finished in finished_sandwiches:
#     print(f'Your {finished} sandwich is ready!')
#
#
# sandwich_orders = ['pastrami', 'tuna', 'scrambler', 'pastrami', 'avocado', 'marmalade', 'pastrami']
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)
#
# responses = {}
# start = True
# while start:
#     name = input('Please enter your name to participate in the survey:')
#     answer = input('Where would you like to spend your vacation?')
#
#     responses[name] = answer
#
#     repeat = input('Would you like to let another person response?[yes/no]')
#     if repeat == 'no':
#         start = False
# for name, answer in responses.items():
#     print(f'{name.title()} wants to spend vacation in {answer.title()}')
#
#
# def display_message():
#     print('Hello, my name is Ann!')
#
#
# display_message()
#
#
# def favourite_book(title):
#     print(f'One of my favourite books is {title}')
#
#
# favourite_book('Roadside Picnic')
#
#
# def make_shirt(size = 'L', text = 'I love python'):
#     print(f'Size this shirt is {size}')
#     print(f'Print is {text}')
#
#
# make_shirt()
#
#
# def describe_city(city, country='ukraine'):
#     print(f'{city.title()} is in {country.title()}')
#
#
# describe_city('kyiv')
# describe_city('severodonetsk')
#
#
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
#
# people = get_formatted_name('ann',  'halii')
# print(people)
#
#
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f'The restaurant is called {self.restaurant_name}, here is {self.cuisine_type} cuisine.')
#
#     def open_restaurant(self):
#         print(f'{self.restaurant_name} is opened!')
#
#
# restaurant = Restaurant('Manhattan', 'european')
# restaurant.describe_restaurant()
#
# restaurant_2 = Restaurant('Churasko', 'mexican')
# restaurant_2.describe_restaurant()
#
# restaurant_3 = Restaurant('Forest', 'georgian')
# restaurant_3.describe_restaurant()
#
#
# class User:
#     def __init__(self, first_name, last_name, age, male):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.male = male
#
#     def describe_user(self):
#         full_name = f'{self.first_name} {self.last_name}'
#         print(full_name.title())
#
#     def greet_user(self):
#         if self.male == 'male':
#             print('piska')
#         elif self.male == 'female':
#             print('Hi, bitch')
#         else:
#             print('Choose correct')
#
#
# user1 = User('ann', 'halii', 19, 'female')
# user1.describe_user()
# user1.greet_user()





# games = ['tennis', 'computer']
# foods = ['pivo', 'fish', 'hinkali']
# favorites = games + foods
# print(favorites)
#
# builds = 3
# ninja = 25
# tunel = 2
# samurai = 40
# all = builds*ninja+tunel*samurai
# print(all)
#
# f_name = 'Ann'
# l_name = 'Halii'
# print("Hello, %s" % f_name, "%s" % l_name)


# import turtle as t
# square
# t = turtle.Pen()
#
# t.forward(70)
# t.up()
# t.forward(30)
# t.down()
# t.left(90)
# t.forward(70)
# t.up()
# t.forward(30)
# t.down()
# t.left(90)
# t.forward(70)
# t.up()
# t.forward(30)
# t.down()
# t.left(90)
# t.forward(70)
# t.up()
# t.forward(30)
# t.down()
# t.left(90)

# triangle
# t = turtle.Pen()
#
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

# rectangle

# t = turtle.Pen()
# t.forward(200)
# t.left(90)
# t.forward(70)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(70)

# money = 2000
# if money > 1000:
#     print('Я багатий!')
# else:
#     print("Я не багатий!")
#     print("Може, коли-небудь потім …")
#
#
# twinkies = 200
# if 100 <= twinkies <= 500:
#     print('Занадто мало або занадто багато')
# else:
#     print('Не відповідає')
#
#
# money = 400
# if 100 <= money <= 500:
#     print('Відповідає')
# elif 1000 <= money <= 5000:
#     print('Відповідає')
# else:
#     print('Не відповідає')
#
#
# ninjas = 60
# if ninjas <= 10:
#     print('Я переможу цих ніндзя!')
# elif ninjas <= 30:
#     print('Буде непросто, але я з ними розправлюсь')
# elif 31 <= ninjas <= 50:
#     print('Їх дуже багато')
# else:
#     print('Їх занадто багато')
#
#
# for i in range(1, 20, 2):
#     print(i)
#
#
# ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes']
# for i, ingredient in enumerate(ingredients):
#     print(f'{i+1}. {ingredient.title()}')


