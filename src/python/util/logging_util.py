from datetime import datetime

# Specifies the intesity of logs
#   0: Logs only errors
#   1: Logs warnings and errors
#   2: Logs everything
log_level = 2

# Check if the specified level is valid
if not log_level in [0,1,2]:
    raise ValueError("Invalid log level: " + str(log_level)) 

def print_log(msg):
    """
    Prints given log message to console.

    Args:
        msg:
            Message to print
    """
    date_time_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(date_time_str + ": " + str(msg))

def log_info(msg):
    """
    Logs given information to console.
    Enabled for log level = 2

    Args:
        msg:
            Message to print
    """
    if log_level in [2]:
        print_log(msg)

def log_warning(msg):
    """
    Logs given warning to console.
    Enabled for log level = 1,2

    Args:
        msg:
            Message to print
    """
    if log_level in [1,2]:
        print_log(msg)

def log_error(msg):
    """
    Logs given error to console.
    Enabled for log level = 0,1,2

    Args:
        msg:
            Message to print
    """
    if log_level in [1,2,3]:
        print_log(msg)
