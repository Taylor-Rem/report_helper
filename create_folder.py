from datetime import datetime
import os

now = datetime.now()
day = now.day
month = now.month
year = now.year
username = "taylorremund"

reports = {"zero": "zero_rent_reports", "double": "double_rent_reports"}

zero = reports["zero"]
double = reports["double"]


def create_folder_csv(report):
    path = (
        f"/Users/{username}/Desktop/report_helper/reports/{report}/{year}/{month}/{day}"
    )

    if not os.path.exists(path):
        os.makedirs(path)
    return path


create_folder_csv(zero)
create_folder_csv(double)


def json_path(report):
    path = f"/Users/{username}/Desktop/report_helper/reports/{report}/{year}/"
    if not os.path.exists(path):
        os.makedirs(path)
    return path
