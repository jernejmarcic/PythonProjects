alphabet = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf','hotel', 'india', 'juliett', 'kilo', 'lima', 'mike',
            'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform','victor', 'whiskey', 'x-ray', 'yankee', 'zulu']

word = str(input("Enter word: "))
i = 0
def spell_NATO(word):

    for i in range(len(word)):
        wrdy = ord(word[i])
        if 97<=wrdy<=122:
            turn = ord(word[i])-97
            print(f"{alphabet[turn]} ", end='')

        else:
            print(f"{word[i]} ", end='')




spell_NATO(word)

