import pandas as pd
import os


def retrieve_csv_info(path, report):
    file_name = os.listdir(path)[-1]
    file_path = os.path.join(path, file_name)
    df = pd.read_csv(file_path)
    properties = df.filter(like="Property Name").values.flatten().tolist()
    units = df.filter(like="Space Number").values.flatten().tolist()
    return [properties, units, report]
