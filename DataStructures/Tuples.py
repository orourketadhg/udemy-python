# tuple
t = "a", "b", "c", "d", ((1, 2), (2, 3))

# not tuple
print(t)
print("a", "b", "c")

# tuple
print(("a", "b", "c"))

# cannot change a tuple
# t[0] = 'd'

# create a new tuple with the altered element -- overwrite
t1 = t[0], "d", t[2]
print(t1)

# will unpack the tuple into the respective variables
# first, second, third = t
# print(first)
# print(second)
# print(third)

# as the data can be changed, unpacking it will prefer a tuple
# t1 = ['a', 'b', 'c', 'd']
# First, Second, Third = t1

first, second, third, fourth, fifth = t
# 2D tuple element
print(fifth)

# a list inside a tuple can be changed
a = (1, 2, 3, ["a", "b", "c"])

print(a)

a1, a2, a3, a4 = a

a4.append("d")
print(a)
