import click
from pop.main import pass_controller
from click import ClickException
from pop.exceptions.no_data_error import NoDataError

@click.command('remove', short_help='Remove a project')
@click.argument('project_name', required=False)
@click.pass_obj
def cli(ctl,project_name):
	if not project_name:
		project_name = ctl.project_name
	
	click.confirm(text='Are you sure to remove '+project_name+' ?')

	ctl.remove_project(project_name)
	click.echo('Project '+project_name+' removed')