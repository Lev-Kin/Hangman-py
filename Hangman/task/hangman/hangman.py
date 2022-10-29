import random

words = ['python', 'java', 'swift', 'javascript']
hidden = random.choice(words)
correct_word = ''
all_letters = ''
tries = 0

print("H A N G M A N")
while tries < 8:
    result = ''
    for l in hidden:
        if l in correct_word:
            result += l
        else:
            result += '-'

    print()
    print('{}'.format(result))
    if set(hidden) == set(correct_word):
        print('You guessed the word!\nYou survived!')
        break
    while True:
        user_letter = input('Input a letter: ')
        all_letters += user_letter
        break
    if user_letter not in hidden:
        tries += 1
        print("That letter doesn't appear in the word")
    elif user_letter in correct_word:
        tries += 1
        print('No improvements')
    else:
        correct_word += user_letter

if tries == 8:
    print('You lost!')
    exit()
