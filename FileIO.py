# # open file
# # file is going to be read and all data assigned to FileExample
# FileExample = open("D:\Programming\Python\FileIO\sample.txt", 'r')
#
# # will loop through each line in FileExample and print that line
# for line in FileExample:
#     # checks for "jabberwock"
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# # file is closed at the end of use
# FileExample.close()

# # with open removes the need to close the file after finishing using it
# # if there is an error with open will not open the file
# with open("D:\Programming\Python\FileIO\sample.txt", 'r') as jabber:
#     for line in jabber:
#         print(line)

with open("D:\Programming\Python\FileIO\sample.txt", 'r') as lineReader:
    # will read a single line then lineReader will iterate to the next line
    line = lineReader.readline()

    # wile line is not the EOF
    while line:
        print(line, end='')
        # iterate lineReader
        line = lineReader.readline()

    # will return a list of lines that can be used
    # lines = lineReader.readlines()

    # read a character at a time
    # more useful with binary files
    # char = lineReader.read()
