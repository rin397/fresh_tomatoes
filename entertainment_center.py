import media
import fresh_tomatoes

toy_movie = media.Movie( 'Toy Story', 'Toy Story movie_storyline' , 
	'https://upload.wikimedia.org/wikipedia/zh/d/dc/Movie_poster_toy_story.jpg' , 
	'https://www.youtube.com/watch?v=nCqtQLmJTl0','2012/01/2')
avatar_movie = media.Movie( 'Avatar', 'Avatar movie_storyline' , 
	'https://upload.wikimedia.org/wikipedia/zh/b/b0/Avatar-Teaser-Poster.jpg' , 
	'https://www.youtube.com/watch?v=5PSNL1qE6VY','2013/01/2')
school_rock_movie = media.Movie( 'school of rock', 'school of rock movie_storyline' , 
	'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg' , 
	'https://www.youtube.com/watch?v=oP7kExN8LFA','2014/01/2')

spider_movice = media.Movie( 'Spider Man', 'Spider Man movie_storyline' , 
	'https://upload.wikimedia.org/wikipedia/en/2/21/Web_of_Spider-Man_Vol_1_129-1.png' , 
	'https://www.youtube.com/watch?v=WfV-0Yv5vNY','2015/01/2')
avengers_movice = media.Movie( 'Avengers: Infinity War ', 'Avengers: Infinity War  movie_storyline' , 
	'https://upload.wikimedia.org/wikipedia/zh/1/18/%E5%BE%A9%E4%BB%87%E8%80%85%E8%81%AF%E7%9B%9F.jpg' , 
	'https://www.youtube.com/watch?v=2tZwt7HADWI','2016/01/2')
captain_movie = media.Movie( 'Captain America', 'Captain America movie_storyline' , 
	'https://upload.wikimedia.org/wikipedia/zh/a/a5/436px-Captain_America_Vol_6_2_Textless.jpg' , 
	'https://www.youtube.com/watch?v=swvzxZjbbfY','2017/01/2')

movies = {toy_movie , avatar_movie , school_rock_movie , spider_movice , avengers_movice , captain_movie}
fresh_tomatoes.open_movies_page(movies)

