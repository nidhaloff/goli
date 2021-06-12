import click
from cookiecutter.main import cookiecutter
from goli import options
from goli.cookiecutters import CookieCutterTemplates


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--language",
    "-l",
    default="python",
    type=click.Choice(options.languages),
    help="programming language to use",
)
@click.option(
    "--topic",
    "-t",
    default="package",
    type=click.Choice(options.topics),
    help="topic of the template you want to create (e.g data-science)",
)
def new(language: str, topic: str) -> None:
    """
    Generate new boilerplate code for your project
    """

    template = CookieCutterTemplates.get_template(language, topic)
    click.secho(f"Template: {template} will be used.", fg="green")
    cookiecutter(template)
    click.echo("Done.")


@cli.command()
def languages() -> None:
    """
    Show all supported programming languages
    """
    for lang in options.languages:
        click.secho(lang, fg="yellow", blink=True, bold=True)


@cli.command()
def topics() -> None:
    """
    Show all supported topics.
    This includes specific libs or frameworks that you may want to use
    """
    for topic in options.topics:
        click.secho(topic, fg="yellow", blink=True, bold=True)
