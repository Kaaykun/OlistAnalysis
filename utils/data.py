import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys are 'sellers', 'orders', 'order_items' etc...
        Its values are pandas.DataFrames loaded from csv files
        """
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/csv')
        file_names = [file for file in os.listdir(csv_path) if file.endswith('.csv')]
        key_names = [file_name.replace('olist_', '').replace('_dataset', '').replace('.csv', '') for file_name in file_names]

        return {key: pd.read_csv(os.path.join(csv_path, csv)) for key, csv in zip(key_names, file_names)}
