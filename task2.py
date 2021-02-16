from geopy.geocoders import Nominatim
from math import asin, sqrt, pi, cos


def convert_name_to_coordinates(name: str):
    geolocator = Nominatim(timeout=10, user_agent="fuck i know")
    location = geolocator.geocode(name)
    try:
        return location.latitude, location.longitude
    except AttributeError:
        return False


def haversin(lat1, lon1, lat2, lon2):
    """
    r = 6371,00 km
    """
    r = 6371
    lat1, lat2 = lat1*pi/180, lat2*pi/180
    lon1, lon2 = lon1*pi/180, lon2*pi/180
    arg = (1-cos(lat2-lat1))/2 + cos(lat1)*cos(lat2)*(1-cos(lon2-lon1))/2
    d = 2*r*asin(sqrt(arg))
    return d


def parse(line: list, coordinates: tuple):
    pass


def read_data(path: str, date: int):
    result = []
    with open(path, encoding="utf-8", errors="ignore") as file:
        for _ in range(14):
            file.readline()
        for line in file:
            line = line.split('\t')
            index = line[0].find('(')
            try:
                year = int(line[0][index+1: index+5])
            except ValueError:
                continue
            if year == date:
                name = line[0][:index-1]
                name = name.replace('''"''', "")
                if line[-1][0] == '(':
                    location_of_film = line[-2].strip()
                else:
                    location_of_film = line[-1].strip()
                result.append((name, location_of_film))
    return result


def main():
    user_year = input("Please enter the year: ")
    while True:
        try:
            user_year = int(user_year)
            break
        except ValueError:
            user_year = input("Please enter the year: ")
            continue
    films_in_year = read_data("half_data", user_year)



# read_data("half_data", 2006)
# haversin(49.83826, 24.02324, 34.0536909, -118.242766)
main()
