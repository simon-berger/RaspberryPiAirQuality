from bme68x import BME68X
import bme68xConstants as cnst
import bsecConstants as bsec
from time import sleep
from util.logging_util import log_info

class BME688:
    def __init__(self, sample_rate=bsec.BSEC_SAMPLE_RATE_LP):
        """
        Initializes the BME688 sensor object.

        Args:
            sample_rate: (optional)
                Sample rate for the sensor.
                Default value: bsec.BSEC_SAMPLE_RATE_LP
        """
        # Create bme sensor object
        self.bme = BME68X(cnst.BME68X_I2C_ADDR_HIGH, 0)

        # Sensor config
        self.bme.set_sample_rate(sample_rate)

        # Log
        log_info("Setup sensor: " + self.bme.get_variant())

    def __get_data(self):
        """
        Source: https://github.com/pi3g/bme68x-python-library/blob/main/examples/airquality.py

        Returns the bsec data if available.
        """
        data = None
        try:
            # Try to read data
            data = self.bme.get_bsec_data()
        except Exception as e:
            # Error handling
            print(e)
            return None
        
        # Return the data
        if data == {}:
            return None
        return data

    def read(self):
        """
        Reads bsec data from the sensor and returns it.
        """
        bsec_data = None

        # Try to read until the data is available
        while bsec_data == None:
            bsec_data = self.__get_data()
            sleep(0.1)

        # Log
        log_info("Read " + str(len(bsec_data)) + " data values with sample number " + str(bsec_data["sample_nr"]) + \
            " - IAQ: " + str(bsec_data["iaq"]) + " (acc=" + str(bsec_data["iaq_accuracy"]) + ")")

        # Return the data
        return bsec_data