from geopy.geocoders import Nominatim
import folium
from math import asin, sqrt, pi, cos


def convert_name_to_coordinates(name: str):
    geolocator = Nominatim(timeout=10, user_agent="fuck i know")
    location = geolocator.geocode(name)
    if location is None:
        name = ",".join(name.split(",")[1:])
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


def convert_coordinates_to_country(coordinates):
    geolocator = Nominatim(timeout=10, user_agent="fuck i know")
    location = geolocator.reverse(coordinates, language="en")
    return str(location)


def parse(films: list, address: str):
    temp = []
    country = address.split(",")[-1].strip()
    for film in films:
        if country in film[1]:
            temp.append(film)
    return temp


def parse_2(films: list, address: str):
    temp = []
    location = address.split(',')[-1:-3:-1]
    for el in location:
        try:
            int(el)
            location = address.split(',')[-1:-2:-1] + address.split(',')[-3:-4:-1]
        except:
            continue
    location.reverse()
    address = ",".join(location).strip()
    for film in films:
        if address in film[1]:
            temp.append(film)
    return temp


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


def get_films():
    coordinates = "49.83826, 24.02324"  # "34.0536909, -118.242766"
    user_address = convert_coordinates_to_country(coordinates)
    user_year = input("Please enter the year: ")
    while True:
        try:
            user_year = int(user_year)
            break
        except ValueError:
            user_year = input("Please enter the year: ")
            continue
    films_in_year = read_data("half_data", user_year)
    films_in_year = parse(films_in_year, user_address)
    if len(films_in_year) > 10:
        films_in_year = parse_2(films_in_year, user_address)
    if len(films_in_year) > 10:
        films_in_year = films_in_year[:10]
    return films_in_year


def create_map(films: list):
    pass

print(main())

