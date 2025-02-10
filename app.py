import numpy as np

array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

print("Firt element:", array[0])
print("Last element:", array[-1])

print("Elements from 1 to 3:", array[1:3])

my_list = [1, 2, 3, 4, 5]
print("list:", my_list)

my_list.append(6)
print("List after append:", my_list)

my_list.insert(2, 7)
print("List after insert:", my_list)

my_list.remove(4)
print("List after remove:", my_list)

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

fruits = ["apple", "banana", "chery"]
for fruit in fruits:
    print(fruit)

i = 0 
while 1 < 5:
    print(i)

my_list = [1, 2, 3, 4, 5]
for i, element in enumerate(my_list):
    print(f"Index {i}: {element}")
 