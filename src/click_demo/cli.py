import click

# defines the command group
@click.group()
def cli():
	pass

@cli.command() # defines a command under the group cli
# options are defined with the option decorator. First argument is the option, 
# second argument (optional) is the variable that click will pass the option to
# in the function. If this idn't specified, click will infer the correct variable by 
# removing leading dashes from the option name. You can set default values and a 
# message to be displayed in the command's help page. 
@click.option('--count', 'n', default=1, help='Number of greetings')
@click.option('--name', help="The person to greet")
def greeting(n, name):
	"""Greets NAME for a total of COUNT times."""
	for i in range(n):
		if name is not None:
			click.echo(f"Hello, {name}!")
		else:
			click.echo(f"Hello!")