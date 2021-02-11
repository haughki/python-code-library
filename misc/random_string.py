import random

# character_list = ['&', '\'', '*', '@', '\\', '`', '|', '^', ':', '-', ',', '$', '.', '"', '=', '!', '#', '%', '+', '?', '/', '~', ';', '<', '>', '{', '}', '[', ']', '(', ')']
# character_list = ['&', '@', '\\', '`', '=', '#', '/', '(', ')']
character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# character_list = ['a', 'b', 'd', 'g', 'h', 'j', 'n', 'r', 'x', 'z']
# character_list = ['a', 'd', 'h', 'n', 'p', 'x', 'z']
# character_list = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
ITERATIONS = 10
MULTIPLE_LINES = True
WORDS = False

with open(r'D:\temp\random_string.txt', 'w') as f:
    for i in range(ITERATIONS):
        list_copy = character_list.copy()

        character_string = ""
        space = " " if WORDS else ""

        while len(list_copy) > 0:
            character_string += list_copy.pop(random.randint(0, len(list_copy) - 1)) + space

        print(character_string)
        if MULTIPLE_LINES: character_string = character_string + '\n\n'
        f.write(character_string)
