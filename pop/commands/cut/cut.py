import click
from pop.main import pass_controller
from pop.exceptions.no_project_error import NoProjectError
from pop.utils.decorators import transformation

@click.command('cut', short_help='Cut columns in data')
@click.option('--columns','-c', type=str, multiple=True)
@click.pass_obj
@transformation
def cli(ctl,columns):
	data = ctl.get_table()

	for column in columns:
		try:
			del data[column]
		except:
			raise ClickException(column+' not present in data')

	return data
