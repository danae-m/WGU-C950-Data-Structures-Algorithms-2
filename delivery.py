
from routes import RouteBuilder
from dijkstra import UpdateRoutes, FindDestination
from datetime import timedelta, datetime


# The DeliveryEngine is the core mechanic which ties together packages, trucks, routes, and the algorithm
# Packages are "delivered" here and all calculations for delivery time and delivery route are made here
# Called from main.py and returns all fully-populated hash tables to main.py. Calls RouteBuilder in routes.py.
def DeliveryEngine():
    all_routes, delivery_table, truck_list = RouteBuilder()
    for key in range(1, 4):
        truck = truck_list.search(key)
        departure_time = truck.truck_departure
        pkg_list = truck.pkg_list
        route = all_routes.search(truck.truck_id)
        distance_list = route.delivery_distance
        package_order = route.package_order
        delivery_route = route.delivery_route
        total_distance = int(0)
        route_updated = False

        # Uninterrupted delivery services for trucks 1 and 3
        for pack_key in pkg_list:
            package = delivery_table.search(pack_key)
            package.pkg_departure = departure_time
            package.StatusSetter(0)

        # Interrupted delivery service for truck 2, which has the wrongly addressed package to be updated
        # Code stops the delivery route at the time the package address is updated and recalculates the remaining route
        for index, pkg in enumerate(package_order):
            if key == 2 and total_distance >= 24 and route_updated is False:
                delivery_route, package_order, delivery_distance = (
                    UpdateRoutes(delivery_route, delivery_table, package_order))
                route_updated = True

            package = delivery_table.search(pkg)
            distance = distance_list[index]
            total_distance += distance
            delivery_route.remove(FindDestination(pkg, delivery_table))
            delivery_time = (
                    timedelta(hours=departure_time.hour, minutes=departure_time.minute)
                    + timedelta(minutes=((total_distance / 18) * 60)))
            delivery_datetime = datetime(2000, 1, 1) + delivery_time
            final_time = delivery_datetime.time()
            package.pkg_delivery = final_time

    return all_routes, delivery_table, truck_list
