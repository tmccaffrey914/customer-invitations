import json
from src.constants.exceptions import InvalidCustomerJSON


def yield_json_from_file(file_path):
    """
    Read Lines from a given File that have been converted to a Python Object.

    :param file_path: (String) The Path to the File to Read
    :raises: FileNotFoundError - If the `filename` File doesn't exist
    :yield: (Dictionary/List) Format Lines from the File `filename`
    """
    with open(file_path, 'r') as f:
        for line in f:
            if line and not line.isspace():
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as e:
                    raise InvalidCustomerJSON("Customer JSON is Invalid") from e


def yield_lines_from_file_in_batches(file_path, batch_size=1024):
    """
    Read Lines from a given File in Batches of a given Size.

    :param file_path: (String) The Path to the File to Read
    :param batch_size: (Integer) the number of Lines to return in each iteration
    :raises: FileNotFoundError - If the `filename` File doesn't exist
    :yield: (String) `batch_size` number of Lines from the File `filename`
    """
    with open(file_path, 'r') as f:
        while True:
            data = f.readlines(batch_size)
            if not data:
                break
            yield data


def output_customers_to_file(output_file, customers):
    """
    Output Customer Names and User ID's as a CSV File.

    :param output_file: (String) Filepath with Filename to Output the CSV as
    :param customers: (Iterable) Object containing Tuples with (User ID, Customer Name)
    :return: None
    """
    with open(output_file, 'w', encoding="utf-8") as f:
        print("user_id, name ", file=f)
        for user_id, customer_name in customers:
            print(f"{user_id}, {customer_name} ", file=f)
