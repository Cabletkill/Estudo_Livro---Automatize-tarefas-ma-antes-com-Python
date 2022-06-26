spam = ['apples', 'bananas', 'tofu', 'cats']

for line in spam:
    print(line)
    for l in range(len(line)):
        print(line[l],'\n')