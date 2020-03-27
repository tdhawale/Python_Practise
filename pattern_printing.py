for i in range(1, 5):
    for j in range(i):
        print("# ", end="")
        j = j + 1
    print()
    i = i + 1
print()
for i in range(4, 0, -1):
    for j in range(i):
        print("# ", end="")
        j = j - 1
    print()
    i = i - 1

print()
n = 4
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(n - (i - j), end="")
        j = j - 1
    print()
    i = i - 1
