import requests
import sys
import pickle


def get_coordinates(place):

    """

    :param place: Name of the place
    :return: dict: {"lat":latitude, "lng":longitude}
    """
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}"
    key = pickle.load(open("key.p", "rb"))
    url = url.format(place, key)
    response = requests.get(url)
    if response:
        data = response.json()["results"]
        if data:
            location = data[0]["geometry"]["location"]
            return location
        else:
            print("Check spelling and try again.")
    else:
        print("Check your internet connection and try again.")
        exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: gecode.py "<name of the place>". Don\'t miss the quotes if place has '
              'more than one word.')
        exit(0)

    place = sys.argv[1]
    coordinates = get_coordinates(place)
    latitude = coordinates["lat"]
    longitude = coordinates["lng"]
    print("{0}'s Latitude: {1}, Longitude: {2}".format(place, latitude, longitude))