# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
print("----------------------------------------------------------------")
print("COVID-19 cases dated in 3/20/2020")
print("----------------------------------------------------------------")
COVID_INDIA = {"Maharashtra": 51,
               "Kerala": 40,
               "UP": 23,
               "Delhi": 17
               }

COVID_GERMANY = {"Bremen": 121,
                 "Hamburg": 586,
                 "Hesse": 813,
                 "Lower Saxony": 803,
                 "NRW": 3497,
                 "Sarland": 146
                 }

COVID_USA = {"New York": 7102,
             "Washington": 1377,
             "California": 1073,
             "Arizona": 53,
             "Colorado": 277,
             "Pennsylvania": 214
             }

print("-------------------------------------------------------------------------------")
print("The number of cases in Maharashtra in India are:",
      COVID_INDIA["Maharashtra"])  # it is case sensitive
print("The number of cases in NRW in Germany are:", COVID_GERMANY.get("NRW"))
print("-------------------------------------------------------------------------------")
# change values
COVID_GERMANY["NRW"] = 3496
print("The number of cases in NRW in Germany are:", COVID_GERMANY.get("NRW"))
COVID_USA["New York"] = 7100
print("The number of cases in New York in USA are:", COVID_USA["New York"])
print("-------------------------------------------------------------------------------")
# looping through the dictionary
print("The state wise number of cases affected in India are given below")
for x, y in COVID_INDIA.items():
    print("State :", x, "(", y, ")")
print()
print()
print("The state wise number of cases affected in Germany are given below")
for x, y in COVID_GERMANY.items():
    print("State :", x, "(", y, ")")
print()
print()
print("The state wise number of cases affected in USA are given below")
for x, y in COVID_USA.items():
    print("State :", x, "(", y, ")")
print()
print()
print("-------------------------------------------------------------------------------")
# add items
COVID_INDIA["Haryana"] = 17
COVID_INDIA["Rajasthan"] = 16
COVID_INDIA["Mumbai"] = 20
COVID_INDIA["Pune"] = 20
print("The number of cases in India :", COVID_INDIA)
if "Karnataka" in COVID_INDIA:
    print("The number of cases in Karnataka are:", COVID_INDIA.get("Karnataka"))
else:
    COVID_INDIA["Karnataka"] = 15
    print("The number of cases in Karnataka are:", COVID_INDIA.get("Karnataka"))
print("-------------------------------------------------------------------------------")
# Remove items from the dictionary
print("The number of cases in India :", COVID_INDIA)
# pop removes specified item
COVID_INDIA.pop("Mumbai")
print("Removed Mumbai :", COVID_INDIA)
# popitem removes the element on the top of the stack
COVID_INDIA.popitem()
print("Removed top element :", COVID_INDIA)
COVID_INDIA["Pune"] = 20
print("The number of cases in India :", COVID_INDIA)
del COVID_INDIA["Pune"]
print("The number of cases in India excluding Pune :", COVID_INDIA)
print()
print("-------------------------------------------------------------------------------")
COVID_INDIA_temp = COVID_INDIA.copy()
print("The temporary list is :", COVID_INDIA_temp)
# clear is used to clear the list
COVID_INDIA_temp.clear()
print("The temporary list is :", COVID_INDIA_temp)
del COVID_INDIA_temp
print("-------------------------------------------------------------------------------")
# The total number of cases in the world
COVID_WORLD = {"INDIA": COVID_INDIA,
               "GERMANY": COVID_GERMANY,
               "USA": COVID_USA}
print("The number of cases in the world:", COVID_WORLD)
print("-------------------------------------------------------------------------------")
for x, y in COVID_WORLD.items():
    print()
    print("#################################################################")
    print("The number of cases in country", x, "are:")
    for a, b in y.items():
        print(a, "(", b, ")")

print("------------------------------------------------------------------------------")
print("The total number of cases in India", sum(COVID_INDIA.values()))
print("The total number of cases in Germany", sum(COVID_GERMANY.values()))
print("The total number of cases in USA", sum(COVID_USA.values()))
total_world = sum(COVID_INDIA.values()) + \
    sum(COVID_GERMANY.values()) + sum(COVID_USA.values())
print("The total number of cases in World", total_world)
