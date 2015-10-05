from big_csv_importer import BigCsvImporter
from csv_importer import CsvImporter
from pop.exceptions.input_format_error import InputFormatError
import click

class ImporterFactory(object):

	@classmethod
	def get_importer(self,ctl,input_format):
		if input_format=='csv':
			file_options = self.prompt_for_csv()
			return CsvImporter(ctl,file_options)
		else:
			raise InputFormatError()

	@classmethod
	def prompt_for_csv(self):
		file_format = {}

		path = click.prompt('Where is your file ?', type=str)
		sep = click.prompt('What is the seperator ?', type=str)
		dates = click.prompt('What are the column dates ?', type=str, default='')

		file_format['path']=path.strip()
		file_format['sep']=sep

		if len(dates) != 0:
			file_format['parse_dates']=[dates]

		return file_format