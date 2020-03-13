#Alco Tracker App v0.4

ml = int(input('How much did you drink? (ml): '))
weight = 76
alcohol = str(input('Specify your drink (beer/wine/vodka): '))
#gendermale = weight * 0.7
gender = str(input('What is your gender?: '))

if gender == 'male':
    gendermale = weight * 0.7
else:
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

promille = ethanol / gendermale
sobertime = promille / 0.2

print('Your blood alcohol =', round(promille, 2), '‰')
print('You drunk', round(ethanol, 2), 'ml clear ethanol.')
print('You can drive approximately in', round(sobertime), 'hours.')

print('Monthly average consumption will be:', (ethanol * 30) / 1000, 'l of ethanol.')
print('Yearly average consumption will be:', (ethanol * 365) / 1000, 'l of ethanol.')
