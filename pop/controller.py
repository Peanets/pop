from managers.project_manager import ProjectManager
from managers.data_manager import DataManager
import click
import os

class Controller(object):

    def __init__(self, ctx, home, pop_home, project_home, verbose):
        self.verbose = verbose
        self.pop_home = os.path.join(home,pop_home)
        self.project_home = os.path.join(home,project_home)
        self.project_manager = ProjectManager(self)
        self.load_project()
        self.data_manager = DataManager(self)
        ctx.call_on_close(self.close)

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)

    def reset_project(self):
        self.project_manager.reset_project()

    def remove_project(self,project_name):
        self.project_manager.remove_project(project_name)

    def create_project(self,name):
        self.project_manager.create_project(name)

    def load_project(self):
        self.project_manager.load_project()

    def switch_project(self,project_name):
        self.project_manager.switch_project(project_name)

    def get_projects(self):
        return self.project_manager.get_projects()

    def save_tmp_table(self,data):
        self.data_manager.add_table(data,table_name='tmp')
        
    def add_table(self,data,table_name='default'):
    	#table_name = click.prompt('Name your data', type=str, default='default')
    	self.data_manager.add_table(data,table_name)
    	click.echo('Data injected')

    def get_table(self,table_name='default'):
    	return self.data_manager.get_table(table_name)

    def has_data(self):
        return self.data_manager.is_empty();

    def close(self):
    	self.data_manager.close()