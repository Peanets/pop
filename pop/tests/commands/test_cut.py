from pop.main import cli
from utils import create_project_with_data

@create_project_with_data
def test_cut(runner):
	result = runner.invoke(cli, ['cut','-c','value'], catch_exceptions=False)
	
	assert 'value' not in result.output
	assert result.exit_code == 0

@create_project_with_data
def test_cut_with_wrong_column(runner):
	result = runner.invoke(cli, ['cut','-c','valuf'])
	
	assert 'not present in data' not in result.output
	assert result.exit_code != 0

def test_cut_without_project(runner):
	with runner.isolated_filesystem():
		result = runner.invoke(cli, ['cut','-c','value'])
		assert 'No Project Selected' in result.output
		assert result.exit_code != 0

def test_cut_without_data(runner):
	with runner.isolated_filesystem():
		result = runner.invoke(cli,['create','toto']);
		result = runner.invoke(cli, ['cut','-c','value'])
		assert 'No Data Imported' in result.output
		assert result.exit_code != 0