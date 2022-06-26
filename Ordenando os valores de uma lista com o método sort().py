""""
spam = ['a', 'z', 'A', 'Z']

#  spam.sort(key=str.lower)
print(spam)
print()

spam.sort(key=str.lower)
print(spam)
"""  # sort() condition
import random



def ent1():
    messages = ['It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later',
                'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']
    

ent1()
print(ent1(), '\n This code wont print nothing because the code there is no return for output ')
print()


def ent():
    messages = ['It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later',
                'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']
    return messages


ent()


print(' this code will output print because I get return into the code ent()')
#   print(messages)
print(ent()[random.randint(0, len(ent()) - 1)])
