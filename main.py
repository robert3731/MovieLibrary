class Movie:
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views

    @property
    def play(self):  # Increases views of title by 1
        self.views += 1
        print('{} ({})'.format(self.title, self.year))


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    @property
    def play(self):  # Increases views of title by 1
        self.views += 1
        self.episode += 1
        print('{} S{:02d}E{:02d}'.format(self.title, self.season, self.episode))


def get_movies():  # Filters library and displays series only
    movies = filter(lambda s: not isinstance(s, Series), library)
    by_name = sorted(movies, key=lambda m: m.title)  # Return titles sorted by name
    print('Movies:')
    for name in by_name:
        print('- {}'.format(name.title))


def get_series():  # Filters library and displays series only
    series = filter(lambda s: isinstance(s, Series), library)
    by_name = sorted(series, key=lambda m: m.title)  # Return titles sorted by name
    print('Series:')
    for name in by_name:
        print('- {}'.format(name.title))


def search():  # Allows to search the exact title in library
    name = input('Enter movie title:')
    for movie in library:
        if movie.title == name:
            print('Title found.')
            return
    else:
        print('Sorry, title not found.')


movie1 = Movie('Pulp Fiction', '1994', 'Crime, Drama', 0)
movie2 = Movie('The Shawshank Redemption', '1994', 'Drama', 0)
movie3 = Movie('The Godfather', '1972', 'Crime, Deama', 0)
series1 = Series(1, 1, 'The Simpsons', '1989', 'Sitcom', 0)
series2 = Series(1, 1, 'Band of Brothers', '2001', 'Action, Drama, History', 0)
series3 = Series(1, 1, 'Breaking Bad', '2008', 'Crime, Drama, Thriller', 0)

library = (movie1, movie2, movie3, series1, series2, series3)

get_movies()
get_series()
search()
