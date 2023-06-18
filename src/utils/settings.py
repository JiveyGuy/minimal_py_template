import configparser as config_parser

def get_settings():
    # read settings
    settings = load_settings()

    # check if this is the first time the program is run
    if not settings.has_section("General"):
        make_default_settings()
        settings = load_settings()

    return settings

def make_default_settings():
    # first time run, create default settings
    config = config_parser.RawConfigParser()
    
    # general settings
    config.add_section("General")
    config.set("General", "log_level", "DEBUG")
    config.set("General", "print_log", True)

    # path settings
    config.add_section("Path")
    config.set("Path", "data", "data")
    config.set("Path", "log", "data/logs")
    
    # save settings to file
    with open("data/settings.cfg", "w") as config_file:
        config.write(config_file)

def load_settings(settings_path="data/settings.cfg"):
    # load settings from file
    config = config_parser.ConfigParser()
    config.read(settings_path)
    return config

