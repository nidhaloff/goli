import click
from goli.example import hello


@click.command(name="")
def cli(name: str) -> None:

    """Prints a greeting for a giving name example."""
    greeting: str = hello(name)
    click.echo(greeting)
