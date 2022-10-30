import random
from string import ascii_lowercase

word = random.choice(['python', 'java', 'swift', 'javascript'])
s = set()
w = set()
tries = 8

print("H A N G M A N")
while tries > 0:
    print()
    for k in word:
        if k in s:
            print(k, end='')
        else:
            print('-', end='')

    print()
    print('Input a letter: ', end='')
    n = input()
    if n not in word and n not in w and n in ascii_lowercase:
        print("That letter doesn't appear in the word.")
        tries -= 1
        w.add(n)
    elif n in w:
        print("You've already guessed this letter.")
        tries -= 0
    elif n in s:
        print("You've already guessed this letter.")
        tries -= 0
    elif len(n) > 1 or n == '':
        print('Please, input a single letter.')
        tries -= 0
    elif n not in ascii_lowercase:
        print('Please, enter a lowercase letter from the English alphabet.')
        tries -= 0
    else:
        s.add(n)
        if set(word) == s:
            print('You guessed the word ' + word + '!\nYou survived!')
            break
else:
    print('You lost!')
