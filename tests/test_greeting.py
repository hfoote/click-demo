# In click, tests are handled with the CliRunner, which invokes commands
# as command-line scripts.

from click.testing import CliRunner
from click_demo.cli import greeting
import pytest

def test_hello_greets_correct_person_n_times():
	runner = CliRunner()
	# note anything after the command or group (ie subcommands) are 
	# passed as args to invoke
	result = runner.invoke(greeting, ["hello", "--count", "2", "Hayden"])
	
	assert result.exit_code == 0
	assert result.output == "Hello, Hayden!\n"*2

def test_goodbye_says_bye_n_times():
	runner = CliRunner()
	result = runner.invoke(greeting, ["goodbye", "--count", "3"])
	
	assert result.exit_code == 0
	assert result.output == "Goodbye!\n"*3

@pytest.fixture()
def temp_file(tmp_path):
	return tmp_path / "test.txt"

def test_writehello_saves_greetings(temp_file):
	runner = CliRunner()
	result = runner.invoke(greeting, [
		"save", "--filename", temp_file, 
		"writehello", "--count", "2", "Hayden"
	])
	
	content = temp_file.read_text()
	assert content == "Hello, Hayden!\n"*2

def test_writegoodbye_saves_goodbyes(temp_file):
	runner = CliRunner()
	result = runner.invoke(greeting, [
		"save", "--filename", temp_file, 
		"writegoodbye", "--count", "4"
	])
	
	content = temp_file.read_text()
	assert content == "Goodbye!\n"*4