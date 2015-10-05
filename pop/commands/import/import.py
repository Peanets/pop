import click
from pop.main import pass_controller
from pop.exceptions.no_project_error import NoProjectError
from cStringIO import StringIO
from pop.managers.manager_factory import ManagerFactory
from importers.importer_factory import ImporterFactory

@click.command('import', short_help='Import data into datastore')
@click.argument('input_format', required=True, type=str)
@click.pass_obj
def cli(ctl,input_format):
	if not ctl.is_project_set:
		raise NoProjectError()

	importer = ImporterFactory.get_importer(ctl,input_format)
	data = importer.get_data()

	ctl.add_table(data)