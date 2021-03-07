from src.constants.locations import DUBLIN_OFFICE
from src.utils.math import calculate_distance_between_two_points


def find_customers_in_radius(resource, load_customer_info, location=DUBLIN_OFFICE, radius=100):
    for customer in load_customer_info(resource):
        customer_location = (customer.get("latitude"), customer.get("longitude"))

        if None in customer_location:
            user_id = customer.get("user_id")
            print(f"[ERROR] Missing Location Data for User: [{user_id}]")

        customer_is_in_range = calculate_distance_between_two_points(customer_location, location) < radius

        if customer_is_in_range:
            yield customer.get("user_id"), customer.get("name")
