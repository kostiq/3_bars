import json
import requests


def load_data(filepath):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
    return data


def get_biggest_bar(data):
    SeatsCount = []
    for bar in data:
        SeatsCount.append(bar['Cells']['SeatsCount'])
    SeatsCount.sort()
    min = SeatsCount[0]
    for bar in data:
        if min == bar['Cells']['SeatsCount']:
            print ('The bigest bar is: {0}'.format(bar['Cells']['Name']))
            return None


def get_smallest_bar(data):
    SeatsCount = []
    for bar in data:
        SeatsCount.append(bar['Cells']['SeatsCount'])
    SeatsCount.sort()
    min = SeatsCount[-1]
    for bar in data:
        if min == bar['Cells']['SeatsCount']:
            print ('The smallest bar is: {0}'.format(bar['Cells']['Name']))
            return None


def get_closest_bar(data, longitude, latitude):
    distance = dict(name='', coordinates=[], distance=1000)
    for bar in data:
        point = bar['Cells']['geoData']['coordinates']
        dist = get_distance(longitude, latitude, point[0], point[1])
        if dist < distance['distance']:
            distance['name'] = bar['Cells']['Name']
            distance['distance'] = dist

    print ('The closest bar is: {0}'.format(distance['name']))
    return None


def get_distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


if __name__ == '__main__':

    bars = load_data('bars.json')
    latitude = float(input('Input latitude:'))
    longitude = float(input('Input longitude:'))

    get_biggest_bar(bars)
    get_smallest_bar(bars)
    get_closest_bar(bars, longitude, latitude)
