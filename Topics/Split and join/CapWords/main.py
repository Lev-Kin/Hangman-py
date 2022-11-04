words = input().lower().split('_')
words_cap = [word.capitalize() for word in words]
print(''.join(words_cap))
