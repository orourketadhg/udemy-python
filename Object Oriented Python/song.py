class Song:
    """Class to represent song
    
    Attributes:
        title (str): Title of song
        artist (Artist): Artist object representing songs author
        duration (int): Duration of song in seconds (can be 0)
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist):  An Artist object representing songs author
            duration (Optional [int]): Initial value of duration attribute.
                Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration

# will print the docstrings
# help(Song.__init__)
# print(Song.__doc__)


class Album:
    """Class to represent an Album, using its track list

    Attributes:
        name (str): name of album
        year (int): year of release
        artist (Artist): Artist object to represent artist
            if not specified, artist will default to "Various Artists"
        tracks (list[Song]): List of songs on album

    Methods:
        add_song: Used to add new song to artists album list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song(Song): a Song to add
            position(Optional[int]): add song to specified position in track list
                if not specified, will append to end
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Class to store artists details

    Arguments:
        name (str): name of srtist
        albums (List[Ablum]): A list of the artists albums
            the list includes only those albums in this collection, it is
            not an exhaustive list of the artists published work

    Methods:
        add_album: Used to add an album to artists album list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list
                if album in list already present, it will not add it again
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Add a new song to the collection of albums

        This method will add a song to an album in the collection.
        A new album will be created if if doesn't already exist

        Args:
            name (str): name of song
            year (int): year song was released
            title (str): title of song
        """
        album_found = find_object(name, self.albums)

        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


def find_object(field, object_list):
    """Check 'object_list to see if an object with a 'name' attribute equal to 'field' exists, return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums/albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)

            # print(artist_field, album_field, year_field, song_field)

            # attempt to find already existing artist object
            new_artist = find_object(artist_field, artist_list)

            # if attempt failed - create new artist and append to artist_list
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_check_file(artist_list):
    """Create a check file from the object data for comparison with the original file"""

    with open("albums/checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == '__main__':
    artist = load_data()

    print("there are {} artists".format(len(artist)))

    create_check_file(artist)
