number = input()
count = 0
list_number = []

for digit in number:
    total = count + int(digit)
    count = total
    list_number.append(total)

print(list_number)
