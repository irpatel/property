import click
from cli import cli

@click.command()
def main():
    cli()

if __name__ == '__main__':
    main()
