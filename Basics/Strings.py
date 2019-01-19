parrot = 'Norwegian blue'
print(parrot[3])

# Will print the 3rd last element in the string
print(parrot[-3])

# Will print from [x:y-1]
print(parrot[0: 6])

# Will print from 0 -> (6 - 1)
print(parrot[:6])

# will print from 6 -> N
print(parrot[6:])

# will print from 0 -> (6-1) in steps of 2
print(parrot[0:6:2])

# prints N times
print("test " * 5)

# Returns True if it is contained IN the second string
print("String" in "TestString")

# printing raw strings
string = r"Bloop \t\t Beep"
print(string)
