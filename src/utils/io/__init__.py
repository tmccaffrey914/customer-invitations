import json


def yield_json_from_file(file_path):
    """
    Read Lines from a given File that have been converted to a Python Object.

    :param file_path: (String) The Path to the File to Read
    :raises: FileNotFoundError - If the `filename` File doesn't exist
    :yield: (Dictionary/List) Format Lines from the File `filename`
    """
    with open(file_path, 'r') as f:
        while True:
            data = f.readline()
            if not data or data.isspace():
                break
            yield json.loads(data)


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
