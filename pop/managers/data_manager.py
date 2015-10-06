import pandas as pd
from pop.exceptions.no_data_error import NoDataError
import click

class DataManager(object):

	def __init__(self,ctl):
		self.ctl=ctl
		self._is_empty=True
		self._load_database()

	def _load_database(self):
		try:
			self.database = pd.HDFStore(self.ctl.project_dir+'/data/store.h5')
			self._is_empty=False
		except:
			pass

	def close(self):
		try:
			self.database.close()
		except:
			pass

	def get_table(self,table_name):
		table_name = table_name.strip()
		if table_name in self.database:
			return self.database[table_name]
		else:
			raise NoDataError()

	def add_table(self,df,table_name='default'):
		df.to_hdf(self.ctl.project_dir+'/data/store.h5',table_name)

	def list_tables(self):
		pass

	def is_empty(self):
		return self._is_empty

	def describe_tables(self):
		pass

	def remove_table(self):
		pass