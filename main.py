from helpers.csv_helper import result_to_csv
from helpers.processing_all_data import processing_existing_data


# pip install https://github.com/vBaiCai/python-pesq/archive/master.zip

def have_fun_yourself():
    final_results = processing_existing_data()
    result_to_csv(final_results)


have_fun_yourself()
