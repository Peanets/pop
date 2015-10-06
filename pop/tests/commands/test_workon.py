import click
from pop.main import cli
from click.testing import CliRunner
from nose.tools import eq_ as eq
from nose.tools import raises
import os

def test_workon(runner):
	with runner.isolated_filesystem():
		result = runner.invoke(cli, ['create', 'toto'], catch_exceptions=False)
		result = runner.invoke(cli, ['create', 'tutu'], catch_exceptions=False)
		result = runner.invoke(cli, ['workon', 'toto'], catch_exceptions=False)
		assert result.exit_code==0

def test_workon_on_wrong_project(runner):
	with runner.isolated_filesystem():
		result = runner.invoke(cli, ['create', 'toto'], catch_exceptions=False)
		result = runner.invoke(cli, ['workon', 'titi'])
		assert result.exit_code!=0