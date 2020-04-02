# Alcohol Tracker App v0.5

from datetime import datetime, timedelta

# Declare all drinks
all_drinks = {
    'beer': 0.07,
    'wine': 0.12,
    'vodka': 0.4
}

all_genders = {
    'male': 0.7,
    'female': 0.6
}

# Declare all others
ethanol = []
num_of_drinks = 0
my_drinks = {}
my_gender = {}

# Questions for user
q_gender = input('Specify your gender: ')
q_weight = int(input('Your weight (kg): '))
my_gender[q_gender] = q_weight

for key, value in my_gender.items():
    gendercoef = my_gender[key] * all_genders[key]

while True:
    q_drink = input('Your drink: ')
    q_volume = int(input('How much you drunk (ml)? '))
    q_else = input('Anything else? (y/n) ')

    my_drinks[q_drink] = q_volume

    if q_else.lower() == 'n':
        break

    if q_else.lower() == 'y':
        print('Please add another drink\n')
        continue

print('You drunk:')
print('-' * 40)

for key, value in my_drinks.items():
    ethanol.append(value * all_drinks[key])
    num_of_drinks += 1
    print(f'{num_of_drinks}. {value} ml of {key}')

print('-' * 40)

sober_time = sum(ethanol) / gendercoef * 300
sober_time_hours = sober_time // 60
sober_time_minutes = sober_time % 60
sober_time_to_drive = datetime.now() + timedelta(hours=sober_time_hours)

message = (
    f'Total amount of alcohol = {sum(my_drinks.values())} ml\n'
    f'(including {int(sum(ethanol))} ml of clear ethanol)\n'
    f'Your Blood Alcohol Index is {(sum(ethanol) / gendercoef):.2f}‰\n'
    f'You can drive in {int(sober_time_hours)} h {int(sober_time_minutes)} min on '
    f'{sober_time_to_drive:%d %b %H:%M}'
)

print(message)
