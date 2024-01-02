from hashtable import HashTable
from trucks import LoadTrucks
from distances import GetMatrix
from packages import PackageData
from datetime import time


# Declare and populate the hash tables and lists which hold package and truck information. These calls go to packages.py
# and trucks.py respectively and return the data here, to be forwarded to RouteBuilder() in routes.py. Also used below.
def GetData():
    delivery_table = PackageData('csvs/packagesCSV.csv')
    truck_list = LoadTrucks()
    return delivery_table, truck_list


# The Dijkstra's Shortest Path algorithm. This is called from routes.py, takes a truck ID and gets info from trucks.py
# and distances.py to feed into the algorithm function below, receives info back, and forwards this info to routes.py.
def CompileRoutes(truck_id):
    matrix = GetMatrix()
    delivery_table, truck_list = GetData()
    package_order = []
    delivery_route = []
    delivery_distance = []
    start_node = int(0)
    total_mileage = float(0.0)

    truck = truck_list.search(truck_id)
    pack_list = truck.pkg_list[:]

    # Exhaust the package list by incrementing the start node to each closest node until the list is empty.
    # This information goes directly into the below function which returns info here.
    while len(pack_list) > 0:
        next_pkg, next_dist = FindNext(pack_list, matrix, start_node, delivery_table)
        next_node = FindDestination(next_pkg, delivery_table)
        package_order.append(next_pkg)
        delivery_route.append(next_node)
        delivery_distance.append(next_dist)
        pack_list.remove(next_pkg)
        start_node = int(next_node)
        total_mileage += float(next_dist)
    total_mileage = float(f'{total_mileage:.1f}')
    yield package_order, delivery_route, delivery_distance, total_mileage


# Handle route updates such as the updated address for Package 9 by recompiling routes and returning to delivery.py.
def UpdateRoutes(delivery_route, delivery_table, package_order):
    delivery_route.append(FindDestination(9, delivery_table))
    matrix = GetMatrix()
    diff = (len(package_order) - len(delivery_route) + 1)
    new_route = []
    pack_order = []
    to_deliver = package_order[diff:]
    to_deliver.append(9)
    update_pack = delivery_table.search(9)
    update_pack.pkg_delivery = time(10,48)
    update_pack.pkg_departure = time(9,0)
    del_distance = []
    start_node = int(FindDestination(to_deliver[0], delivery_table))
    while len(to_deliver) > 0:
        next_pack, next_dist = FindNext(to_deliver, matrix, start_node, delivery_table)
        next_node = FindDestination(next_pack, delivery_table)
        pack_order.append(next_pack)
        new_route.append(next_node)
        del_distance.append(next_dist)
        to_deliver.remove(next_pack)
        start_node = int(next_node)
    return new_route, pack_order, del_distance


# Translates between Package ID and Delivery ID. This info is called from the above & below functions and returns there.
def FindDestination(pkg_id, delivery_table):
    package = delivery_table.search(pkg_id)
    delivery_id = package.pkg_delivery_id
    return delivery_id

def FindPackage(delivery_id, delivery_table):
    for package in delivery_table:
        if package.pkg_delivery_id == delivery_id:
            pkg_id = package.pkg_id
            return pkg_id


# This is the meat of the algorithm, which compares numbers from the weighted adjacency matrix and selects the closest
# node. This information comes from the CompileRoutes and UpdateRoutes methods above and returns it there.
def FindNext(pkg_list, matrix, start_node, delivery_table):
    min_dist = 1000
    min_node = -1
    for pkg in pkg_list:
        delivery_id = int(FindDestination(pkg, delivery_table))
        if delivery_id >= start_node:
            if matrix[delivery_id][start_node] < float(min_dist):
                min_dist = float(matrix[delivery_id][start_node])
                min_node = pkg
        if delivery_id < start_node:
            if matrix[start_node][delivery_id] < float(min_dist):
                min_dist = float(matrix[start_node][delivery_id])
                min_node = pkg
    return min_node, min_dist
