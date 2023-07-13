from config import username, password, resident_map
from csv_reader import retrieve_csv_info
from create_folder import create_folder_csv, zero, double
from report_helper import ReportHelper

report_types = {
    "zero_report": retrieve_csv_info(create_folder_csv(zero), zero),
    "double_report": retrieve_csv_info(create_folder_csv(double), double),
}

choose_report = input("Type zero_report or double_report and press ENTER... ")

if choose_report not in report_types:
    print("Invalid report type! Please enter either 'zero_report' or 'double_report'.")
else:
    if __name__ == "__main__":
        helper = ReportHelper(report_types[choose_report])
        helper.webdriver_operations.driver.get(resident_map)
        helper.webdriver_operations.login(username, password)
        helper.webdriver_operations.driver.maximize_window()
        helper.reports_loop()
        helper.webdriver_operations.driver.quit()
