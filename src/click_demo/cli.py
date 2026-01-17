import click

# defines the command group
@click.group()
@click.version_option() # adds a --version option to the group
def cli():
	pass

@cli.command() # defines a command under the group cli
# options are defined with the option decorator. First argument is the option, 
# second argument (optional) is the variable that click will pass the option to
# in the function. If this isn't specified, click will infer the correct variable by 
# removing leading dashes from the option name. You can set default values and a 
# message to be displayed in the command's help page. 
# For more on options, see https://click.palletsprojects.com/en/stable/options/
@click.option("--count", "n", default=1, help='Number of greetings')
# to add arguments, use the argument decorator. For more on these, see 
# https://click.palletsprojects.com/en/stable/arguments/
@click.argument("name", type=str)
def greeting(n, name):
	"""Greets NAME for a total of COUNT times."""
	for i in range(n):
		click.echo(f"Hello, {name}!")
