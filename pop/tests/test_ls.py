import click
from pop.main import cli
from click.testing import CliRunner
from nose.tools import eq_ as eq
from nose.tools import raises
import os

def test_ls(runner):
	with runner.isolated_filesystem():
		result = runner.invoke(cli, ['create', 'toto'], catch_exceptions=False)
		result = runner.invoke(cli, ['ls'], catch_exceptions=False)
		assert 'toto' in result.output
		assert result.exit_code==0