from click import ClickException

class NoProjectError(ClickException):
	
	def __init__(self):
		self.message = 'No Project Selected'