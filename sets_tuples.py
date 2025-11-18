# sets and tuples examples:
# set examples:
set1 = {1, 2, 3, 4, 5}
print(set1)
print(type(set1))
set1.add(6)
print(set1)
set1.remove(2)
print(set1)

# sets drop duplicate variables:
set2 = {"apple", "bannana", "cherry", "cherry"}
print(set2)

#tuples examples:
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))
# tuples are unmutable, meaning they cannot be changed after creation
# this makes tuples useful for storing data that should not be modified
social_security_number = (123444, 444445, 5676789)
print(social_security_number)