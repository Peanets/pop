import click
from pop.main import pass_controller
from pop.exceptions.no_project_error import NoProjectError

@click.command('ls', short_help='List all projects')
@click.pass_obj
def cli(ctl):
	projects = ctl.get_projects();
	for project in projects:
		click.echo(project['name'])