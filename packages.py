
import csv
from datetime import time

import hashtable


# Create each package with the information gleaned from the .csv file.
# This data comes from the PackageData() method below and is sent through the same method to the hash table in main.py.
class Package:
    def __init__(self, pkg_id, pkg_delivery_id, pkg_address, pkg_city, pkg_state, pkg_zip, pkg_deadline, pkg_status,
                 pkg_departure, pkg_delivery, pkg_weight, pkg_notes):
        self.pkg_id = pkg_id
        self.pkg_delivery_id = pkg_delivery_id
        self.pkg_address = pkg_address
        self.pkg_city = pkg_city
        self.pkg_state = pkg_state
        self.pkg_zip = pkg_zip
        self.pkg_deadline = pkg_deadline
        self.pkg_status = 'N/A'
        self.pkg_departure = 'N/A'
        self.pkg_delivery = 'N/A'
        self.pkg_weight = pkg_weight
        self.pkg_notes = pkg_notes

    # Control the way print calls display when printing package information.
    def string_all(self):
        return (' ~ Information for Package ID: %s ~ \n'
                'Delivery address: %s, %s %s, %s\n'
                'Left the Hub at: %s\n'
                'Original delivery deadline: %s\n'
                'Delivered at: %s  |  Weighs %s lb(s)\n'
                'Notes (if available): %s\n') % (
            self.pkg_id, self.pkg_address, self.pkg_city, self.pkg_state, self.pkg_zip, self.pkg_departure,
            self.pkg_deadline, self.pkg_delivery, self.pkg_weight, self.pkg_notes)

    # packages at the hub
    def string_tracking_0(self):
        return (' ~ Tracking Information for Package ID: %s ~ \n'
                'Delivery status: %s | Delivery deadline: %s\n'
                'Delivery address: %s, %s %s, %s\n'
                'Scheduled to leave the Hub at %s\n') % (
            self.pkg_id, self.pkg_status, self.pkg_deadline, self.pkg_address, self.pkg_city, self.pkg_state,
            self.pkg_zip, self.pkg_departure)

    # packages on the way
    def string_tracking_1(self):
        return (' ~ Tracking Information for Package ID: %s ~ \n'
                'Delivery status: %s | Delivery deadline: %s\n'
                'Delivery address: %s, %s %s, %s\n'
                'Left the Hub at %s\n') % (
            self.pkg_id, self.pkg_status, self.pkg_deadline, self.pkg_address, self.pkg_city, self.pkg_state,
            self.pkg_zip, self.pkg_departure)

    # delivered packages
    def string_tracking_2(self):
        return (' ~ Tracking Information for Package ID: %s ~ \n'
                'Delivery status: %s | Delivered at: %s\n'
                'Original delivery deadline: %s\n'
                'Delivered to: %s, %s %s, %s\n') % (
            self.pkg_id, self.pkg_status, self.pkg_delivery, self.pkg_deadline, self.pkg_address, self.pkg_city,
            self.pkg_state, self.pkg_zip)

    # delayed packages
    def string_tracking_4(self):
        return ('Tracking Information for Package ID: %s\n'
                'is unavailable at this time. Package %s\n'
                'has been delayed. Please try again later.\n') % (self.pkg_id, self.pkg_id)

    # packages on truck
    def string_tracking_6(self):
        return 'Package ID: %s | Delivery status: On the way' % self.pkg_id

    # Set status for packages as they are delivered or depart the hub
    def StatusSetter(self, status):
        if status == 4:
            self.pkg_status = 'Awaiting package...'
        elif status == 1:
            self.pkg_status = 'On the way'
        elif status == 2:
            self.pkg_status = 'Delivered!'
        else:
            self.pkg_status = 'At the hub'


# Instantiate the hash table and parse package data from the package csv file.
# This info will head to the Package constructor.
def PackageData(filename):
    delivery_table = hashtable.HashTable(40)
    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')
        for package in package_data:
            pkg_id = int(package[0])
            pkg_delivery_id = package[1]
            pkg_address = package[2]
            pkg_city = package[3]
            pkg_state = package[4]
            pkg_zip = package[5]
            pkg_deadline = package[6]
            pkg_status = None
            pkg_departure = None
            pkg_delivery = None
            pkg_weight = package[7]
            pkg_notes = package[8]

            # Send parsed data to Package constructor, then add each complete package to the hash table.
            new_package = Package(pkg_id, pkg_delivery_id, pkg_address, pkg_city, pkg_state, pkg_zip, pkg_deadline,
                                  pkg_status, pkg_departure, pkg_delivery, pkg_weight, pkg_notes)
            delivery_table.insert(pkg_id, new_package)
        return delivery_table


# Parse data from a csv file to create a list of package IDs to be assigned to each truck.
# This info goes to the LoadTrucks() method in trucks.py to be passed to the Truck constructor there.
def PackageList():
    package_lists = []
    with open('csvs/pkglistsCSV.csv') as pkglists:
        reader = csv.reader(pkglists)
        for row in reader:
            int_row = [int(value) for value in row]
            package_lists.append(int_row)
    return package_lists
