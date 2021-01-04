import random

character_list = ['&', '\'', '*', '@', '\\', '`', '|', '^', ':', '-', ',', '$', '.', '"', '=', '!', '#', '%', '+', '?', '/', '~', ';', '<', '>', '{', '}', '[', ']', '(', ')']

for i in range(3):
    list_copy = character_list.copy()

    character_string = ""
    while len(list_copy) > 0:
        character_string += ' ' + list_copy.pop(random.randint(0, len(list_copy) - 1))

    print(character_string)
