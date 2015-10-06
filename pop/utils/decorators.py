from pop.exceptions.no_project_error import NoProjectError
from pop.exceptions.no_data_error import NoDataError
import click

def project_exists(command_function):
	def inner_function(ctl,*args,**kwargs):
		if not ctl.is_project_set:
			raise NoProjectError()
		return command_function(ctl,*args,**kwargs)
	return inner_function

def data_exists(command_function):
	def inner_function(ctl,*args,**kwargs):
		if ctl.has_data():
			raise NoDataError()
		return command_function(ctl,*args,**kwargs)
	return inner_function

def transformation(command_function):
	def inner_function(ctl,*args,**kwargs):
		if not ctl.is_project_set:
			raise NoProjectError()
		if ctl.has_data():
			raise NoDataError()
		data = command_function(ctl,*args,**kwargs)
		ctl.add_table(data,'tmp')
		click.echo(data.__str__())

	return inner_function