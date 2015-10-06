from pop.main import cli
from click.testing import CliRunner

def create_file():
	with open('hello.csv', 'w') as f:
		f.write('id,name,register_dates,value\n')
		f.write('12,toto,2015-05-10,25\n')
		f.write('13,titi,2014-06-10,26\n')
		f.write('13,titu,2013-06-10,29\n')
        f.close()
        
def file_exists(path):
	boolean = os.path.exists(path)
	return boolean

def create_project_with_data(test_function):
	def inner_function(runner):
		with runner.isolated_filesystem():
			result = runner.invoke(cli, ['create','default'])
			create_file()
			result = runner.invoke(cli, ['import','csv'],input="hello.csv\n,\n\n")
			test_function(runner)
	return inner_function