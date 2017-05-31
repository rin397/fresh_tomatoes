import webbrowser

class Movie():

	def __init__(self , movie_title, movie_storyline , movie_post_img_url , movie_youtube_url, start_date):
		print 'init ...'
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_post_img_url
		self.trailer_youtube_url = movie_youtube_url
		self.start_date = start_date

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)



