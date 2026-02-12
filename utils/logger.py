import logging
import os

def get_logger(name):
    # 1. Create the logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 2. Prevent duplicate logs if run multiple times
    if logger.hasHandlers():
        return logger

    # 3. Create a file handler (Writes to app.log)
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)

    # 4. Create a console handler (Prints to screen)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 5. Define format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 6. Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger