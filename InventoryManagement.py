import random
import re

read_file = open("words.txt", 'r')
write_file = open("saved_items.txt", 'a+')
blank = ''
for line in read_file:
    blank += line


def random_word():
    word = re.split('\n', blank)
    return random.choice(word)


def assignment(item_name):
    store = {}
    identifier = ''
    for words in range(4):
        identifier += random_word()
        identifier += ' '
    if identifier not in write_file:
        store.update({identifier.lower(): item_name})
        write_file.write(str(store) + '\n')
    else:
        assignment(item_name)

assignment('Book')
