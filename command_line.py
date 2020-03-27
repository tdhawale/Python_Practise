import sys
# to run command line arguments you use argv and you need to import sys
# to run this program go to ommand promt and navigate to the loacation
# where the file is present
# After you navigate to the loaction where the file is present
# Enter : python command_line.py  8    9
#                   [0]          [1]  [2]
# index 1 will have the file name
# index 2 will have the value of variable x
# index 3 will have the value of variable y
######################################################################
# Note : You can't run this program from VS code because it is
# waiting for command line argument
######################################################################
x = int(sys.argv[1])    # so argv[1]
y = int(sys.argv[2])    # so argv[2]
z = x + y
print("The sum calculated by command line arguments is :", z)
