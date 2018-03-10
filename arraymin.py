a = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    a.append(numbers)
print("\nMinimum element in the list is :", min(a))
