import click
from pop.main import cli
from click.testing import CliRunner
from nose.tools import eq_ as eq
from nose.tools import raises
import os

def setup():
    global PROJECT_NAME;
    PROJECT_NAME = 'toto'

def test_create_command(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create', PROJECT_NAME], catch_exceptions=False)
        project_dir = runner.env['POP_PROJECT_HOME']+'/'+PROJECT_NAME
        pop_dir = runner.env['POP_HOME']+'/'+PROJECT_NAME
        context_file = runner.env['POP_HOME']+'/context.txt'

        project_dir_exists = os.path.exists(project_dir)
        pop_dir_exists = os.path.exists(pop_dir)
        context_file_exists = os.path.exists(context_file)
       
        with open(context_file,'r') as f:
            project_name = f.read()
            assert project_name == 'toto'

        assert project_dir_exists
        assert pop_dir_exists
        assert context_file_exists

    assert result.exit_code == 0

def test_without_env_variables(runner):
    runner = CliRunner(env={'HOME':''})
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create'], input=PROJECT_NAME, catch_exceptions=False)
        print result.output
        assert result.exit_code==0

def test_valid_name(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create',PROJECT_NAME], catch_exceptions=False)
        assert result.exit_code == 0
        result = runner.invoke(cli, ['create'],input=PROJECT_NAME)
        assert result.exit_code != 0

def test_project_structure(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create'], input=PROJECT_NAME, catch_exceptions=False)
        project_dir = os.path.join(runner.env['POP_PROJECT_HOME'],PROJECT_NAME)
        data_folder_exist = os.path.exists(os.path.join(project_dir,'data'))
        assert data_folder_exist
        assert result.exit_code == 0
