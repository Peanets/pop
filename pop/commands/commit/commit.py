import click
from pop.utils.decorators import project_exists, data_exists

@click.command('commit', short_help='Commit unit step and save data for further transformation')
@click.pass_obj
@project_exists
@data_exists
def cli(ctl):
	data = ctl.get_table('tmp');
	data = ctl.add_table(data)
	pass