spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print('spam.values = ',v)

for k in spam.keys():
    print('spam.key = ',k)

for i in spam.items():
    print('spam,items = ',i)

print()
print(spam.keys())
print(spam.values())
print(spam.items())

for k, v in spam.items():
    print()


