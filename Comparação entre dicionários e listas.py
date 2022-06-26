"""
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
spam = {12345: 'Luggage Combination', 42: 'The Answer'}
eggs = {'name': 'Sophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Sophie'}
print(eggs == ham)
print(eggs == myCat)
print()
"""


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


while True:
    print('Enter a name :')
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)

    else:
        print('I do not have a birthday information for ' + name)
        print()
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated")