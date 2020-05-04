"""
Utilities module for H5-NewsTracker, contains function that are needed by multiple other modules
"""
import sys
import logging
import yaml

config_path = 'config.yml'


def get_logger():
    """H5_News_tracker.controller.utilities.get_logger is used to provide a logger object when needed"""
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    return logger


def load_config_file():
    """H5_News_tracker.controller.utilities.load_config_file is used to load data from a configuration file"""
    try:
        with open(config_path) as file:
            config = yaml.safe_load(file)
            LOGGER.info('Successfully loaded config file')
            return config
    except FileNotFoundError:
        LOGGER.info('Could not find config file, generating new file')
        mk_config_file()
        with open(config_path) as file:
            config = yaml.safe_load(file)
            return config


def mk_config_file():
    """H5_News_tracker.controller.utilities.mk_config_file is used to generate a configuration yaml file"""
    config = dict(
        source=dict(
            cycle_time=6,
            path_to_file=None,
            default_url='https://news.google.com/news/rss',
        ),
        ticker_window=dict(
            font_size=12,
            text_color='white',
            background_color='black',
        )
    )
    with open(config_path, 'w') as outfile:
        yaml.dump(config, outfile)


LOGGER = get_logger()
