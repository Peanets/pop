import click
import os
import shutil

@click.command('create', short_help='Init a project')
@click.argument('name', required=False, type=str)
@click.pass_obj
def cli(ctl,name):
	if not name:
		name = click.prompt('Please enter a name for your project', type=str, default='default')
	ctl.create_project(name)
	click.echo('Project '+name+' created')

