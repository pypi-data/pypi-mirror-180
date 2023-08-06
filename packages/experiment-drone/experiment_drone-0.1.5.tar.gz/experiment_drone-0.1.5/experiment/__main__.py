"""Console script for experiment."""
import sys
import click


try:
    from . import  __version__
except ImportError:
    __version__ = '0.1.0'

@click.command()
@click.version_option(__version__, '-V', '--version', prog_name='experiment', message='%(prog)s: v%(version)s')
@click.option('-v', '--verbose', count=True)
@click.help_option('-h', '--help')
def main(verbose=None):
    """Console script for experiment."""
    click.echo('Replace this message by putting your code into '
               'experiment.__main__.main')
    click.echo('See click documentation at https://click.palletsprojects.com/')
    return 0


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
