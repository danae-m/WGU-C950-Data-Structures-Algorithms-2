
from dijkstra import CompileRoutes, GetData
from hashtable import HashTable


# This is the class which initiates the entire build process. All downstream data from the packages, hashtable, trucks,
# distances, routes, and dijkstra modules begins here and ultimately returns here.
class Route:
    def __init__(self, truck_id, package_order, delivery_route, delivery_distance, total_mileage):
        self.truck_id = truck_id
        self.package_order = package_order
        self.delivery_route = delivery_route
        self.delivery_distance = delivery_distance
        self.total_mileage = total_mileage
        self.delivery_time = float("{:.2f}".format(total_mileage / 18))
        self.hours = int(self.delivery_time)
        self.minutes = int(60 * (self.delivery_time - self.hours))

    # Control the way print calls display when printing route information.
    def __str__(self):
        return ('Truck ID: %s has traveled %s total miles today.\n'
                'Its route today took %s hour(s) and %s minute(s).\n') % (self.truck_id, self.total_mileage,
                                                                      self.hours, self.minutes)


# Instantiate a hashtable for routes, populate other truck and package data, and send to dijkstra.py for the output of
# the algorithm which has gathered all previous information. This information is called from and returned to delivery.py
def RouteBuilder():
    delivery_table, truck_list = GetData()
    all_routes = HashTable(3)
    for truck_id in range(1, 4):
        for results in CompileRoutes(truck_id):
            package_order, delivery_route, delivery_distance, total_mileage = results
            new_route = Route(truck_id, package_order, delivery_route, delivery_distance, total_mileage)
            all_routes.insert(truck_id, new_route)
    return all_routes, delivery_table, truck_list
