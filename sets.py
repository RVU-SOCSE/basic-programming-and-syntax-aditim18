
ADITI.M
1RUA25BCA0006

set1 = {26, 25, 18, 10, "Aditi", "Dheeksha"}
set2 = {18, 10, "Nagashree", "Sahana", "Suma"}
print("Set 1:", set1)
print("Set 2:", set2)

set1.add("Suma")
print("\nAfter add():", set1)

set1.update([50, "Riya"])
print("After update():", set1)

set1.remove(25)
print("After remove():", set1)

set1.discard(100)
print("After discard():", set1)

set1.pop()
print("After pop():", set1)

temp_set = {1, 2, 3}
temp_set.clear()
print("After clear():", temp_set)

copy_set = set2.copy()
print("\nCopy of Set2:", copy_set)

print("\nUnion:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference (set1 - set2):", set1.difference(set2))

print("Symmetric Difference:", set1.symmetric_difference(set2))

print("\nIs set1 subset of set2?:", set1.issubset(set2))

print("Is set1 superset of set2?:", set1.issuperset(set2))

print("Are sets disjoint?:", set1.isdisjoint(set2))

set3 = {26, 18, 10}
set4 = {18, 10, 5}
set3.intersection_update(set4)
print("\nAfter intersection_update():", set3)

set5 = {26, 25, 18}
set6 = {18}
set5.difference_update(set6)
print("After difference_update():", set5)

set7 = {1, 2, 3}
set8 = {3, 4, 5}
set7.symmetric_difference_update(set8)
print("After symmetric_difference_update():", set7)
