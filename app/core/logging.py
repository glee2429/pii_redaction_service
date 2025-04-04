from loguru import logger
import sys

def setup_logging():
    logger.add("logs/app.log", rotation="10 MB")
    logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")

