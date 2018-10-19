# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

# unpack imelda
title, artist, year, tracks, = imelda
print(title)
print(artist)
print(year)

# print without unpacking tracks
for song in tracks:
    print("\t", song)

# print with unpacking tracks
for song in tracks:
    # unpack tracks tuple into its elements
    songID, title = song
    # print tracks
    print("\t", songID, title)
