import logging


def initialize_wc_logger():
    logger = logging.getLogger('wc_logger')

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s [%(asctime)s] - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
