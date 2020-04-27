# Alcohol Tracker App v0.6

from datetime import datetime, timedelta

# Declare all drinks
all_drinks = [
    ('#', 0),
    ('beer', 0.07),
    ('wine', 0.12),
    ('vodka', 0.4)
]

all_genders = [
    ('male', 0.7),
    ('female', 0.6)
]

my_ethanol = []
my_drinks = []
my_volume = []


def alco_tracker():
    global my_ethanol, my_drinks
    print('Welcome to Alco Tracker v0.6')
    weight = float(input('Your weight (kg): '))
    gender = input('Specify your gender: ')
    if gender == 'male':
        weight *= all_genders[0][1]
    elif gender == 'female':
        weight *= all_genders[1][1]

    while True:
        drink = int(input(f'Choose your drink:\n'
                          f'1. {all_drinks[1][0]}\n'
                          f'2. {all_drinks[2][0]}\n'
                          f'3. {all_drinks[3][0]} '))
        volume = int(input('How much you drunk (ml)? '))
        my_drinks.append((all_drinks[drink][0], volume))
        my_ethanol.append(all_drinks[drink][1] * volume)
        my_volume.append(volume)

        add_drink = input('Anything else? (y/n) ')

        if add_drink.lower() == 'n':
            break

        if add_drink.lower() == 'y':
            print('Please add another drink\n')
            continue

    print('-' * 40)
    print('You drunk:')
    print('-' * 40)
    num_of_drinks = 0
    for drink in my_drinks:
        num_of_drinks += 1
        print(f'{num_of_drinks}. {drink[0]}, {drink[1]} ml')
    print('-' * 40)

    sober_time = sum(my_ethanol) / weight * 300
    sober_time_hours = sober_time // 60
    sober_time_minutes = sober_time % 60
    sober_time_to_drive = datetime.now() + timedelta(hours=sober_time_hours)

    message = (
        f'Total amount of alcohol = {sum(my_volume)} ml\n'
        f'(including {sum(my_ethanol)} ml of clear ethanol)\n'
        f'Your Blood Alcohol Index is {(sum(my_ethanol) / weight):.2f}‰\n'
        f'You can drive in {int(sober_time_hours)} h {int(sober_time_minutes)} min on '
        f'{sober_time_to_drive:%d %b %H:%M}'
    )

    print(message)


alco_tracker()
