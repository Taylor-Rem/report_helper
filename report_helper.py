from webdriver_operations import WebDriverOperations
from create_folder import json_path
from json_operations import JsonOperations


class ReportHelper:
    def __init__(self, report):
        self.report = report
        self.webdriver_operations = WebDriverOperations()
        self.json_operations = JsonOperations(json_path(self.report_name))
        self.properties = report[0]
        self.units = report[1]
        self.report_name = report[2]

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
        temp_storage = self.json_operations.retrieve_json()
        properties, units = self.filter_properties(
            self.current_report_items(), self.json_operations.retrieve_json()
        )
        for i in range(len(properties)):
            property = properties[i]
            unit = units[i]
            self.webdriver_operations.open_property(property)
            self.webdriver_operations.open_unit(unit)
            self.webdriver_operations.open_ledger()
            input("Press ENTER to continue")
            propunit = property + "_" + str(unit)
            temp_storage.append(propunit)
        self.json_operations.write_json(temp_storage)
