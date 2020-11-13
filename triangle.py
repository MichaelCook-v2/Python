amount = float(input('Total Bill Amount? '))
level_of_service = input('Level of Service? ')
split = int(input('Split how many ways? '))
if (level_of_service == 'great'):
    level_of_service = level_of_service.lower()
    tip = (amount * .2)
elif (level_of_service == 'fine'):
    level_of_service == level_of_service.lower()
    tip = (amount * .15)
elif (level_of_service == 'bad'):
    level_of_service = level_of_service.lower()
    tip = (amount * .10)
else:
    tip = 0
print(f'Tip Amount: {tip:.2f}')
total_amount = (amount + tip)
print(f'Total Amount {total_amount:.2f}')
split_amount = (amount / split)
print(f'Total amount per person {split_amount:.2f}')