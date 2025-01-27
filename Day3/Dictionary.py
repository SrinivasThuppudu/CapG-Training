D = {}                                                                  # Empty Dictionary
D1 = {'spam' : 2, 'eggs' : 3}                                           # Dictionary with two items
D2 = {'food': {'ham': 1, 'egg': 2}}                                     # Nested Dictionary
D3 = dict(name = 'Bob', age = 40)                                       # Creating Dictionary in another way
D4 = dict(zip(['x', 'y', 'z'], [1,[1, 2, 3, 4], 3]))                    # Zipping two lists into Dictionary
D5 = dict.fromkeys(['a', 'b'])     
print(D.update(D1))                                     # Initializing Dictionary with empty valued keys
print('', D,'\n', D1,'\n', D2,'\n', D3,'\n', D4, '\n', D5)              # Printing all Dictionaries