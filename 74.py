x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(n):
    power = 2 * i + 1

    fact = 1
    for j in range(1, power + 1):
        fact = fact * j

    term = (x ** power) / fact

    if i % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

print("Sum =", sum)