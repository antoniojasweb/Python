# Example of slicing in Python

# Define a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Mi lista es:", my_list)

# Slicing the list
# Syntax: list[start:end:step]
slice_1 = my_list[2:5]  # Elements from index 2 to 4
slice_2 = my_list[:4]   # Elements from start to index 3
slice_3 = my_list[5:]   # Elements from index 5 to end
slice_4 = my_list[::2]  # Every second element
slice_5 = my_list[::-1] # Reversed list
slice_6 = my_list[::-2] # Reversed list

# Print the slices
print("Slice 1 (2:5):", slice_1)
print("Slice 2 (:4):", slice_2)
print("Slice 3 (5:):", slice_3)
print("Slice 4 (::2):", slice_4)
print("Slice 5 (:: -1):", slice_5)
print("Slice 6 (:: -2):", slice_6)

for valor in range(2,30,2):
    print(valor)
