# # import os
# # print("My name is", os.getlogin(), 'and I am', 26, " years old")
# #
# # def you_pay(spending, is_monday):
# #     if spending <51:
# #         return ((spending)-(spending/100)*10)
# #     elif is_monday and spending >= 51:
# #         new_spending = spending - 5
# #     else:
# #         new_spending = spending
# #     if spending > 50 and spending <= 100:
# #         return (new_spending-((new_spending)/100)*20)
# #     else:
# #         return (new_spending-((new_spending)/100)*40)
# #
# # test = [50, 51, 100, 101]
# # for num in test:
# #     print("For",num,"CAD, you pay", you_pay(num,True),"if  Monday")
# # print("--------------------------------------------------------------------------------")
# # for num in test:
# #     print("For",num,"CAD, you pay", you_pay(num,False),"if  Monday")
#
# # f =
# # print(f.read())
#
# # with open('colorado_elev.vit', 'rb') as f:
# # data = f.read()
# # print(data)
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# with open('colorado_elev.vit', 'rb') as f:
#     data = f.read()
#
# arr1 = np.array([])
# print(arr1)
# # for i in data:
# #     arr1 =  arr1
# lst = []
# for i in data:
#     lst.append(i)
#
# print(len(lst))
# arr1 = np.array(lst[268:])
# arr1 = arr1.reshape(400,400)
# print(arr1)
#
#
# # plt.imshow(arr1, origin = 'lower',  extent = [0, 400, 0, 400], aspect = 1000)
# # plt.xlabel('X')
# # plt.ylabel('Y')
# # plt.plot(arr1)
# #
# # fig ,axes = plt.subplots() # figure will have two rows and two column
# # It is a 1D array
#
# # axes.imshow(arr1, cmap='gray')
# # axes.plot(arr1)
# # axes.set_title('Colorado Data Set')
# # axes.set_xlim([0,400])
# # axes.set_ylim([0,400])
# # plt.show()
#
#
# # fig1 ,axes1 = plt.subplots() # figure will have two rows and two column
# # It is a 1D array
#
# # axes.imshow(arr1, cmap='gray')
# # axes1.plot(arr1[100:300])
# # axes1.set_title('Colorado Data Set')
# # axes1.set_xlim([0,400])
# # axes1.set_ylim([0,400])
# # plt.show()
#



from matplotlib import pyplot as plt
import mplcursors
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
df = DataFrame(
    [(0, 0, 1, 1),
     (1, 1, 1, 1),
     (0, 4, 1, 1),
     (0, 2, 1, 1)],
    columns=["x_pos", "y_pos", "x_direct", "y_direct"])

df['length'] = np.hypot(df.x_direct , df.y_direct)
flow = ax.quiver(df.x_pos, df.y_pos, df.x_direct, df.y_direct)
ax.set_title('Quiver plot with one arrow')
#
# df.plot.scatter("height", "weight")
mplcursors.cursor( hover=True ).connect(
    # "add" , lambda sel : sel.annotation.set_text(df["length"][sel.target.index]))
    # "add", lambda sel: sel.annotation.set_text("{}".format([df["x_pos"][sel.target.index], df["y_pos"][sel.target.index],
    #                                             df["x_direct"][sel.target.index],df["y_direct"][sel.target.index],
    #                                             df["length"][sel.target.index]])))
    "add" ,lambda sel : sel.annotation.set_text("x = {}, y = {} , dx = {} , dy = {} , length = {:.2f}".format(
                                                                           df["x_pos"][sel.target.index],
                                                                           df["y_pos"][sel.target.index],
                                                                           df["x_direct"][sel.target.index],
                                                                           df["x_direct"][sel.target.index],
                                                                           df["length"][sel.target.index]))
    )
plt.show()

# test: skip
# import matplotlib.pyplot as plt
# import mplcursors
# import numpy as np
#
# x = np.array([0, 1, 2, 3, 4])
# y = np.array([1, 2, 3, 4, 5])
# y2 = np.array([2, 3, 4, 5, 6])
#
# fig, ax = plt.subplots()
# line1, = ax.plot(x, y, "ro")
# line2, = ax.plot(x, y2, 'bx')
#
# labels1 = ["a", "b", "c", "d", "e"]
# labels2 = ["f", "g", "h", "i", "j"]
#
# d = dict(zip([line1, line2], [labels1, labels2]))
#
# mplcursors.cursor(ax, hover=True).connect(
#     "add", lambda sel: sel.annotation.set_text(d[sel.artist][sel.target.index]))
#
# plt.show()