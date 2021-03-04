from click.testing import CliRunner
from app import change_func

def test_change():
  runner = CliRunner()
  result = runner.invoke(change_func, ['--change', '0.41'])
  assert result.exit_code == 0
  assert '1 penny' in result.output
  assert '1 nickel' in result.output
  assert '1 dime' in result.output
  assert '1 quarter' in result.output
  