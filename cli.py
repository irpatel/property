import click
from clients.email import send_email
from clients.file_generator import generate_excel
from utils.db_setup import insert_utility_record, get_utility_records

@click.group()
def cli():
    pass

@cli.command()
@click.option('--api-key', prompt='SendGrid API Key', help='Your SendGrid API Key')
def send_email(api_key):
    # Implement sending email functionality using send_email function
    pass

@cli.command()
def generate_file():
    # Implement generating Excel file functionality using generate_excel function
    pass

@cli.command()
def add_utility_record():
    utility_type = input("Enter utility type: ")
    month = input("Enter month: ")
    amount = float(input("Enter amount: "))
    insert_utility_record(utility_type, month, amount)
    print("Utility record added successfully!")

@cli.command()
def show_utility_records():
    records = get_utility_records()
    if records:
        for record in records:
            print(record)
    else:
        print("No utility records found.")
