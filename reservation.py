"""
Reservation finder

Along with this file, you'll find two files named units.csv and reservations.csv with fields in the following format

units.csv
location_id, unit_size

reservations.csv
location_id, reservation_start_date, reservation_end_date

You will write a simple application that manages a reservation system. It will have two commands, 'available' and 'reserve' with the following behaviors:

available <date> <number of occupants> <length of stay>
This will print all available units that match the criteria. Any unit with capacity equal or greater to the number of occupants will be printed out.

Example:
SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available

reserve <unit number> <start date> <length of stay>
This creates a record in your reservations that indicates the unit has been reserved. It will print a message indicating its success.

A reservation that ends on any given day may be rebooked for the same evening, ie:
    
    If a reservation ends on 10/10/2013, a different reservation may be made starting on 10/10/2013 as well.

Example:
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights

Reserving a unit must make the unit available for later reservations. Here's a sample session:

SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights
SeaBnb> available 10/10/2013 2 4
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Unit 10 is unavailable during those dates
SeaBnb> quit

Notes:
Start first by writing the functions to read in the csv file. These have been stubbed for you. Then write the availability function, then reservation. Test your program at each step (it may be beneficial to write tests in a separate file.) Use the 'reservations' variable as your database. Store all the reservations in there, including the ones from the new ones you will create.

The datetime and timedelta classes will be immensely helpful here, as will the strptime function.
"""

import sys
import datetime

def parse_one_record(line):
    """Take a line from reservations.csv and return a dictionary representing that record. (hint: use the datetime type when parsing the start and end date columns)"""
    resDict = {}
    thisRes = line.split(",")
    unit_id = int(thisRes[0])
    startDate = datetime.datetime.strptime(thisRes[1], "%m/%d/%Y")
    endDate = datetime.datetime.strptime(thisRes[2], "%m/%d/%Y")
    resDict[unit_id] = (startDate, endDate)
    return resDict

def read_units():
    """Read in the file units.csv and returns a list of all known units."""
    list_of_units = []

    for line in open("units.csv").readlines():
        list_of_units.append(line.replace("\n", "").replace(" ",""))

    return list_of_units

def read_existing_reservations():
    """Reads in the file reservations.csv and returns a list of reservations."""
    list_of_res = []

    for line in open("reservation.csv").readlines():
        list_of_res.append(line.replace("\n","").replace(" ",""))

    return list_of_res

def available(units, reservations, start_date, occupants, stay_length):
    """Prints out what is available based on the start_date, occupants, and stay_length"""

    num_unit_avail = 0

    for unit in units:
        # get unit id and unit size
        thisUnit = unit.split(",")
        unit_id = int(thisUnit[0])
        unit_size = int(thisUnit[1])

        # make sure unit size is big enough
        if unit_size >= int(occupants):

            # when size is good, look up reservations for this unit to make sure it's avail
            for res in reservations:
                resDict = parse_one_record(res)
                # returns (the first unavail date, the last unavail date) for this unit id
                res_info = resDict.get(unit_id, None) 
                if res_info:
                    startDate = datetime.datetime.strptime(start_date, "%m/%d/%Y")

                    # unit is available on the start_date for stay_length days
                    if res_info[0] <= startDate < res_info[1]:
                        unit_id = 0
                        break
            if unit_id:
                num_unit_avail += 1      
                print "Unit %d (Size %d) is available"%(unit_id, unit_size)

    if not num_unit_avail:
        print "No unit is available"

def reserve(units, reservations, unit_id, start_date, stay_length):

    for res in reservations:
        resDict = parse_one_record(res)
        res_info = resDict.get(int(unit_id), None)

        # go through all reservations for this unit_id
        if res_info:
            startDate = datetime.datetime.strptime(start_date, "%m/%d/%Y")

            # make sure startDate doesn't fall into any existing reservations
            if res_info[0] <= startDate < res_info[1]:
                print "Unit %s is unavailable during those dates"%unit_id
                return;
     
            # gather all existing reservations for this unit_id


    # fix this...
    if avail_list:
        print avail_list
        # check if unit is avail for stay_length days from existing reservations

        # reserve the unit and record in write to reservations.csv
        print "Successfully reserved unit %d for %d days"%(unit_id, stay_length)

def main():
    units = read_units()
    reservations = read_existing_reservations()  

    while True:
        command = raw_input("SeaBnb> ")
        cmd = command.split()
        if cmd[0] == "available":
            # look up python variable arguments for explanation of the *
            available(units, reservations, *cmd[1:])
        elif cmd[0] == "reserve":
            reserve(units, reservations, *cmd[1:])
        elif cmd[0] == "quit":
            sys.exit(0)
        else:
            print "Unknown command"

if __name__ == "__main__":
    main()