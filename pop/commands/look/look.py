import click
from pop.main import pass_controller
from pop.exceptions.no_project_error import NoProjectError
from pop.utils.decorators import project_exists, data_exists

@click.command('look', short_help='Look into data')
@click.argument('table_name', required=False, type=str, default='default')
@click.pass_obj
@project_exists
@data_exists
def cli(ctl,table_name):
	data = ctl.get_table(table_name)

	click.echo(data.__str__())