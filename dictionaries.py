ADITI.M
1RUA25BCA0006


d1 = {"Aditi": 98, "Pawan": 99}
d2 = {"Dheeksha": 98, "Girija": 99}

d1.update(d2)
print("After using update():")
print(d1)

d1 = {"Aditi": 98, "Pawan": 99}
d2 = {"Dheeksha": 98, "Girija": 99}

d3 = d1 | d2
print("\nAfter using | operator:")
print(d3)
