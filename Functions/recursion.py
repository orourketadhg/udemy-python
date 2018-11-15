import os
# generally recursion is not used in python,
# but depending on problem may still be used
# can effects the processing time due to stacking


# factorial(n)
def fact(n):
    result = 1
    if n > 1:
        for f in range(1, n + 1):
            result *= f
    return result


# for i in range(15):
#     print(i, ': ', fact(i))


# factorial(n) using recursion
def fact_rec(n):
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)


# for i in range(15, 0, -1):
#     print(i, ': ', fact_rec(i))

listing = os.walk('.')


def list_directories(s):
    # nested function
    # rare to have any more than 1 deep nested functions
    def dir_list(d):
        # will get a variable from the parent functions - like global
        # only use if no other option will work - can lead to bugs with scope
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    # nested function cannot see out scope variable
    tab_stop = 0
    if os.path.exists(s):
        print("Directory list of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")


# will print the same as globals contain locals
print(locals())
print(globals())
# python will search for data in order of Local, Enclosing, Globals, Builtins (LEGB)

# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)
