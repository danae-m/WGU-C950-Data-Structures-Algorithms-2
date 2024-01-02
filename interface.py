
from datetime import time

# Look up and print all package information. From the terminal menu.
def print_all_packages(truck_list, delivery_table):
    for truck_key in range(1, 4):
        truck = truck_list.search(truck_key)
        onboard_list = truck.pkg_list
        print("Packages on Truck #" + str(truck_key) + ":")
        for pkg_key in range(1, 41):
            package = delivery_table.search(pkg_key)
            if package.pkg_id in onboard_list:
                print(package.string_all())
    return None

# Look up and print truck and route info by truck ID. From the terminal menu.
def truck_lookup(lookup_id, truck_list, all_routes):
    truck = truck_list.search(lookup_id)
    route = all_routes.search(lookup_id)
    print(truck)
    print(route)
    return None


# Get information about packages on a given truck at any time specified by the user.
def truck_time_lookup(user_time, lookup_id, truck_list, delivery_table):
    truck = truck_list.search(lookup_id)
    onboard_list = truck.pkg_list
    truck_time = truck.truck_departure
    truck_end = truck.route_end
    if truck_time <= user_time <= truck_end:
        print('The packages currently on Truck ID: ' + str(lookup_id) + ' are:')
        for package in onboard_list:
            pack_status = status_lookup(user_time, package, delivery_table)
            if pack_status == 1:
                onboard_package = delivery_table.search(package)
                print(onboard_package.string_tracking_6())
    else:
        print('There are no packages currently on Truck ID: ' + str(lookup_id))
    return None


# Get information about total mileage for all trucks individually and combined
def total_lookup(all_routes):
    total_all_trucks = 0
    for key in range(1,4):
        route = all_routes.search(key)
        total_all_trucks += route.total_mileage
    return total_all_trucks


# Call status_lookup below and print appropriate information status information. Called from the main terminal.
def time_lookup(user_time, key, delivery_table):
    package = delivery_table.search(key)
    pack_status = status_lookup(user_time, key, delivery_table)

    if pack_status == 0:
        print(package.string_tracking_0())
    if pack_status == 1:
        print(package.string_tracking_1())
    if pack_status == 2:
        print(package.string_tracking_2())
    if pack_status == 4:
        print(package.string_tracking_4())
    if pack_status == 9:
        print("Package ID: 9 is currently Delayed. Please try again later.\n")

    return None


# Set all package statuses at any time specified by the user. Called from and returned to other local functions.
def status_lookup(user_time, key, delivery_table):
    package = delivery_table.search(key)

    # Package 9 cannot be marked out for delivery until the address is updated at 10:20.
    if key == 9 and user_time < time(10, 20):
        return 9

    # Delayed packages must not be marked at hub until they have arrived at 9:05.
    elif package.pkg_notes.startswith("Delayed") and user_time < time(9, 5):
        package.StatusSetter(4)
        return 4

    # Update all package statuses based on their relationship to the user entered time.
    elif package.pkg_departure < user_time < package.pkg_delivery:
        package.StatusSetter(1)
        return 1

    elif package.pkg_delivery < user_time:
        package.StatusSetter(2)
        return 2

    else:
        return 0
