from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException

from webdriver_manager.chrome import ChromeDriverManager

from config import username, password, resident_map

import json, os

from big_panda import retrieve_csv_info
from create_folder import zero, double, create_folder_csv, json_path

zero_report = retrieve_csv_info(create_folder_csv(zero), zero)
double_report = retrieve_csv_info(create_folder_csv(double), double)


class report_helper:
    def __init__(self, report):
        self.report = report
        self.driver = self.setup_webdriver()
        self.wait = WebDriverWait(self.driver, 10)
        self.primary_tab = None
        self.properties = report[0]
        self.units = report[1]
        self.report_name = report[2]
        self.json_path = json_path(self.report_name)

    def setup_webdriver(self):
        options = Options()
        options.add_experimental_option("detach", True)
        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def login(self, username, password):
        try:
            username_input = self.driver.find_element(By.NAME, "username")
            password_input = self.driver.find_element(By.NAME, "password")
            username_input.send_keys(username)
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass

    def current_report_items(self):
        current_report_items = []
        for i in range(len(self.properties)):
            property = self.properties[i]
            unit = self.units[i]
            propunit = property + "_" + str(unit)
            current_report_items.append(propunit)
        return current_report_items

    def filter_properties(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)

        unique_elements = (set1 - set2) | (set2 - set1)
        print(unique_elements)

        properties = []
        units = []
        for item in unique_elements:
            prop, unit = item.split("_")
            properties.append(prop)
            units.append(unit)

        return properties, units

    def reports_loop(self):
        temp_storage = self.retrieve_json()
        properties, units = self.filter_properties(
            self.current_report_items(), self.retrieve_json()
        )
        for i in range(len(properties)):
            property = properties[i]
            unit = units[i]
            self.open_property(property)
            self.open_unit(unit)
            self.open_ledger()
            input("Press ENTER to continue")
            propunit = property + "_" + str(unit)
            temp_storage.append(propunit)
        self.write_json(temp_storage)

    def open_property(self, property):
        change_property_link = self.driver.find_element(
            By.XPATH, "//a[contains(., 'CHANGE PROPERTY')]"
        )
        change_property_link.click()
        property_link = self.driver.find_element(
            By.XPATH, f"//a[contains(., '{property}')]"
        )
        property_link.click()

    def open_unit(self, unit):
        search_input = self.driver.find_element(By.NAME, "search_input")
        search_input.clear()
        search_input.send_keys(unit)
        search_input.send_keys(Keys.ENTER)

    def open_ledger(self):
        ledger_xpath = "/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr/td/table[3]/tbody/tr[2]/td/table/tbody/tr[last()]/td[4]/a[4]"
        ledger_link = self.driver.find_element(By.XPATH, ledger_xpath)
        ledger_link.click()

    def write_json(self, data):
        file_path = self.json_path + "completed.json"
        try:
            with open(file_path, "w") as file:
                json.dump(data, file)
        except Exception as e:
            print(e)

    def retrieve_json(self):
        try:
            file_path = self.json_path + "completed.json"
            with open(file_path, "r") as file:
                json_string = file.read()
            data = json.loads(json_string)
            return data
        except:
            return []

    def delete_json(self):
        file_path = self.json_path + "completed.json"
        if os.path.exists(self.json_path):
            os.remove(self.json_path)


if __name__ == "__main__":
    helper = report_helper(zero_report)
    helper.driver.get(resident_map)
    helper.login(username, password)
    helper.driver.maximize_window()
    helper.reports_loop()
    helper.driver.quit()
