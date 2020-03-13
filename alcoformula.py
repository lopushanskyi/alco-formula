#Alco Tracker App v0.3

ml = int(input('How much did you drink? (ml): '))
weight = int(input('Your weight is: '))
gender = str(input('Your gender (male/female): '))
alcohol = str(input('Specify your drink (beer/wine/vodka): '))
gendermale = weight * 0.7
genderfemale = weight * 0.6

if alcohol == 'beer':
    alcohol = 7
    ethanol = ml * (alcohol / 100)
elif alcohol == 'wine':
    alcohol = 12
    ethanol = ml * (alcohol / 100)
elif alcohol == 'vodka':
    alcohol = 40
    ethanol = ml * (alcohol / 100)
else:
    print('Please restart app and specify your drink.')

if (gender == 'male') or (gender == 'man'):
    promille = ethanol / gendermale
    sobertime = promille / 0.2
    print('Your blood alcohol =', round(promille, 2), '‰')
    print('You drunk', ethanol, 'ml clear ethanol')
    print('You can drive approximately in', round(sobertime), 'hours')

elif (gender == 'female') or (gender == 'woman'):
    promille = ethanol / genderfemale
    sobertime = promille / 0.2
    print('Your blood alcohol =', round(promille, 2), '‰')
    print('You drunk', ethanol, 'ml clear ethanol')
    print('You can drive approximately in', round(sobertime), 'hours')
else:
    print('Please specify your gender.')
