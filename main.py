# Student ID 010270658

from datetime import time
import interface
from delivery import DeliveryEngine


# The entire process is started here with the DeliveryEngine in delivery.py.
all_routes, delivery_table, truck_list = DeliveryEngine()


# Get total mileage.
total_mileage = interface.total_lookup(all_routes)


# This is the user interface. Code runs sequentially and calls methods from interface.py to print info as requested.
# The populated tables, returned from the DeliveryEngine call above, power all user requests below.
print("Welcome to the WGUPS Package Routing and Tracking System (PRATS)")
print("Total mileage today for all trucks is: " + str(total_mileage))
while True:
    print("Press Q to quit. To continue, please select from the following options:")
    print("  1. List all packages")
    print("  2. Check package tracking information by time")
    print("  3. Check truck and route information by Truck ID")
    user_choice = str(input())

    # Quit statement
    if user_choice == 'q' or user_choice == 'Q':
        break

    # List all packages
    if user_choice == '1':
        main_menu = False
        while not main_menu:
            user_in = input("Press Q to quit. Press 0 to list all packages.")
            if user_in == 'q' or user_in == 'Q':
                main_menu = True
                break
            elif user_in == '0':
                user_out = interface.print_all_packages(truck_list, delivery_table)
                if user_out is None:
                    user_in2 = input("Press Q to quit.")
                    if user_in2 == 'q' or user_in2 == 'Q':
                        main_menu = True
                        break
            else:
                print("Invalid entry. Please try again.")
                continue

    # Search for package tracking information by time using a while loop to continue using the feature until 'quit'
    elif user_choice == '2':
        main_menu = False
        while not main_menu:
            user_hr = input("Press Q to quit. Please enter the hour: ")
            if user_hr == 'q' or user_hr == 'Q':
                main_menu = True
                break

            # Check that entered user time is valid before proceeding with package search
            else:
                user_hr = int(user_hr)
                if user_hr < 0 or user_hr > 23:
                    print("Invalid entry. Please try again.")
                    continue
                user_min = int(input("Please enter the minutes: "))
                if user_min < 0 or user_min > 59:
                    print("Invalid entry. Please try again.")
                    continue
                user_time = time(user_hr, user_min)

            print("Press 1 to search for a package by Package ID. Press 0 to see all packages.")
            user_in = int(input())

            # For searching for a specific package ID number at the aforespecified time
            # Uses a while loop to continue searching for multiple specific packages by package ID until 'quit'
            if user_in == 1:
                print("Please enter the Package ID number:")
                time_menu = False
                while not time_menu:
                    user_in2 = int(input())
                    if user_in2 in range(1, 41):
                        user_out = interface.time_lookup(user_time, user_in2, delivery_table)
                        if user_out is None:
                            print("Press 0 to search for another package. Press X to return to the previous menu.")
                            user_in3 = str(input())
                            if user_in3 == '0':
                                print("Please enter the Package ID number: ")
                                continue
                            if user_in3 == 'X' or user_in3 == 'x':
                                time_menu = True
                                break
                    else:
                        print("Invalid entry. Please try again. Enter the Package ID number:")

            # Print all packages and their delivery status at the aforespecified time
            if user_in == 0:
                for a_key in range(1,41):
                    interface.time_lookup(user_time, a_key, delivery_table)
                print("Press X to return to the main menu.")
                user_in2 = str(input())
                if user_in2 == 'X' or user_in2 == 'x':
                    main_menu = True
                    break

    # Searching for truck and route information by truck ID number
    # Uses a while loop to continue using this feature until 'quit'
    elif user_choice == '3':
        print("Please enter the Truck ID number: ")
        main_menu = False
        while not main_menu:
            user_in = int(input())

            # Check that the truck ID number is valid
            if user_in in range(1,4):
                user_out = interface.truck_lookup(user_in, truck_list, all_routes)
                if user_out is None:
                    print("Press I for more information. Press 0 to search for another truck. "
                          "Press X to return to the main menu.")
                    user_in2 = str(input())

                    # Additional information about which packages are on any individual truck at any specific time
                    # Uses a while loop to continue searching for trucks by truck ID until 'quit'
                    if user_in2 == 'I' or user_in2 == 'i':
                        time_menu = False
                        while not time_menu:
                            user_hr = input("Press Q to quit. Please enter the hour: ")
                            if user_hr == 'q' or user_hr == 'Q':
                                print("Please enter the Truck ID number: ")
                                time_menu = True
                                break

                            # Check that entered user time is valid before proceeding with truck and route search
                            else:
                                user_hr = int(user_hr)
                                if user_hr < 0 or user_hr > 23:
                                    print("Invalid entry. Please try again.")
                                    continue
                                user_min = int(input("Please enter the minutes: "))
                                if user_min < 0 or user_min > 59:
                                    print("Invalid entry. Please try again.")
                                    continue
                                user_time = time(user_hr, user_min)
                                user_out = interface.truck_time_lookup(user_time, user_in, truck_list, delivery_table)
                    if user_in2 == '0':
                        print("Please enter the Truck ID number: ")
                        continue
                    if user_in2 == 'X' or user_in2 == 'x':
                        main_menu = True
                        break

            # Error statement in case of invalid selection
            else:
                print("Invalid selection. Please try again. Enter Truck ID number: ")

    # Error statement in case of invalid selection
    else:
        print("Invalid selection. Please try again. Select from the following options: ")
