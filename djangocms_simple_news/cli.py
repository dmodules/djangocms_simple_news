# -*- coding: utf-8 -*-

"""Console script for djangocms_simple_news."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for djangocms_simple_news."""
    click.echo("Replace this message by putting your code into "
               "djangocms_simple_news.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
