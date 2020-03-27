n = int(input("Enter the number of elements: "))
prime = []
for i in range(0, n):
    num = int(input("Enter the number: "))
    prime.append(num)
print("The entered list is :", prime)
for i in prime:
    if i % 2 == 0:
        print(i, "is a prime number")
    else:
        print(i, "is a not a prime number")
