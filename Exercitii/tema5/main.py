
from utils import read_csv, consumption_check, horse_power_check, generate_id, check_brand, save_file_at_dir, user_choice_1

if __name__ == "__main__":
    csv_data = read_csv("cars_list.csv")
    generated_ids = generate_id(csv_data)
    low_mpg, medium_mpg, high_mpg = consumption_check(csv_data)
    slow_cars, fast_cars, sport_cars = horse_power_check(csv_data)

    dr_path = "/Users/dumitrumarin/PycharmProjects/ScoalaInformala/Exercitii/tema5/output_data"

    low_mpg_sv = save_file_at_dir(dr_path, "low_mpg.json", low_mpg)
    medium_mpg_sv = save_file_at_dir(dr_path, "medium_mpg.json", medium_mpg)
    high_mpg_sv = save_file_at_dir(dr_path, "high_mpg.json", high_mpg)
    slow_cars_sv = save_file_at_dir(dr_path, "slow_cars.json", slow_cars)
    fast_cars_sv = save_file_at_dir(dr_path, "fast_cars.json", fast_cars)
    sport_cars_sv = save_file_at_dir(dr_path, "sport_cars.json", sport_cars)

    brand_choice = user_choice_1()

    brand_output = check_brand(csv_data, brand_choice)





