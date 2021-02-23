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

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f'The restaurant is called {self.restaurant_name}, here is {self.cuisine_type} cuisine.')
#
#     def set_number_served(self, number):
#         if number >= self.number_served:
#             self.number_served = number
#         else:
#             print("You can't roll back a counter!")
#
#     def increment_number_served(self, count):
#         self.number_served += count
#
#     def open_restaurant(self):
#         print(f'{self.restaurant_name} is opened!')
#
#
# restaurant = Restaurant('Manhattan', 'european')
# restaurant.set_number_served(20)
# print(restaurant.number_served)
# restaurant.increment_number_served(3)
# print(restaurant.number_served)
#
# restaurant_2 = Restaurant('Churasko', 'mexican')
# restaurant_2.describe_restaurant()
#
# restaurant_3 = Restaurant('Forest', 'georgian')
# restaurant_3.describe_restaurant()
#
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['sweet', 'caramel', 'salt', 'raspberry']
#
#     def show_flavor(self):
#         print('Our flavours is: ')
#         for flavor in self.flavors:
#             print(flavor)


# icecream = IceCreamStand('Forest', 'georgian')
# print(icecream.show_flavor())

# class User:
#     def __init__(self, first_name, last_name, age, male):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.male = male
#         self.login_attempts = 0
#
#     def describe_user(self):
#         full_name = f'{self.first_name} {self.last_name}'
#         print(full_name.title())
#
#     def increment_login_attempts(self, count):
#         self.login_attempts += count
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#     def greet_user(self):
#         if self.male == 'male':
#             print('pipiska')
#         elif self.male == 'female':
#             print('hi, bitch')
#         else:
#             print('Choose correct')
#
#
# user1 = User('ann', 'halii', 19, 'female')
# user1.increment_login_attempts(1)
# user1.increment_login_attempts(1)
# user1.increment_login_attempts(1)
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)
#
#
# class Privileges:
#     def __init__(self):
#         self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]
#
#     def show_privileges(self):
#         print('Администратору разрешено:')
#         for i in self.privileges:
#             print(i)
#
#
# class Admin(User):
#     def __init__(self, first_name, last_name, age, male):
#         super().__init__(first_name, last_name, age, male)
#         self.privileges = Privileges()
#
#
# user2 = Admin('ann', 'halii', 19, 'female')
# print(user2.privileges.show_privileges())


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class Battery():
#     def __init__(self, battery_size=75):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#     def get_range(self):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#
#         print(f"This car can go about {range} miles on a full charge.")
#
#     def upgrade_battery(self, battery_size2):
#         if battery_size2 >= self.battery_size:
#             self.battery_size = battery_size2
#
#
#
# class ElectricCar(Car):
#
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank!")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery(100)
# my_tesla.battery.get_range()



from random import randint, choice

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(0, self.sides))


game = Die()


for i in range(0,10):
    game3.roll_die()


