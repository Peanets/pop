from click import ClickException

class InputFormatError(ClickException):

	def __init__(self):
		self.message = 'Input format not recognized'