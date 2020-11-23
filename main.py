import random
from datetime import date
today = date.today()


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

    def number_of_episodes(self):
        print('{} has {} episodes'.format(self.title, self.episode))

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
            movie.play
            return
    else:
        print('Sorry, title not found.')


def generate_views():  # Randomly generates views for items in library from range 1 to 100
    rand_movie = random.choice(library)
    rand_movie.views += random.choice(range(1, 101))


def ten_times():
    for i in range(10):
        generate_views()


def top_titles(content_type):  # Shows top movies or series based on views
    if content_type == 'movies':
        movies = filter(lambda s: not isinstance(s, Series), library)
        by_views = sorted(movies, reverse=True, key=lambda m: m.views)[:3]
        print("Top 3 Movies:")
        for name in by_views:
            print('- {} - {} views.'.format(name.title, name.views))
    elif content_type == 'series':
        movies = filter(lambda s: isinstance(s, Series), library)
        by_views = sorted(movies, reverse=True, key=lambda m: m.views)[:3]
        print('Top 3 Series:')
        for name in by_views:
            print('- {} - {} views.'.format(name.title, name.views))


movie1 = Movie('Pulp Fiction', '1994', 'Crime, Drama', 0)
movie2 = Movie('The Shawshank Redemption', '1994', 'Drama', 0)
movie3 = Movie('The Godfather', '1972', 'Crime, Drama', 0)
movie4 = Movie('Enola Holmes', '2020', 'Action, Adventure, Crime', 0)
movie5 = Movie('Interstellar', '2014', 'Adventure, Drama, Sci-Fi', 0)
series1 = Series(1, 13, 'The Simpsons', '1989', 'Sitcom', 0)
series2 = Series(1, 10, 'Band of Brothers', '2001', 'Action, Drama, History', 0)
series3 = Series(1, 7, 'Breaking Bad', '2008', 'Crime, Drama, Thriller', 0)
series4 = Series(1, 8, 'The Mandalorian', '2019', 'Action, Adventure, Sci-Fi', 0)
series5 = Series(1, 8, 'The Witcher', '2019', 'Action, Adventure, Fantasy', 0)

library = (movie1, movie2, movie3, movie4, movie5, series1, series2, series3, series4, series5)


if __name__ == '__main__':
    print("Movie Library\n")
    ten_times()
    print('Most popular shows for {}\n'.format(today.strftime("%d/%m/%Y")))
    top_titles('movies')
    top_titles('series')
