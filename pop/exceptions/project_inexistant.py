from click import ClickException

class ProjectInexistant(ClickException):
	
	def __init__(self):
		self.message = "The project mentionned doesn't exist"