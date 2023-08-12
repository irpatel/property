import click
from db_setup import create_database, create_utility_records, update_utility_records
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@click.group()
def cli():
    pass

@cli.command(help="Add a utility record")
@click.option('--utility-type', type=click.Choice(['internet', 'electricity', 'hydro', 'water', 'sewage']), prompt='Utility Type', help='Type of utility (options: internet, electricity, hydro, water, sewage)')
@click.option('--year', type=int, prompt='Year', help='Year for the utility record')
@click.option('--month', type=click.Choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']), prompt='Month', help='Month for the utility record')
@click.option('--amount', prompt='Amount', type=float, help='Amount of the utility bill')
def add_utility_record(utility_type, year, month, amount):
    create_database()  # Create the database
    create_utility_records()  # Create the table if it doesn't exist
    full_month = f"{month} {year}"
    update_utility_records(utility_type, full_month, amount)
    logger.info("Utility record added successfully!")

@cli.command(help="Update a utility record")
@click.option('--utility-type', type=click.Choice(['internet', 'electricity', 'hydro', 'water', 'sewage']), prompt='Utility Type', help='Type of utility (options: internet, electricity, hydro, water, sewage)')
@click.option('--year', type=int, prompt='Year', help='Year for the utility record')
@click.option('--month', type=click.Choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']), prompt='Month', help='Month for the utility record')
@click.option('--amount', prompt='Updated Amount', type=float, help='Updated amount of the utility bill')
def update_utility_record(utility_type, year, month, amount):
    full_month = f"{month} {year}"
    update_utility_records(utility_type, full_month, amount)
    logger.info("Utility record updated successfully!")

if __name__ == '__main__':
    cli(obj={})