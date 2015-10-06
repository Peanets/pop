from pop.main import cli

def test_pop(runner):
	with runner.isolated_filesystem():
		result = runner.invoke(cli, catch_exceptions=False)
		assert 'ls' in result.output
		assert 'rm' in result.output
		assert result.exit_code == 0