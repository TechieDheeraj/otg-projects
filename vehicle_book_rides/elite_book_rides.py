import sys
import os

rides_available = list()
# rides_assigned contains dict of key(driver unique id : vehicle_info), value (ride class object)
rides_assigned = dict()
drivers_available = list()


class Ride:
    """
        @pickup_time: Time of pickup 
        @pickup_location: [lattitude, longitude]
        @pickup_address: Pickup point address 
        @drop_point_location: [lattitude, longitude]
        @drop_point_address: Drop point address 
        @duration: Ride duration 
        @ride_end_time: Ride end time 
    """

    def __init__(self, pickup_time, pickup_location,
                pickup_address, drop_point_location,
                drop_point_address, duration):

        # Time of pickup
        self.pickup_time = pickup_time
        # Pickup location [lattitude,longitude]
        self.pickup_location = pickup_location
        # Pickup Address 
        self.pickup_address = pickup_address
        # Drop point location [lattitude, longitude]
        self.drop_point_location = drop_point_location
        # Drop point address 
        self.drop_point_address = drop_point_address
        # Duration of ride (in minutes) 
        self.duration = duration
        self.ride_end_time = pickup_time + duration 


class Driver:
    """
        @name: Name of driver
        @current_location: Current location of driver 
        @vehicle_type: Type of vehicle 
        @vehicle_info: Vehicle information 
        @list_of_rides: Stores objects of Rides class, rides assigned to driver 
        @ride_fare: Stores the ride fare information 
    """

    def __init__(self, name, vehicle_type,
                vehicle_info, current_location, list_of_rides = []):
        self.name = name
        self.vehicle_type = vehicle_type 
        self.vehicle_info = vehicle_info 
        self.current_location = current_location
        self.ride_fare = 0  
        self.list_of_rides = list_of_rides 
    
    def update_location(self, new_location):
        """
            Updates the location of driver
        """
        self.current_location = new_location
    

    def update_ride_fare(self, fare):
        """
            Updates the ride fares 
        """
        self.ride_fare = fare 
    

    def assign_ride(self, ride):
        """
            assign ride to driver 
        """
        self.list_of_rides.append(ride)
    

    def calculate_ride_fare(self, ride):
        """
            Calculate fare of driver based on the ride
        """
        # Calculation for calculating fare for driver based on the ride 
        # new_fare = ride.end_time * duration
        # return new_fare



def load_drivers_information():
    """
        Loading the driver information
    """

    driver1 = Driver('Joe', 'SUV', 'DL2C1882', [52.33, 7.37])
    driver2 = Driver('Bob', 'SUV', 'DL2C1732', [52.33, 7.37])
    drivers_available.append(driver1)
    drivers_available.append(driver2)


def load_rides_information():
    """
        Loading the rides information
    """

    ride1 = Ride('2023/05/18-13:10:05', [55.32, 10.22], 'Park avenue street',
                [73.22, 13.44], 'NYC street', '30')

    rides_available.append(ride1)

def optimize_driver_list_and_assign_ride(ride):
    """
       This function will optimize driver list and assign ride in the below manner:

       1. Iterate through the list of drivers and check if driver is available
          based on the list_of_rides in Driver Obj.
       2. If No ride is assigned to driver we assume driver is free
       3. Check the last ride's endTime (Calculated from PickupTime + duration) and 
          see if current ride pickup time is more than the last ride's endtime If yes,
          means driver is free.
       4. Call calculate_ride_fare(ride) # Calculate fare of driver based on the ride 
       5. update_ride_fare(fare) # Update the ride fare for the driver based on the ride
       6. Take the free driver list and sort the list based on the shortest distance
          from driver's current location and pickup_location. If two drivers have same
          current location (take sorting decision based on ride_fare for those).  
       7. Pick the driver from the beginning of sorted list and do the below operations:
           1. Call assign_ride(ride) method on driver class object 
           2. Call update_location(ride.drop_point_location) # to update the new location of driver
              for decidign further rides
           3. rides_assigned[driverObj.vehicle_info] = ride # fill ride_assigned dictionary
    """

def book_ride():
    """
        Pseudo/Partial code for backend logic to book ride
    """

    if len(rides_available) == 0:
        print("No Rides to assign at the moment")
        return
    
    if len(drivers_available) == 0:
        print("No Driver is available at the moment, please try after some time")
        return 
    
    for ride in rides_available:
        optimize_driver_list_and_assign_ride(ride)

if __name__ == '__main__':
    load_drivers_information()
    load_rides_information()
    book_ride()