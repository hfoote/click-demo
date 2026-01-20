import click

# defines the command group
@click.group()
@click.version_option() # adds a --version option to the group
def greeting():
	pass

@greeting.command() # defines a command under the group cli
# options are defined with the option decorator. First argument is the option, 
# second argument (optional) is the variable that click will pass the option to
# in the function. If this isn't specified, click will infer the correct variable by 
# removing leading dashes from the option name. You can set default values and a 
# message to be displayed in the command's help page. 
# For more on options, see https://click.palletsprojects.com/en/stable/options/
@click.option("--count", "n", default=1, help='Number of greetings')
# To add arguments, use the argument decorator. These accept the name of the variable 
# that will be assigned by the argument and passed to the function.
# For more on these, see https://click.palletsprojects.com/en/stable/arguments/
@click.argument("name", type=str)
def hello(n, name):
	"""Greets NAME for a total of COUNT times."""
	for i in range(n):
		click.echo(f"Hello, {name}!")

@greeting.command()
@click.option("--count", "n", default=1, help='Number of goodbyes')
def goodbye(n):
	"""Says goodbye COUNT times."""
	for i in range(n):
		click.echo("Goodbye!")


# You can make sub-groups as well, for example here's a sub-group which saves greetings
# to a file
@greeting.group()
# To allow commands and groups to communicate with each other, 
# click uses Context objects, which keep track of how parent commands are invoked. 
# Here, we'll use this to store the filename we want to store greetings in. This
# makes the context object the first argument of the function. 
@click.pass_context
@click.option(
	"--filename", 
	type=click.File('a'), # For files, click has a special File type to handle I/O
	prompt="Enter a file name to store greetings", # prompt the user for an option.
	prompt_required=True
)
def save(ctx, filename):
	# make sure the context exists as a dict
	ctx.ensure_object(dict)
	# pass the file to the context object
	ctx.obj["FILE"] = filename

# Command that writes greetings to the file
@save.command()
@click.option("--count", "n", default=1, help='Number of greetings')
@click.argument("name", type=str)
@click.pass_context
def writehello(ctx, n, name):
	"""Writes a greeting for NAME to a file for COUNT times"""
	for i in range(n):
		ctx.obj["FILE"].write(f"Hello, {name}!\n")

# Command that writes goodbyes to the file
@save.command()
@click.option("--count", "n", default=1, help='Number of goodbyes')
@click.pass_context
def writegoodbye(ctx, n):
	"""Writes a goodbye to a file for COUNT times"""
	for i in range(n):
		ctx.obj["FILE"].write(f"Goodbye!\n")
