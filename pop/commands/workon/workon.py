import click
from pop.main import pass_controller
from pop.exceptions.no_project_error import NoProjectError

@click.command('workon', short_help='Workon on a project')
@click.argument('project_name', required=True, type=str)
@click.pass_obj
def cli(ctl,project_name):
	ctl.switch_project(project_name);
	click.echo('Working on project '+project_name)