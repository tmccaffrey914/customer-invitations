import os
import unittest
from unittest import mock

from src.utils.requests import yield_json_from_url


# This method will be used by the mock to replace requests.get:
def mocked_requests_get(*args, **kwargs):
    # This Class Mocks the Response Object:
    class MockResponse:
        def __init__(self, body_file, status_code):
            self.body_file = body_file
            self.encoding = "utf-8"
            self.status_code = status_code

        def iter_lines(self, decode_unicode=True):
            with open(self.body_file) as f:
                return f.readlines()

    # The URLs that our Tests try to hit:
    if args[0] == "https://someurl.com/regular.txt":
        return MockResponse(os.path.join("resources", "regular.txt"), 200)
    elif args[0] == "https://someurl.com/large_file.txt":
        return MockResponse(os.path.join("resources", "large_file.txt"), 200)
    elif args[0] == "https://someurl.com/empty.txt":
        return MockResponse(os.path.join("resources", "empty.txt"), 200)
    elif args[0] == "https://someurl.com/single_record.txt":
        return MockResponse(os.path.join("resources", "single_record.txt"), 200)
    elif args[0] == "https://someurl.com/gappy.txt":
        return MockResponse(os.path.join("resources", "single_record.txt"), 200)
    else:
        return MockResponse(None, 404)


class TestRequests(unittest.TestCase):
    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_regular_request(self, mock_get):
        for line in yield_json_from_url("https://someurl.com/regular.txt"):
            self.assertTrue(isinstance(line, dict))
            break

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_large_file_request(self, mock_get):
        count = 0
        for line in yield_json_from_url("https://someurl.com/large_file.txt"):
            self.assertTrue(isinstance(line, dict))
            if count > 99:
                break

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_empty_file_request(self, mock_get):
        for line in yield_json_from_url("https://someurl.com/empty.txt"):
            self.assertEqual(line, None)

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_single_record_request(self, mock_get):
        for line in yield_json_from_url("https://someurl.com/single_record.txt"):
            self.assertTrue(isinstance(line, dict))

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_gappy_request(self, mock_get):
        for line in yield_json_from_url("https://someurl.com/single_record.txt"):
            self.assertTrue(isinstance(line, dict))
