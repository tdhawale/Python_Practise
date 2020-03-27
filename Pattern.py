
# for i in range (0, n+1)
#     for j in range(0, n+1)
#         if i + j == n:
#             pattern[i][j] = '*'
#         elif j == n / 2:
#             pattern[i][j] = '*'
#         elif i == j:
#             pattern[i][j] = '*'
#         elif :
#             pattern[i][j] = ' '

"""
for i in range(n, -1, -1):
    print(''*(n-i-1)+'* '*(3))
"""


def print_2d_array(arr):
    """Print 2D array"""
    assert len(arr) > 0 and len(arr[0]) > 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end="")
        print("")


# pattern == [[]]


def drawStar(n):
    assert n >= 2 and n % 2 == 0
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            if i + j == n:
                pattern[i][j] = '*'
            elif j == n / 2:
                pattern[i][j] = '*'
            elif i == j:
                pattern[i][j] = '*'
            else:
                pattern[i][j] = ' '


n = int(input("Enter a multiple of 2:"))
# drawStar(n)
