import random


def input_player():
    player_select = input('Enter the number:')
    return player_select


def validate_input_player(string):
    if string.isdigit():
        return int(string)


def rand_number():
    random_number = random.randint(1, 1000)
    return random_number


def compare_values(gen, inp):
    if inp < gen:
        return 'Your number is less'
    if inp > gen:
        return 'Your number is greater'
    if inp == gen:
        return 'You win!'


def start_game():
    start = True
    while start is True:
        rnd = rand_number()
        for i in range(10):
            print(f'You have {10-i} attempts')
            select = validate_input_player(input_player())
            if select is None:
                print("Error: Please enter the correct character!")
                start = False
                break
            print(str(compare_values(rnd, select)))
            if select == 'You win!':
                break


start_game()

