minimum = int(input())
maximum = int(input())
hours = int(input())

if hours < minimum:
    print("Deficiency")
elif hours > maximum:
    print("Excess")
else:
    print("Normal")
