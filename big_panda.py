import pandas as pd
from create_folder import create_folder_csv, create_json


def retrieve_csv_info(path):
    df = pd.read_csv(path)
    properties = df.filter(like="Property Name").values.flatten().tolist()
    units = df.filter(like="Space Number").values.flatten().tolist()
    return properties, units
