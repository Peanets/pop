import pandas as pd

class CsvImporter(object):

	def __init__(self,ctl,file_options):
		self.ctl = ctl
		self.file_options = file_options

	def get_data(self):
		path = self.file_options['path']
		del self.file_options['path']
		return pd.read_csv(path,**self.file_options)
		