import json
import os
import argparse
import math


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    return min(data, key=lambda data: data['Cells']['SeatsCount'])['Cells']['Name']


def get_smallest_bar(data):
    return max(data, key=lambda data: data['Cells']['SeatsCount'])['Cells']['Name']


def get_closest_bar(data, latitude, longitude):
    if not (latitude or longitude):
        return 'Input correct coordinates!'
    return min(data, key=lambda data: get_distance(
        latitude, longitude, data['Cells']['geoData']['coordinates']))['Cells']['Name']


def get_distance(x1, y1, point):
    return math.sqrt((x1 - point[0])**2 + (y1 - point[1])**2)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, required=True)
    parser.add_argument('-lat', '--latitude', type=float, help='Your latitude')
    parser.add_argument(
        '-long', '--longitude', type=float, help='Your longitude')
    args = parser.parse_args()

    bars = load_data(args.path)
    print ('The biggest bar is: {}'.format(get_biggest_bar(bars)))
    print ('The smallest bar is: {}'.format(get_smallest_bar(bars)))
    print ('The closest bar is: {}'.format(
        get_closest_bar(bars, args.latitude, args.longitude)))
