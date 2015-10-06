import click
from pop.main import cli
from click.testing import CliRunner
from nose.tools import eq_ as eq
from nose.tools import raises
import os
from utils import create_file, file_exists

def create_file_with_dates():
    with open('hello.csv', 'w') as f:
        f.write('id,name,register_dates\n')
        f.write('12,toto,2015-05-10\n')

def test_import_without_project_set(runner):
    with runner.isolated_filesystem():
        create_file()
        result = runner.invoke(cli, ['import','csv'],input='hello.csv')
        assert 'Data injected' not in result.output
        assert result.exit_code != 0

def test_import(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create','hello'])
    	create_file()
        result = runner.invoke(cli, ['import','csv'], input="hello.csv\n,\n\n")
        project_dir = os.path.join(runner.env['POP_PROJECT_HOME'],'hello')
        project_store_exist = os.path.exists(os.path.join(project_dir,'data/store.h5'))
        
        #assert project_store_exist
        assert 'Data injected' in result.output
        assert result.exit_code == 0

def test_import__with_whitespace(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create','hello'])
        create_file()
        result = runner.invoke(cli, ['import','csv'], input="\rhello.csv\t\n,\n\n")
        project_dir = os.path.join(runner.env['POP_PROJECT_HOME'],'hello')
        project_store_exist = os.path.exists(os.path.join(project_dir,'data/store.h5'))
        
        #assert project_store_exist
        assert 'Data injected' in result.output
        assert result.exit_code == 0

def test_import_with_dates(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create','hello'])
        create_file_with_dates()
        result = runner.invoke(cli, ['import','csv'], input="hello.csv\n,\nregister_dates\n")
        project_dir = os.path.join(runner.env['POP_PROJECT_HOME'],'hello')
        project_store_exist = os.path.exists(os.path.join(project_dir,'data/store.h5'))
        
        #assert project_store_exist
        assert 'Data injected' in result.output
        assert result.exit_code == 0
