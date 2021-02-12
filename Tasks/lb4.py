#  1
money = 2000
if money > 1000:
    print('Я багатий!')
else:
    print("Я не багатий!")
    print("Може, коли-небудь потім …")

# 2
twinkies = 200
if 100 <= twinkies <= 500:
    print('Занадто мало або занадто багато')
else:
    print('Не відповідає')

# 3
money = 400
if 100 <= money <= 500:
    print('Відповідає')
elif 1000 <= money <= 5000:
    print('Відповідає')
else:
    print('Не відповідає')

# 4
ninjas = 60
if ninjas <= 10:
    print('Я переможу цих ніндзя!')
elif ninjas <= 30:
    print('Буде непросто, але я з ними розправлюсь')
elif 31 <= ninjas <= 50:
    print('Їх дуже багато')
else:
    print('Їх занадто багато')