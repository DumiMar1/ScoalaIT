import csv
import os
import uuid
import json


def read_csv(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        return list(csv_reader)


def generate_id(lst):
    for item in lst:
        item["ID"] = str(uuid.uuid1())


def consumption_check(lst):
    low_consumption = []
    medium_consumption = []
    high_consumption = []

    for item in lst:
        if int(item["City mpg"]) < 16:
            low_consumption.append(item)

        elif 16 <= int(item["City mpg"]) < 20:
            medium_consumption.append(item)

        elif 20 <= int(item["City mpg"]):
            high_consumption.append(item)

    return low_consumption, high_consumption, medium_consumption


def horse_power_check(lst):
    slow_cars = []
    fast_cars = []
    sport_cars = []

    for item in lst:
        if int(item["Horsepower"]) < 120:
            slow_cars.append(item)
        elif 120 <= int(item["Horsepower"]) < 180:
            fast_cars.append(item)
        else:
            sport_cars.append(item)

    return slow_cars, fast_cars, sport_cars


def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)


def check_brand(lst, name):
    make = []
    for item in lst:
        if item["Make"] == name:
            make.append(item)
            with open(f'output_data/{name}.json', 'w', encoding='utf-8') as f:
                json.dump(make, f, ensure_ascii=False, indent=4)







