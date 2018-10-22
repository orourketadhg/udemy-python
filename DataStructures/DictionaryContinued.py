fruit = {"orange": "a sweet, orange, citrus fruit",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "round and crunchy"}

print(fruit)

veg = {"cabbage": "every child's worst",
       "sprouts": "Christmas nightmare",
       "corn": "not digestible",
       "peas": "goes well with corn"}

print(veg)

veg.update(fruit)
print(veg)

fruitCopy = fruit.copy()
print(fruitCopy)
