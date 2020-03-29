l1 = [[1,1,1,1],[2,2,2,2]]
l2 = [[2,2],[3,3],[4,4]]

def MM(a,b):
    c = []
    if len(a[0]) != len(b):
        print("The matrix cant be multiplied because of different dimensions")
        return c
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(b[0])):
            s = 0
            for k in range(0,len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)
    
    return c
# a=[[1,2]]
# b=[[1],[2]]
# print(MM(a,b))
print("--------------------------------")
print(MM(l1,l2))
