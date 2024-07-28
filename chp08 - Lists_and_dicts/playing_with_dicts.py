birthdays = dict([
    ('Luke Skywalker', '5/24/19'),
    ('Obi-Wan Kenobi', '3/11/57'),
    ('Darth Vader', '4/1/41')])

def birthday_check(name, birthdays):
    if name in birthdays.keys():
        print(birthdays[name])
    else:
        print('unknown')

birthday_check('Darth Vader', birthdays)
birthday_check('Yoda', birthdays)

for key in birthdays.keys():
    print(key, birthdays[key])

del(birthdays['Darth Vader'])
