from webdriver_operations import WebDriverOperations
from create_folder import json_path
from json_operations import JsonOperations
from selenium.common.exceptions import NoSuchWindowException


class ReportHelper:
    def __init__(self, report):
        self.report = report
        self.webdriver_operations = WebDriverOperations()
        self.properties = report[0]
        self.units = report[1]
        self.report_name = report[2]
        self.json_operations = JsonOperations(json_path(self.report_name))

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
        properties = []
        units = []
        for item in unique_elements:
            prop, unit = item.split("_")
            properties.append(prop)
            units.append(unit)
        return properties, units

    def user_input(self):
        user_input = input(
            """
            Press 1 to mark complete
            Press 2 to skip
            Press 3 to exit application
            """
        )

        if user_input is None or user_input == "":
            user_input = 1

        return int(user_input)

    def reports_loop(self):
        temp_storage = self.json_operations.retrieve_json()
        properties, units = self.filter_properties(
            self.current_report_items(), self.json_operations.retrieve_json()
        )
        for i in range(len(properties)):
            property = properties[i]
            unit = units[i]
            try:
                self.webdriver_operations.open_property(property)
                self.webdriver_operations.open_unit(unit)
                self.webdriver_operations.open_ledger()
                propunit = property + "_" + str(unit)

                user_input = self.user_input()
                if user_input == 1:
                    temp_storage.append(propunit)
                elif user_input == 2:
                    pass
                elif user_input == 3:
                    break
                else:
                    print("Invalid input. Press 1, 2, or 3")

            except NoSuchWindowException:
                print("Browser window was closed unexpectedly. Saving progress...")
                self.json_operations.write_json(temp_storage)
                break
        self.json_operations.write_json(temp_storage)
