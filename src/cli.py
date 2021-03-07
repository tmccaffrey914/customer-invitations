import click
from src.main_process import find_customers_in_radius
from src.utils.io import (
    yield_json_from_file,
    output_customers_to_file
)
from src.utils.requests import yield_json_from_url


@click.command()
@click.argument("filepath", type=click.Path(exists=True))
@click.option("--output", default="output.txt", help="Output File Location & Name")
@click.option("--radius", default="100", type=click.INT, help="Number of Kilometers Radius Around Dublin to Invite")
def from_file(filepath, output, radius):
    """
    Formulate a List of Customers within 100km from the Dublin Office.

    You should provide a FilePath to the customer data file as an argument.

    Example Usage:
    create-invite-list-from-file path/to/customers.txt --output ../../invitees.txt
    """
    matching_customers = find_customers_in_radius(filepath, yield_json_from_file, radius=radius)
    output_customers_to_file(output, matching_customers)
    click.echo(f"Customer Invite List Outputted at [{output}]")


@click.command()
@click.argument("url", default="https://s3.amazonaws.com/intercom-take-home-test/customers.txt")
@click.option("--output", default="output.txt", help="Output File Location & Name")
@click.option("--radius", default="100", type=click.INT, help="Number of Kilometers Radius Around Dublin to Invite")
def from_url(url, output, radius):
    """
    Formulate a List of Customers within 100km from the Dublin Office.

    You may provide a URL to retrieve the customer data from, otherwise we default to:
    https://s3.amazonaws.com/intercom-take-home-test/customers.txt

    Example Usage:
    create-invite-list https://s3.amazonaws.com/intercom-take-home-test/customers.txt
    """
    matching_customers = find_customers_in_radius(url, yield_json_from_url, radius=radius)
    output_customers_to_file(output, matching_customers)
    click.echo(f"Customer Invite List Outputted at [{output}]")
