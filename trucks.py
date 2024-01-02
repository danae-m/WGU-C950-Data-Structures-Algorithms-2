
from datetime import time

from hashtable import HashTable
from packages import PackageList


# Create each Truck object with info from the LoadTrucks() method, and route data to be updated later.
# This information comes from the LoadTrucks() method in trucks.py and is returned through that method to main.py.
class Truck:
    def __init__(self, truck_id, pkg_list, delivered_list, truck_departure, route_end):
        self.truck_id = truck_id
        self.pkg_list = pkg_list
        self.delivered_list = delivered_list
        self.truck_departure = truck_departure
        self.route_end = route_end

    # Control the way print calls display when printing truck information.
    def __str__(self):
        return ('Truck ID: %s delivered the following packages today: \n'
                '%s') % (self.truck_id, self.pkg_list)


# Connect the Truck objects to their respective IDs and parsed package lists, thus "loading" the trucks.
# This information comes from the PackageList() method in packages.py, uses the Truck constructor in trucks.py,
# and returns the truck objects to main.py.
def LoadTrucks():
    pkg_list = PackageList()
    truck_list = HashTable(3)
    truck1 = Truck(1, pkg_list[0], [], time(8, 00), time(9, 40))
    truck2 = Truck(2, pkg_list[1], [], time(9, 10), time(11,0))
    truck3 = Truck(3, pkg_list[2], [], time(10, 5), time(11,25))
    truck_list.insert(1, truck1)
    truck_list.insert(2, truck2)
    truck_list.insert(3, truck3)
    return truck_list
