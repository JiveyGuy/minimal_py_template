# this handles logging 

import datetime
import logging
import sys

def make_log_name(settings):
    # get the time and log level
    time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_level = settings.get("General", "log_level")
    
    # make the log name
    log_name = "{}_{}.log".format(time, log_level)
    return log_name


def configure_logging(settings):
    # read settings
    log_level = get_logging_level(settings)
    print_log = settings.get("General", "print_log")

    # formatr desired "#epoch-level-function: message"
    log_format = "%(asctime)s-%(levelname)s-%(funcName)s: %(message)s"

    # pick a log file name
    log_path = settings.get("Path", "log")
    log_name = make_log_name(settings)
    log_file = f"{log_path}/{log_name}"

    # configure logger
    logging.basicConfig(filename=log_file,
                        level=log_level,
                        format=log_format
                    )
    
    if print_log == "True":
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    
    logging.debug("Logging configured")
    logging.debug(f"Log level: {log_level}")
    logging.debug(f"Log file: {log_file}")
    logging.debug(f"Log format: {log_format}")
    logging.debug(f"Print log: {print_log}")

def get_logging_level(settings):
    # read settings
    log_level = settings.get("General", "log_level")
    log_level_local = logging.INFO

    # match log level to logging level
    if log_level == "DEBUG":
        log_level_local = logging.DEBUG
    elif log_level == "INFO":
        log_level_local = logging.INFO
    elif log_level == "WARNING":
        log_level_local = logging.WARNING
    elif log_level == "ERROR":
        log_level_local = logging.ERROR
    elif log_level == "CRITICAL":
        log_level_local = logging.CRITICAL
    else:
        log_level_local = logging.INFO

    return log_level_local