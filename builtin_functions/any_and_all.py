"""
examining the any and all functions

"""

__author__ = "Tadhg O'Rourke"
__date__ = "07/09/2019"

entries = [1, 2, 3, 4, 5]
entries_with_zero = [1, 2, 0, 4, 5]     # 0 counts as boolean False
entries_with_neg = [1, 2, -1, 4, 5]     # negative counts as boolean False
entry_with_none = []


# any()
# any() will check if (at least) any of the elements in an iterable are True - returns boolean value
print("all: {}".format(all(entries)))
print("all with zero: {}".format(all(entries_with_zero)))
print("all with negative: {}".format(all(entries_with_zero)))
print("all with none: {}".format(all(entry_with_none)))     # an empty will return TRUE

print("=" * 40)

# all()
# all() will check if all of the elements in an iterable are True - returns boolean value
print("any: {}".format(any(entries)))
print("any with zero: {}".format(any(entries_with_zero)))
print("any with negative: {}".format(any(entries_with_zero)))
print("any with none: {}".format(any(entry_with_none)))     # an empty will return FALSE


