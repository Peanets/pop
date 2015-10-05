import pytest
from click.testing import CliRunner

@pytest.fixture(scope='function')
def runner(request):
    return CliRunner(env={'POP_HOME':'.pop','POP_PROJECT_HOME':'project','HOME':''})