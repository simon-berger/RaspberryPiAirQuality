from sensor.bme688 import BME688
from time import sleep
import decimal

# Create sensor object
bme = BME688()

try:
    while True:
        # Read the data
        d = bme.read()

        # Round all data values
        for d_key in d:
            d[d_key] = float(round(d[d_key], 2))

        # Print several values
        split_char = "-"
        print("Sample Nr:", d["sample_nr"], split_char,\
            "IAQ:", d["iaq"], split_char,\
            "IAQ Acc:", d["iaq_accuracy"], split_char,\
            "Temp:", d["temperature"], split_char,\
            "Hum:", d["humidity"], split_char,\
            "C02:", d["co2_equivalent"], split_char,\
            "C02 Acc:", d["co2_accuracy"], split_char,\
            "Comp Gas:", d["comp_gas_value"], split_char,\
            "Comp Gas Acc:", d["comp_gas_accuracy"], split_char,\
            end="\r")

        # Update every second
        sleep(1)
except KeyboardInterrupt:
    # Interrupt received
    print("Program stopped")
    exit(0)