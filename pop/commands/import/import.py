import click
from pop.main import pass_controller
from pop.exceptions.no_project_error import NoProjectError
from importer_factory import ImporterFactory
from pop.utils.decorators import project_exists 

@click.command('import', short_help='Import data into datastore')
@click.argument('source', required=True, type=click.Choice(['csv']), default='csv')
@click.pass_obj
@project_exists
def cli(ctl,source):
	importer = ImporterFactory.get_importer(ctl,source)
	data = importer.get_data()

	ctl.add_table(data)