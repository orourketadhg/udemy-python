# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the FOR loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example
# the 2 times tables should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#   10 times 2 is 20
#   11 times 2 is 22
#   12 times 2 is 24
# ===================================================================

with open("D:/Programming/Python/FileIO/sample.txt", 'a') as Poem:
    for i in range(1, 13):
        for j in range(1, 13):
            print(j, " times ", i, " is ", (i * j), file=Poem)

        print("\n", file=Poem)


with open("D:/Programming/Python/FileIO/sample.txt", 'r') as Poem:
    line = Poem.readline()

    while line:
        print(line, end=' ')
        line = Poem.readline()
