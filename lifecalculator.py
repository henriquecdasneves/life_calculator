age = int(input('Enter your current age: '))

expect_life = 90
days = 365
weeks = 52
months = 12

years_left = ((expect_life) - (age))

days_left = (days) * (years_left)
weeks_left = (weeks) * (years_left)
months_left = (months) * (years_left)

print('You have', days_left, 'days,', weeks_left, 'weeks', 'and', months_left, 'months left.')
