import json
import os
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    return min(data, key=lambda data: data['Cells']['SeatsCount'])['Cells']['Name']


def get_smallest_bar(data):
    return max(data, key=lambda data: data['Cells']['SeatsCount'])['Cells']['Name']


def get_closest_bar(data, longitude, latitude):
    closest = data[0]
    for bar in data[1:]:
        closest_dist = get_distance(
            latitude, longitude, closest['Cells']['geoData']['coordinates'])
        temp_dist = get_distance(
            latitude, longitude, bar['Cells']['geoData']['coordinates'])
        if temp_dist < closest_dist:
            closest = bar
    return closest['Cells']['Name']


def get_distance(x1, y1, point):
    return (x1 - point[0])**2 + (y1 - point[1])**2


if __name__ == '__main__':

    bars = load_data('bars.json')
    parser = argparse.ArgumentParser()
    parser.add_argument("latitude", type=float, help="Input latitude")
    parser.add_argument("longitude", type=float, help="Input longitude")
    args = parser.parse_args()


    print ('The biggest bar is: {0}'.format(get_biggest_bar(bars)))
    print ('The smallest bar is: {0}'.format(get_smallest_bar(bars)))
    print ('The closest bar is: {0}'.format(
        get_closest_bar(bars, args.latitude, args.longitude)))
