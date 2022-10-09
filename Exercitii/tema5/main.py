import os
import json
from utils import read_csv, consumption_check, horse_power_check, generate_id, check_brand

if __name__ == "__main__":
    csv_data = read_csv("cars_list.csv")
    generated_ids = generate_id(csv_data)
    low_mpg, medium_mpg, high_mpg = consumption_check(csv_data)
    slow_cars, fast_cars, sport_cars = horse_power_check(csv_data)
    checked_brand = check_brand(csv_data, "BMW")

    os.makedirs("/Users/dumitrumarin/PycharmProjects/ScoalaInformala/Exercitii/tema5/output_data", exist_ok=True)

    with open('output_data/low_mpg.json', 'w', encoding='utf-8') as f:
        json.dump(low_mpg, f, ensure_ascii=False, indent=4)

    with open('output_data/medium_mpg.json', 'w', encoding='utf-8') as f:
        json.dump(medium_mpg, f, ensure_ascii=False, indent=4)

    with open('output_data/high_mpg.json', 'w', encoding='utf-8') as f:
        json.dump(high_mpg, f, ensure_ascii=False, indent=4)

    with open('output_data/slow_cars.json', 'w', encoding='utf-8') as f:
        json.dump(slow_cars, f, ensure_ascii=False, indent=4)

    with open('output_data/fast_cars.json', 'w', encoding='utf-8') as f:
        json.dump(fast_cars, f, ensure_ascii=False, indent=4)

    with open('output_data/sports_cars.json', 'w', encoding='utf-8') as f:
        json.dump(slow_cars, f, ensure_ascii=False, indent=4)






