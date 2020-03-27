i = 1
while i <= 6:
    print("This is the", i, "th iteration")
    i += 1
else:
    print("End of while loop after", i, "iterations")
# https: // github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches
print("Hi1 \rHi2 Hi3 Hi4")
# https://www.codespeedy.com/how-does-carriage-return-work-in-python/
# So whatever content is there after the \r will come at the beginning of our whole string.
print("This is a string to test how \rcarriage return works\n")
print("------------------------------------------------------")


i = 1
while i <= 6:
    print("Arsenal", end="")
    j = 1
    while j <= 3:
        print("!", end="")
        j = j + 1
    print()  # empty line
    # print("\n")  # blank line
    i = i + 1
