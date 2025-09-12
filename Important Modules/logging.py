#The logging module in Python is a built-in, standard library module that provides 
# a flexible and powerful framework for emitting log messages from Python programs. 
# It is a crucial tool for debugging, monitoring, and understanding the behavior of 
# applications, especially in complex or production environment

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
)

logging.info("App started successfully")
logging.warning("Low disk space")
logging.error("Database connection failed")
