import random

print('H A N G M A N')

words = ['python', 'java', 'swift', 'javascript']
x = random.choice(words)
y = x.format()
if x == 'python':
    print('Guess the word pyt---:')
elif x == 'java':
    print('Guess the word jav-:')
elif x == 'swift':
    print('Guess the word swi--:')
if x == 'javascript':
    print('Guess the word jav-------:')

word = input()
if word == x:
    print('You survived!')
else:
    print('You lost!')
