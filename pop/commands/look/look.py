import click
from pop.main import pass_controller
from pop.managers.manager_factory import ManagerFactory
from pop.exceptions.no_project_error import NoProjectError

@click.command('look', short_help='Look into data')
@click.argument('table_name', required=False, type=str, default='default')
@click.pass_obj
def cli(ctl,table_name):
	if not ctl.is_project_set:
		raise NoProjectError()
	data = ctl.get_table(table_name)
	print data