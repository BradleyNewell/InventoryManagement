import random
import re

read_file = open("words.txt", 'r')
write_file = open("saved_items.txt", 'a+')
blank = ''
for i in read_file:
    blank += i


def random_word():
    word = re.split('\n', blank)
    return random.choice(word)


def assignment(item_name):
    item = ''
    for i in range(4):
        item += random_word()
        item += ' '
    write_file.write(item_name + ': ' + item)

assignment('Book')
