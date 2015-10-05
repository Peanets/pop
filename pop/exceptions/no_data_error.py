from click import ClickException

class NoDataError(ClickException):

	def __init__(self):
		self.message = 'No Data Imported'