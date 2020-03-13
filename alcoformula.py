#Alco Tracker App v0.3

ml = int(input('How much did you drink? (ml) '))
weight = int(input('Your weight is '))
gender = str(input('Your gender '))
alcohol = int(input('Alcohol % '))
ethanol = ml * (alcohol / 100)
gendermale = round(weight * 0.7)
genderfemale = round(weight * 0.6)

"""
if gender == 'male':
    print('You are male with gender koef equal', gendermale)
elif gender == 'female':
    print('You are female with gender koef equal', genderfemale)
"""

if gender == 'male':
    promille = ethanol / gendermale
    print('Your blood alcohol =', round(promille, 2), '‰')
elif gender == 'female':
    promille = ethanol / genderfemale
    print('Your blood alcohol =', round(promille, 2), '‰')

sobertime = promille / 0.2

print('You drunk', ethanol, 'ml clear ethanol')

print('You can drive approximately in', round(sobertime), 'hours')
