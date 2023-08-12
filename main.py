import click
from cli import cli

@click.command()
def main():
    cli(obj={})

if __name__ == '__main__':
    main()
