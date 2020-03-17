print("Hello user welcome to number system conversion program ")
print("Below are the supported input number formats"
      "\n1.Binary"
      "\n2.Decimal"
      "\n3.Octal"
      "\n4.Hexa decimal ")
format = input("Please enter your choice : ")
#input always returns string format. So below code was
#not working in if else
if format == 1 or 2 or 3 or 4:
    number = input("Please enter the number : ")
    if format == '1':
        number = int(number,2)  # converting binary to integer
        # do nothing in case of format is 2
        # integer will be stored as integer
    elif format == '3':
        number = int(number,8) # converting octal to integer
    elif format == '4':
        number = int(number,16)  # converting hexadecimal to integer

    r = 'Y'
    while r == 'Y':
        option = int(input("\n Below are the number format you can "
                           "convert into "
                            "\n 1. Binary"
                            "\n 2. Decimal"
                            "\n 3. Octal"
                            "\n 4. Hexa Decimal"
                            "\n "
                            "\n Please enter your choice : "))

        if option == 1 :
            binary = bin(number)
            print("The binary number value " , binary)
            r = input("Do you want to continue (Y/N) : ")
        elif option == 2 :
            decimal = number
            print("The decimal number value " ,decimal)
            r = input("Do you want to continue (Y/N) : ")
        elif option == 3:
            octal = oct(number)
            print("The octal number value " ,octal)
            r = input("Do you want to continue (Y/N) : ")
        elif option == 4:
            hex = hex(number)
            print("The hexadecimal number value " ,hex)
            r = input("Do you want to continue (Y/N) : ")