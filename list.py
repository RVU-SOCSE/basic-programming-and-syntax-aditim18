ADITI.M
1RUA25BCA0006

my_list = [26, 25, 18, 10, 26, "Aditi", "Dheeksha", "Nagashree", "Sahana", "Suma"]

print("Original List:")
print(my_list)

my_list.append("Aditi")
print("\nAfter append():")
print(my_list)

my_list.insert(2, 25)
print("\nAfter insert():")
print(my_list)

my_list.extend([18, 10])
print("\nAfter extend():")
print(my_list)

my_list.remove(26)
print("\nAfter remove():")
print(my_list)

my_list.pop(3)
print("\nAfter pop():")
print(my_list)

print("\nIndex of 'Aditi':", my_list.index("Aditi"))

print("Count of 25:", my_list.count(25))

num_list = [26, 25, 18, 10]
num_list.sort()
print("\nAfter sort():", num_list)

num_list.reverse()
print("After reverse():", num_list)

copied_list = my_list.copy()
print("\nCopied List:")
print(copied_list)

temp_list = [26, 25, 18]
temp_list.clear()
print("\nAfter clear():", temp_list)
