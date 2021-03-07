from src.constants.locations import DUBLIN_OFFICE
from src.utils.math import calculate_distance_between_two_points


def find_customers_in_radius(resource, load_customer_info, location=DUBLIN_OFFICE, radius=100):
    """
    This function combines all of the necessary information, and informs us which customers live near a given Location.

    :param resource: (String) This can be either a URL or a File Path where we can find relevant Customer Info
    :param load_customer_info: (Function) This is a Function which instructs us how to Load the Customer Info
    :param location: (Tuple) A Tuple containing the Latitude and Longitude of the Location around which we want to
        search
    :param radius: (Integer) The Range around the Location we wish to seach in.
    :yield: (Tuple) User ID and Customer Name of Individuals that are within the Radius
    """
    for customer in load_customer_info(resource):
        customer_location = (customer.get("latitude"), customer.get("longitude"))

        if None in customer_location:
            user_id = customer.get("user_id")
            print(f"[ERROR] Missing Location Data for User: [{user_id}]")

        customer_is_in_range = calculate_distance_between_two_points(customer_location, location) < radius

        if customer_is_in_range:
            yield customer.get("user_id"), customer.get("name")
