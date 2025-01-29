t = ()                                              # Empty Tuple
t1 = (0, )                                          # One item Tuple
t2 = (0, 'Cl', 1.2, 3)                              # Four Item Tuple
t3 = ('abc', ('def', 'xyz'))                        # Nested Tupels
t4 = tuple('spam')                                  # Tuple of items in an iterable

print("Empty Tuple:", t)
print("One item Tuple:", t1)
print("Four Item Tuple:", t2)
print("Nested Tuple:", t3)
print("Tuple of items in an iterable", t4)
print("Second element of t2:", t2[1])
print("Element in t3[1][0] is:", t3[1][0])
print("Slicing of tuple t4 from 1 to 3:", t4[1:3])
print("Length of tuple t4:", len(t4))