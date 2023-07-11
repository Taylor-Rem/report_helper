from datetime import datetime
import os

now = datetime.now()
day = now.day
month = now.month
year = now.year
username = "taylorremund"

months_of_the_year = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}

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


def create_json(report):
    path = f"/Users/{username}/Desktop/report_helper/reports/{report}/{year}/{month}"
    if not os.path.exists(path):
        os.makedirs(path)
    return path
