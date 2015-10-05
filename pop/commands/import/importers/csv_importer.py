import pandas as pd

class CsvImporter(object):

	def __init__(self,ctl,file_format):
		self.ctl = ctl
		self.file_format = file_format

	def get_data(self):
		path = self.file_format['path']
		del self.file_format['path']
		return pd.read_csv(path,**self.file_format)
		