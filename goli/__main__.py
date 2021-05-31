import click
from goli.example import hello


@click.command(name="")
def main(name: str):

    """Prints a greeting for a giving name."""
    greeting: str = hello(name)
    click.echo(greeting)
