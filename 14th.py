n = int(input("Enter a number: "))
k = int(input("Enter bit position: "))

if (n & (1 << k)) != 0:
    print("Kth bit is set")
else:
    print("Kth bit is not set")