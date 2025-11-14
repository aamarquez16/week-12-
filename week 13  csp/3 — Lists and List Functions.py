# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

# Collections are used to store multiple items in a singular varible
# lists are ordered collection of items \
# lists are mutable, meaning you can change your content
# lists are created using square bracets []


# instead of creating seperate varibles for each item, we can store them in a list. this makes our jobs easier when we manage multipule items 
# performance task answer^
 
#my_list =[1,2,3,4,5]
#print(my_list)
#print(type(my_list))
#print(my_list[0])
#print(my_list[1:4])
#print(my_list[0:])
# modifying list
# adding an item to the end of the list 
#my_list.append(6)
#my_list.append(7)
#my_list.append(8)
#print(my_list)
#my_list.extend([9,10,11,12,13,14])
#print(my_list)
# add 500 more numbers to the list \
#my_list.extend(list(range(15,515)))
#print(my_list)
#my_list.extend(list(range(515,1115)))
#print(my_list)

#sorting the list #
numbers = [4, 2, 5, 1, 3]
numbers.sort()
print(numbers)
#reverse the list
numbers.reverse
print(numbers)
#inserting an item into a spesific postition 
numbers.insert(2, 10)
print(numbers)
third_list = [7, 8, 9]
third_list[0] = 6
print(third_list)
third_list[-1] = 10
print(third_list)

import random 
random_list = random.sample(range(1, 1000), 100)
# this will create a list of 10 unique random numbers between 1 and 99
print(random_list)
print(sorted(random_list))
#reverse the list
# remove every 3rd item from the list
random_list.reverse
print(random_list)
# summary of list functions 
# .append(item) - adds item to the end of the list 
# .pop(index) - removes and returns the item at the specified index
# .sort() - sorts the list of ascending order
# .reverse() - reverses the order of the list 
















# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)




# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.