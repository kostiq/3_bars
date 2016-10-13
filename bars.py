import json
import requests
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    return sorted(data, key=lambda data: data['Cells']['SeatsCount'])[-1]['Cells']['Name']


def get_smallest_bar(data):
    return sorted(data, key=lambda data: data['Cells']['SeatsCount'])[0]['Cells']['Name']


def get_closest_bar(data, longitude, latitude):
    closest = data[0]
    for bar in data:
        closest_dist = get_distance(
            longitude, latitude, closest['Cells']['geoData']['coordinates'])
        temp_dist = get_distance(
            longitude, latitude, bar['Cells']['geoData']['coordinates'])
        if temp_dist < closest_dist:
            closest = bar
    return closest['Cells']['Name']


def get_distance(x1, y1, point):
    return (x1 - point[0])**2 + (y1 - point[1])**2


if __name__ == '__main__':

    bars = load_data('bars.json')
    try:
        latitude = float(input('Input latitude:'))
    except ValueError:
        latitude = None
    try:
        longitude = float(input('Input longitude:'))
    except ValueError:
        longitude = None

    if (latitude or longitude) is None:
        print ('Incorrect input data!')
    else:
        print ('The biggest bar is: {0}'.format(get_biggest_bar(bars)))
        print ('The smallest bar is: {0}'.format(get_smallest_bar(bars)))
        print ('The closest bar is: {0}'.format(
            get_closest_bar(bars, longitude, latitude)))
