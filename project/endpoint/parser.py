import json

import pandas
from fastapi import UploadFile

from project.model.excel_model import ExcelModel
from project.model.fact import Fact
from project.model.forecast import Forecast
from project.service.excel_service import create_post

pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)


def parser(file: UploadFile):
    file_x = pandas.read_excel(file, index_col=None, na_values=['NA'], usecols="A,B:AA")
    return read_file(file_x)


def read_file(file):
    parsed_json = (json.loads(file.to_json()))
    company1 = ExcelModel('company1')
    company2 = ExcelModel('company2')

    fact_first_column_list_add_one = []
    fact_second_column_list_add_one = []
    fact_third_column_list_add_one = []
    fact_four_column_list_add_one = []
    forecast_first_column_list_add_one = []
    forecast_second_column_list_add_one = []
    forecast_third_column_list_add_one = []
    forecast_four_column_list_add_one = []

    fact_first_column_list_add_two = []
    fact_second_column_list_add_two = []
    fact_third_column_list_add_two = []
    fact_four_column_list_add_two = []
    forecast_first_column_list_add_two = []
    forecast_second_column_list_add_two = []
    forecast_third_column_list_add_two = []
    forecast_four_column_list_add_two = []

    for i in parsed_json:

        if i != 'id':
            for j in parsed_json[i]:
                if i == 'company':
                    if parsed_json['company'][j] == 'company1':
                        fact_first_column_list_add_one.append(parsed_json['fact'][j])
                        fact_second_column_list_add_one.append(parsed_json['Unnamed: 3'][j])
                        fact_third_column_list_add_one.append(parsed_json['Unnamed: 4'][j])
                        fact_four_column_list_add_one.append(parsed_json['Unnamed: 5'][j])

                        fact = Fact()
                        dictionary = dict()
                        dictionary['10.08.2021'] = ['company1', 'fact', 'qliq', fact_first_column_list_add_one]
                        dictionary['11.08.2021'] = ['company1', 'fact', 'qliq', fact_second_column_list_add_one]

                        dictionary['12.08.2021'] = ['company1', 'fact', 'qoil', fact_third_column_list_add_one]
                        dictionary['13.08.2021'] = ['company1', 'fact', 'qoil', fact_four_column_list_add_one]

                        fact.count = dictionary

                        forecast_first_column_list_add_one.append(parsed_json['forecast'][j])
                        forecast_second_column_list_add_one.append(parsed_json['Unnamed: 7'][j])
                        forecast_third_column_list_add_one.append(parsed_json['Unnamed: 8'][j])
                        forecast_four_column_list_add_one.append(parsed_json['Unnamed: 9'][j])

                        forecast = Forecast()
                        dictionary_two = dict()
                        dictionary_two['10.08.2021'] = ['company1', 'fact', 'qliq', forecast_first_column_list_add_one]
                        dictionary_two['11.08.2021'] = ['company1', 'fact', 'qliq', forecast_second_column_list_add_one]

                        dictionary_two['12.08.2021'] = ['company1', 'fact', 'qoil', forecast_third_column_list_add_one]
                        dictionary_two['13.08.2021'] = ['company1', 'fact', 'qoil', forecast_four_column_list_add_one]

                        forecast.count = dictionary_two

                        company1.fact = fact
                        company1.forecast = forecast

                    if parsed_json['company'][j] == 'company2':
                        fact_first_column_list_add_two.append(parsed_json['fact'][j])
                        fact_second_column_list_add_two.append(parsed_json['Unnamed: 3'][j])
                        fact_third_column_list_add_two.append(parsed_json['Unnamed: 4'][j])
                        fact_four_column_list_add_two.append(parsed_json['Unnamed: 5'][j])

                        fact = Fact()
                        dictionary = dict()
                        dictionary['10.08.2021'] = ['company2', 'fact', 'qliq', fact_first_column_list_add_two]
                        dictionary['11.08.2021'] = ['company2', 'fact', 'qliq', fact_second_column_list_add_two]

                        dictionary['12.08.2021'] = ['company2', 'fact', 'qoil', fact_third_column_list_add_two]
                        dictionary['13.08.2021'] = ['company2', 'fact', 'qoil', fact_four_column_list_add_two]

                        fact.count = dictionary

                        forecast_first_column_list_add_two.append(parsed_json['forecast'][j])
                        forecast_second_column_list_add_two.append(parsed_json['Unnamed: 7'][j])
                        forecast_third_column_list_add_two.append(parsed_json['Unnamed: 8'][j])
                        forecast_four_column_list_add_two.append(parsed_json['Unnamed: 9'][j])

                        forecast = Forecast()
                        dictionary_two = dict()
                        dictionary_two['10.08.2021'] = ['company2', 'fact', 'qliq', forecast_first_column_list_add_two]
                        dictionary_two['11.08.2021'] = ['company2', 'fact', 'qliq', forecast_second_column_list_add_two]

                        dictionary_two['12.08.2021'] = ['company2', 'fact', 'qoil', forecast_third_column_list_add_two]
                        dictionary_two['13.08.2021'] = ['company2', 'fact', 'qoil', forecast_four_column_list_add_two]

                        forecast.count = dictionary_two

                        company2.fact = fact
                        company2.forecast = forecast


    return create_post()
