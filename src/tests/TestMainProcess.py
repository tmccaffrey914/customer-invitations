import unittest
from src.main_process import find_customers_in_radius


class TestMainProcess(unittest.TestCase):
    def test_find_customer_in_radius(self):
        def return_a_customer(throwaway):
            return [{"latitude": "54.0894797", "user_id": 8, "name": "Eoin Ahearn", "longitude": "-6.18671"}]

        for _, customer_name in find_customers_in_radius("a/dummy/path", return_a_customer):
            self.assertEqual(customer_name, "Eoin Ahearn")

    def test_find_customer_not_in_radius(self):
        def return_a_customer(throwaway):
            return [{"latitude": "54.0894797", "user_id": 8, "name": "Eoin Ahearn", "longitude": "-6.18671"}]

        generator_is_empty = True
        for _, customer_name in find_customers_in_radius("a/dummy/path", return_a_customer, radius=1):
            generator_is_empty = False
        self.assertTrue(generator_is_empty)
