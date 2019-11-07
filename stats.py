import requests
import sys
import time

# TODO
# 1. Add GUI to accept user input - origin, destination, time windows etc.
# 2. Allow user to export output into a csv -- advanced
#    can be done by writing output to a text file and a function that reads from this
#    text file and writes it to a csv
#
# 3. Add google maps autocomplete to allow user to select locations instead of asking him
#    for coordinates


def get_data(url):
    response = requests.get(url)
    if response:
        data = response.json()
        if data["rows"]:
            elements = data["rows"][0]["elements"][0]
            return elements
        return "Invalid coordinates. Check again."
    return ""


def get_times(place1, place2):
    """

    :param place1: comma separated latitude longitude numbers of origin
    :param place2: comma separated latitude longitude numbers of destination
    :return: estimated time of travel from origin to destination
    """
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?&origins=" + place1 + "&destinations="+ place2
    key = ""
    data = get_data(url+key)
    if data:
        t = data["duration"]["text"]
        return t
    return "Error. Try later."


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: stats.py <lat1,long1> <lat2,long2> without the angular brackets")
        exit(0)
    INTERVAL = 30
    stop = 0
    while stop < 150:
        origin = sys.argv[1]
        # "40.764722,-111.842330"
        destination = sys.argv[2]
        # "40.757659,-111.865315"
        t = get_times(origin, destination)
        print(t)
        time.sleep(INTERVAL)
        stop += INTERVAL
