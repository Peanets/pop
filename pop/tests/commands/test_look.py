import click
from pop.main import cli
from click.testing import CliRunner
from nose.tools import eq_ as eq
from nose.tools import raises
import os
from utils import create_project_with_data

@create_project_with_data
def test_look_data(runner):
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
