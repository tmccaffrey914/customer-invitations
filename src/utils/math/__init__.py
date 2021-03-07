from geopy.distance import great_circle


def calculate_distance_between_two_points(current_location, destination):
    """
    Calculate the distance between two points on the globe using Great Circle measurement.

    :param current_location: (Tuple) Containing the Latitude and Longitude of the Start Point.
    :param destination: (Tuple) Containing the Latitude and Longitude of the Destination,
        Defaults to Intercom Dublin Offices
    :return: (Float) Distance between the two points measured in Kilometers
    """
    return great_circle(current_location, destination).km
