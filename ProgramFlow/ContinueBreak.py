# shoppingList = ['milk', 'eggs', 'pasta', 'bread']
#
# for item in shoppingList:
#     if item != 'eggs':
#         continue
#
#     print("buy " + item)

meal = ['egg', 'bacon', 'spam', 'sausages']
# empty string
nasty_food = ''

for item in meal:
    # break out of loop if item is 'spam'
    if item == 'spam':
        nasty_food = item
        # break out of for loop
        break
# else can follow a for which will only work if it has a break 
else:
    print('I\'ll have a plate of bacon then')

if nasty_food == 'spam':
    print('Can\'t I have anything without spam in it')
