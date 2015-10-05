import click
from pop.main import cli
from click.testing import CliRunner
from nose.tools import eq_ as eq
from nose.tools import raises
import os

def file_exists(path):
	boolean = os.path.exists(path);
	return boolean

def test_rm_command(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create', 'toto'])
        result = runner.invoke(cli, ['rm'], input="y")
        assert result.exit_code == 0

def test_rm_command_with_name(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create', 'toto'])
        result = runner.invoke(cli, ['create', 'tutu'])
        result = runner.invoke(cli, ['rm','toto'], input="y")
        assert result.exit_code == 0

def test_exception_rm_command(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['create', 'toto'], catch_exceptions=False)
        result = runner.invoke(cli, ['create', 'tutu'], catch_exceptions=False)

        context_file = runner.env['POP_HOME']+'/context.txt'
        toto_project_dir = runner.env['POP_PROJECT_HOME']+'/'+'toto'
        toto_pop_dir = runner.env['POP_HOME']+'/'+'toto'
        tutu_project_dir = runner.env['POP_PROJECT_HOME']+'/'+'tutu'
        tutu_pop_dir = runner.env['POP_HOME']+'/'+'tutu'

        with open(context_file,'r+') as f:
            project_name = f.read()
            assert project_name == 'tutu'

        result = runner.invoke(cli, ['rm', 'momo'], input='y', catch_exceptions=False)

        assert "doesn't exist" in result.output
        assert result.exit_code != 0
