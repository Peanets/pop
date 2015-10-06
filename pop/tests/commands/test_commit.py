from pop.main import cli
from utils import create_project_with_data

@create_project_with_data
def test_commit(runner):
	result = runner.invoke(cli, ['cut','-c','register_dates'])
	result = runner.invoke(cli, ['commit'], catch_exceptions=False)
	result = runner.invoke(cli, ['look'], catch_exceptions=False)
	assert 'register_dates' not in result.output
	assert result.exit_code == 0