# -*- coding: utf-8 -*-

import click
from . import version
from . import almond

@click.version_option(version=version.__version__)
@click.group()
def cli():
    pass

@cli.command()
def build():
    click.echo('Building')
    a = almond.Almond()

    for f in a.find_files():
        a.convert(f)

if __name__ == "__main__":
    cli()
