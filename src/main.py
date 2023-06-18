# === imports ===
import logging

# = local imports =
from utils import log, settings

def main():
    # read settings
    my_settings = settings.get_settings()

    # configure logging
    log.configure_logging(my_settings)

    # log start of program
    logging.info("Program started")

    # do stuff
    logging.info("Doing stuff")

    # log end of program
    logging.info("Program ended")
    exit(0)

if __name__ == "__main__":
    main()