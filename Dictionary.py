#Dictonary is used to specify key value pairs
"""
d = {'Tejas': 8796740405 , 'Shreyash':7040144021}
print(d)
d.update({'Tejas': 8888633136})
d.update({'Dhiraj': 8888633136})
d.update({'Tejas': 8796740405})
d.update({'Shweta': 8390120866})
print(d)
print(d.keys())
print(d.values())
"""
def dictEqual(d1, d2):
    type_d1 = type(d1)
    type_d2 = type(d2)
    if type_d1 != type_d2:
        return False

    if isinstance(d1, dict):
        if len(d1) != len(d2):
            print('Dictonaries not equal')
            return False
        for key in d1:
            if key not in d2:
                print('Key not present')
                return False
            else:
                if d1[key] != d2[key]:
                    print(d1[key])
                    print('Value Not matching')
                    return False
                else:
                    print('Dictionaries equal')
                    return True
        return True

d1 = {'key1':1 , 'key2':2}
d2 = {'key1':1, 'key2':2}

dictEqual(d1, d2)

