class Song:
    # Class attribute to keep track of the number of songs
    count = 0
    # Class attributes to store unique genres and artists
    genres = []
    artists = []
    # Class attributes to store genre and artist counts
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment count when a new song is created
        Song.add_song_to_count()

        # Add genre and artist to their respective lists
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increment the count of songs
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add genre to genres list if not already present
        if genre not in cls.genres:
            cls.genres.append(genre)
        # Add genre to genre_count dictionary
        cls.add_to_genre_count(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add artist to artists list if not already present
        if artist not in cls.artists:
            cls.artists.append(artist)
        # Add artist to artist_count dictionary
        cls.add_to_artist_count(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Add genre to genre_count dictionary with count
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Add artist to artist_count dictionary with count
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

