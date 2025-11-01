# import logging
# import os

# def get_logger(name):
#     os.makedirs("logs", exist_ok=True)
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)
#     handler = logging.FileHandler(f"logs/{name}.log")
#     console = logging.StreamHandler()
#     formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#     handler.setFormatter(formatter)
#     console.setFormatter(formatter)
#     logger.addHandler(handler)
#     logger.addHandler(console)
#     return logger

# src/logger.py

import logging
import os

def get_logger(name: str):
    """Configures and returns a logger for the given module."""
    os.makedirs("logs", exist_ok=True)
    log_file = os.path.join("logs", f"{name}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if the function is called multiple times
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

