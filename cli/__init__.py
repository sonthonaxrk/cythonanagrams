import click


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    print('hello world')
