from sensor.bme688 import BME688
from time import sleep
from util.logging_util import log_info
from datetime import datetime
import decimal
import os

############################# Config #############################
filepath = "/home/pi/RaspberryPiAirQuality/data/measurements.csv"
##################################################################

def clear_console():
    """
    Clears the linux console.
    """
    os.system('clear')

def print_welcome():
    """
    Prints the welcome text.
    """
    # Clear console
    clear_console()

    # Print welcome text
    line_width = 58
    print()
    print(line_width * "#")
    print("\n  Welcome to IndoorAirQualityMeasurement by Simon Berger\n")
    print(line_width * "#")
    print()

def write_data_to_csv(data, filepath):
    """
    Writes the data from the given dictionary to the specified file in csv format.
    If the file does not exist it is created and the csv column names are added automatically.

    Args:
        data:
            Dict containing the data values
        filepath:
            File path of the file the data is written to
    """
    # List of values that are not saved
    ignore_list = []

    # Character that is used to split values
    split_char = ";"

    # Check if the file already exists
    if os.path.isfile(filepath):
        # File already exists
        # Open file with append mode
        f = open(filepath, "a")
    else:
        # File does not exist
        # Create new file
        f = open(filepath, "w")

        # Write column headers
        printed = False
        for d_key in data:
            if not d_key in ignore_list:
                if printed:
                    # Write split character
                    f.write(split_char)
                printed = True
                # Write measurement data name
                f.write(d_key)
        f.write("\n")

    printed = False
    for d_key in data:
        if not d_key in ignore_list:
            if printed:
                # Write split character
                f.write(split_char)
            printed = True
            # Write measurement value
            f.write(str(data[d_key]))
    f.write("\n")

def main():
    """
    Main method to start IndoorAirQualityMeasurement.
    """
    # Print welcome text
    print_welcome()

    # Wait
    sleep(2)

    # Delete old data file
    try:
        os.remove(filepath)
        log_info("Deleted old measurements")
    except FileNotFoundError:
        pass # Nothing to do here

    # Create sensor object
    bme = BME688()

    try:
        while True:
            # Read the data
            d = bme.read()

            # Round all data values
            for d_key in d:
                d[d_key] = float(round(d[d_key], 2))

            # Add timestamp
            d["datetime"] = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

            # Write data values
            write_data_to_csv(d, filepath)

            # Sleep to reduce load
            # sleep(5)
    except KeyboardInterrupt:
        # Interrupt received
        log_info("Program stopped")
        exit(0)

if __name__ == "__main__":
    main()