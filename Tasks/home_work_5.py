import math


def seasons():
    month = int(input('Введите месяц:'))
    if month == 12 or month == 1 or month == 2:
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


def converter():
    string = input('Введите свои слова:')
    string = string.split()
    counter = {}
    for word in string:
        counter[word] = counter.get(word, 0)+1
    doubles = {element: count for element, count in counter.items() if count >= 1}
    return doubles


print(converter())


def get_rectangle_data():
    a = int(input('Введите сторону квадрата:'))
    return 4*a, a**2, math.sqrt(2)*a


print(get_rectangle_data())