my_list = [] # Start an empty list
my_list.append(10) # Append the value 10
my_list.append(20) # Append the value 20
my_list.append(30) # Append the value 30
my_list.append(40) # Append the value 40 
print(f"List after appending: {my_list}")
my_list.insert(1, 15)
print(f"List after inserting 15: {my_list}")
my_list.extend([50, 60, 70])
print(f"List after extending: {my_list}")
my_list.pop()
print(f"List after removing the last element: {my_list}")
my_list.sort()
print(f"List after sorting: {my_list}")
index_of_30 = my_list.index(30)
print(f"The index of the value 30 is: {index_of_30}")