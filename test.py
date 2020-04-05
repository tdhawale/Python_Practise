import os
print("My name is", os.getlogin(), 'and I am', 26, " years old")

def you_pay(spending, is_monday):
    if spending <51:
        return ((spending)-(spending/100)*10)
    elif is_monday and spending >= 51:
        new_spending = spending - 5
    else:
        new_spending = spending
    if spending > 50 and spending <= 100:
        return (new_spending-((new_spending)/100)*20)
    else:
        return (new_spending-((new_spending)/100)*40)
    
test = [50, 51, 100, 101]
for num in test:
    print("For",num,"CAD, you pay", you_pay(num,True),"if  Monday")
print("--------------------------------------------------------------------------------")
for num in test:
    print("For",num,"CAD, you pay", you_pay(num,False),"if  Monday")