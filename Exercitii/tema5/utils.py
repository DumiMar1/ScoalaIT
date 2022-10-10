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
    low_consumption = [item for item in lst if int(item["City mpg"]) < 16]
    medium_consumption = [item for item in lst if 16 <= int(item["City mpg"]) < 20]
    high_consumption = [item for item in lst if 20 <= int(item["City mpg"])]

    return low_consumption, high_consumption, medium_consumption


def horse_power_check(lst):
    slow_cars = [item for item in lst if int(item["Horsepower"]) < 120]
    fast_cars = [item for item in lst if 120 <= int(item["Horsepower"]) < 180]
    sport_cars = [item for item in lst if 180 <= int(item["Horsepower"])]

    return slow_cars, fast_cars, sport_cars


def save_file_at_dir(dir_path, filename, file_content,):
    os.makedirs(dir_path, exist_ok=True)
    with open(f'{dir_path}/{filename}.json', 'w') as f:
        json.dump(file_content, f, ensure_ascii=False, indent=4)


def check_brand(lst, name):
    make = [item for item in lst if item["Make"] == name]

    with open(f'output_data/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(make, f, ensure_ascii=False, indent=4)


def user_choice():
    while True:
        user_choice = input("Choose a brand you want to see.")

        if user_choice.isalpha():
            return user_choice





