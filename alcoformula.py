# usr/bin/python3
# Alcohol Tracker App v0.7

from datetime import datetime, timedelta

all_drinks = [
    ('#', 0),
    ('beer', 0.07),
    ('wine', 0.12),
    ('vodka', 0.4)
]

all_genders = {
    'male': 0.7,
    'female': 0.6
}

my_drinks, my_ethanol, my_volume = [], [], []
gender_weight = 0


def ask(data):
    return input(f'Enter your {data}: ')


def calculate_gender_weight(gender_result, weight_result):
    if gender_result == 'male':
        return float(weight_result) * all_genders['male']
    elif gender_result == 'female':
        return float(weight_result) * all_genders['female']


def sober(ethanol_list, volume_list, gender_weight_result):
    sober_time = sum(ethanol_list) / float(gender_weight_result) * 300
    sober_time_hours = sober_time // 60
    sober_time_minutes = sober_time % 60
    sober_time_to_drive = datetime.now() + timedelta(hours=sober_time_hours)
    message = (
        f'Total amount of alcohol = {sum(volume_list)} ml\n'
        f'(including {sum(ethanol_list)} ml of clear ethanol)\n'
        f'Your Blood Alcohol Index is {(sum(ethanol_list) / gender_weight_result):.2f}‰\n'
        f'You can drive in {int(sober_time_hours)} h {int(sober_time_minutes)} min on '
        f'{sober_time_to_drive:%d %b %H:%M}'
    )
    print(message)


def separator():
    print('-' * 40)


def ask_drink():
    while True:
        drink = int(input(f'Choose your drink:\n'
                          f'1. {all_drinks[1][0]}\n'
                          f'2. {all_drinks[2][0]}\n'
                          f'3. {all_drinks[3][0]} '))
        volume = ask('volume (ml)')
        my_drinks.append((all_drinks[drink][0], volume))
        my_ethanol.append(all_drinks[drink][1] * float(volume))
        my_volume.append(float(volume))

        add_drink = input('Anything else? (y/n) ')

        if add_drink.lower() == 'y':
            print('Please add another drink\n')
            continue
        elif add_drink.lower() == 'n':
            result_drinks(my_drinks)
            break


def result_drinks(drinks_list):
    separator()
    print('You drunk:')
    separator()
    num_of_drinks = 0
    for drink in drinks_list:
        num_of_drinks += 1
        print(f'{num_of_drinks}. {drink[0]}, {drink[1]} ml')
    separator()
    sober(my_ethanol, my_volume, gender_weight)


def alcohol_tracker():
    global my_volume, my_ethanol, my_drinks, gender_weight
    while True:
        weight = float(input('Enter your weight: '))
        if weight > 200 or weight < 20:
            print('Weight must be from 20 kg to 200 kg')
            continue
        else:
            break

    while True:
        gender = str(input('Enter your gender: '))
        if gender == 'male' or gender == 'female':
            break
        else:
            print('Specify you gender')

    gender_weight = calculate_gender_weight(gender, weight)
    ask_drink()


print('Welcome to Alcohol Tracker v0.7')
alcohol_tracker()
