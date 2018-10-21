cities = ["Dublin", "Cork", "Galway"]

# create/open cities.txt and write to file
# with open("D:\Programming\Python\FileIO\Cities.txt", 'w') as city_file:
#     # write city to city_file
#     for city in cities:
#         print(city, file=city_file)

cities2 = []

# open city file read
with open("D:\Programming\Python\FileIO\Cities.txt", 'r') as city_file:
    for city in city_file:
        # append a stripped of escape characters string to list
        cities2.append(city.strip())

for i in cities2:
    print(i)