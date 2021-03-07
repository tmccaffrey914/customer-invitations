import os
import time
import unittest

from src.constants.exceptions import InvalidCustomerJSON
from src.utils.io import (
    yield_json_from_file,
    yield_lines_from_file_in_batches
)


class TestIO(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.file_path = os.path.join("src", "tests", "resources")

    def test_load_empty_file(self):
        generator_is_empty = True
        for _ in yield_json_from_file(os.path.join(self.file_path, "empty.txt")):
            generator_is_empty = False
        self.assertTrue(generator_is_empty)

    def test_load_large_file(self):
        pre_test = time.time()
        for _ in yield_json_from_file(os.path.join(self.file_path, "large_file.txt")):
            continue
        post_test = time.time()
        execution_time = post_test - pre_test   # Result is in Seconds
        self.assertTrue(execution_time < 1)

    def test_different_batch_sizes(self):
        result_map = {}
        batch_size = 1
        while batch_size <= 10000:
            pre_test = time.time()
            for batch in yield_lines_from_file_in_batches(os.path.join(self.file_path, "large_file.txt"), batch_size):
                batch.count(".")    # Give Some Task that will be Equally Expensive over the course of Entire File
            post_test = time.time()

            result_map[batch_size] = post_test - pre_test   # Result is in Seconds
            batch_size *= 10

        print(result_map)
        self.assertLess(min(result_map.values()), 1)

    def test_load_file_single_line(self):
        counter = 0
        for _ in yield_json_from_file(os.path.join(self.file_path, "single_record.txt")):
            counter += 1
        self.assertEqual(1, counter)

    def test_load_regular_file(self):
        counter = 0
        for _ in yield_json_from_file(os.path.join(self.file_path, "regular.txt")):
            counter += 1

        self.assertGreater(counter, 1)

    def test_load_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            for _ in yield_json_from_file(os.path.join(self.file_path, "does_not_exist.txt")):
                continue

    def test_gappy_file(self):
        counter = 0
        for _ in yield_json_from_file(os.path.join(self.file_path, "gappy.txt")):
            counter += 1
        self.assertGreater(counter, 1)

    def test_file_with_invalid_json(self):
        with self.assertRaises(InvalidCustomerJSON):
            for _ in yield_json_from_file(os.path.join(self.file_path, "not_json.txt")):
                continue
