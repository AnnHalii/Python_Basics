import math


def seasons():
    month = int(input('Введите месяц:'))
    if month in {1,2,12}:
        return 'Зима'
    if month == 3 or month == 4 or month == 5:
        return 'Весна'
    if month == 6 or month == 7 or month == 8:
        return 'Лето'
    if month == 9 or month == 10 or month == 11:
        return 'Осень'
    else:
        return 'Неправильно введён месяц!'


print(seasons())


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
