import numpy as np
import matplotlib.pyplot as plt
img = np.array([])
by_lst = []
with open('E:\Workspace\Python\Python_Practise\colorado_elev.vit', 'rb') as f:
    while True:
        data = f.read(1)
        if not data:
            break
        img = np.append(img,data)
        by_lst.append(data)



print("The numpy array is:")
print(img)
print()
print("The list is: ")
print(len(by_lst))