import random

# character_list = ['&', '\'', '*', '@', '\\', '`', '|', '^', ':', '-', ',', '$', '.', '"', '=', '!', '#', '%', '+', '?', '/', '~', ';', '<', '>', '{', '}', '[', ']', '(', ')']
character_list = ['&', '@', '\\', '`', '=', '#', '/', '(', ')']
ITERATIONS = 10
MULTIPLE_LINES = False

with open(r'D:\temp\random_string.txt', 'w') as f:
    for i in range(ITERATIONS):
        list_copy = character_list.copy()

        character_string = ""
        while len(list_copy) > 0:
            character_string += list_copy.pop(random.randint(0, len(list_copy) - 1))

        print(character_string)
        if MULTIPLE_LINES: character_string + '\n\n'
        f.write(character_string)
