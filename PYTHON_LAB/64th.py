# Write a Python program to show that tuple values cannot be changed directly. Convert tuple into list, update it, and convert it back into tuple.



my_tuple = (10, 20, 30)
print("Original tuple:", my_tuple)
temp_list = list(my_tuple)
temp_list[1] = 50
my_tuple = tuple(temp_list)
print("Updated tuple:", my_tuple)
