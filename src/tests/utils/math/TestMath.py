import unittest
from src.utils.math import calculate_distance_between_two_points
from src.constants.locations import (
    BELFAST,
    CORK,
    DUBLIN_OFFICE,
    GALWAY,
    LONDON,
    NY,
    SYDNEY
)


class TestIO(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.local_degree_of_error_in_km = 2
        cls.remote_degree_of_error_in_km = 50

    def test_calculate_distance_belfast_dublin(self):
        expected_distance = 141
        # https://www.trippy.com/distance/Dublin-to-Belfast-United-Kingdom

        calculated_distance = calculate_distance_between_two_points(BELFAST, DUBLIN_OFFICE)
        self.assertAlmostEqual(expected_distance, calculated_distance, delta=self.local_degree_of_error_in_km)

    def test_calculate_distance_cork_dublin(self):
        expected_distance = 221
        # https://www.trippy.com/distance/Dublin-to-Cork

        calculated_distance = calculate_distance_between_two_points(CORK, DUBLIN_OFFICE)
        self.assertAlmostEqual(expected_distance, calculated_distance, delta=self.local_degree_of_error_in_km)

    def test_calculate_distance_galway_dublin(self):
        expected_distance = 187
        # https://www.trippy.com/distance/Dublin-to-Galway

        calculated_distance = calculate_distance_between_two_points(GALWAY, DUBLIN_OFFICE)
        self.assertAlmostEqual(expected_distance, calculated_distance, delta=self.local_degree_of_error_in_km)

    def test_calculate_distance_ny_london(self):
        expected_distance = 5586
        # https://www.trippy.com/distance/New-York-City-to-London

        calculated_distance = calculate_distance_between_two_points(NY, LONDON)
        self.assertAlmostEqual(expected_distance, calculated_distance, delta=self.remote_degree_of_error_in_km)

    def test_calculate_distance_sydney_dublin(self):
        expected_distance = 17211
        # https://www.trippy.com/distance/Dublin-to-Sydney

        calculated_distance = calculate_distance_between_two_points(SYDNEY, DUBLIN_OFFICE)
        self.assertAlmostEqual(expected_distance, calculated_distance, delta=self.remote_degree_of_error_in_km)
