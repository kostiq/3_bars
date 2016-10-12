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
            print (bar['Cells']['Name'])
            return 0


def get_smallest_bar(data):
    SeatsCount = []
    for bar in data:
        SeatsCount.append(bar['Cells']['SeatsCount'])
    SeatsCount.sort()
    min = SeatsCount[-1]
    for bar in data:
        if min == bar['Cells']['SeatsCount']:
            print (bar['Cells']['Name'])
            return 0


def get_closest_bar(data, longitude, latitude):
    distance = dict(name='', coordinates=[], distance=1000)
    for bar in data:
        point = bar['Cells']['geoData']['coordinates']
        dist = get_distance(longitude, latitude, point[0], point[1])
        if dist < distance['distance']:
            distance['name'] = bar['Cells']['Name']
            distance['distance'] = dist

    print (distance['name'])
    return 0


def get_distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


if __name__ == '__main__':

    bars = load_data('bars.json')
    latitude = float(input())
    longitude = float(input())

    get_biggest_bar(bars)
    get_smallest_bar(bars)
    get_closest_bar(bars, longitude, latitude)
