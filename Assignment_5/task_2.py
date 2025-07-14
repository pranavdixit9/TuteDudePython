my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list: ", my_list)

new_list = my_list[:5:]
print("Extracted first five elements: ", new_list)

rev_list = new_list[::-1]
print("Reversed extracted elements: ", rev_list)