import math


def seasons(month):
    if month in {1,2,12}:
        return 'Зима'
    if month in {3,4,5}:
        return 'Весна'
    if month in {6,7,8}:
        return 'Лето'
    if month in {9,10,11}:
        return 'Осень'
    return 'Неправильно введён месяц!'

month_num = int(input('Введите месяц:'))
print(seasons(month_num))


def converter(string, delimter):
    string = string.split(delimter)
    counter = {}
    for word in string:
        counter[word] = string.count(word)
    return counter


string = input('Введите свои слова:')
delimter = input('Введите свои слова:')

print(converter(string, delimter))


def get_rectangle_data():
    a = int(input('Введите сторону квадрата:'))
    return 4*a, a**2, math.sqrt(2)*a


print(get_rectangle_data())
