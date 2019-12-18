my_list = [1, 2, 3, 4, 5, 6]

for number in my_list:
    print(number)

user_wants_number = True
while user_wants_number == True:
    number = 10
    print(number)
    user_input = input(f'Should we print {number} again ?? (y/n) ')

    if user_input == 'n':
        user_wants_number = False
