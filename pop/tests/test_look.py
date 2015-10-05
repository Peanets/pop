import click
from pop.main import cli
from click.testing import CliRunner
from nose.tools import eq_ as eq
from nose.tools import raises
import os

def create_file():
	with open('hello.csv', 'w') as f:
		f.write('id,name\n')
		f.write('12,toto\n')
        f.close()

def file_exists(path):
	boolean = os.path.exists(path)
	return boolean

def test_look_data(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create','hello'], catch_exceptions=False)
        create_file()
        result = runner.invoke(cli, ['import','csv'], input="hello.csv\n,\n\n", catch_exceptions=False)
        result = runner.invoke(cli, ['look'], catch_exceptions=False)

        assert 'id' in result.output
        assert result.exit_code == 0

def test_look_data_without_project(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['look'])
        assert result.exit_code != 0

def test_look_data_without_data(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create','hello'], catch_exceptions=False)
        result = runner.invoke(cli, ['look'])
        assert result.exit_code != 0
