from config import username, password, resident_map
from csv_reader import retrieve_csv_info
from create_folder import create_folder_csv, zero, double
from report_helper import ReportHelper

zero_report = retrieve_csv_info(create_folder_csv(zero), zero)
double_report = retrieve_csv_info(create_folder_csv(double), double)

if __name__ == "__main__":
    helper = ReportHelper(zero_report)
    helper.webdriver_operations.driver.get(resident_map)
    helper.webdriver_operations.login(username, password)
    helper.webdriver_operations.driver.maximize_window()
    helper.reports_loop()
    helper.webdriver_operations.driver.quit()
