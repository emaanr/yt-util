# This file will allow interface with the functions via CLI through argparse

import sys
import logging
import datetime
from argparse import ArgumentParser
from resource import getrusage, RUSAGE_SELF
import functions as functions

# _Parser class implements argparse
# Called in __name__ == "__main__"

class _Parser:
    
    def _init_(self):

        usage = "python cli.py --arg1 <arg1> [--opt-arg1] <opt-arg1>"
        self.parser = ArgumentParser(usage=usage)

# CLI Params
        self.parser.add_argument(
            "--arg1",
            required=True,
            dest="arg",
            help="What is this? \
                Another line if needed."
        )

        self.parser.add_argument(
            "--opt-arg1",
            required=False,
            default="Define a default value if needed",
            dest="opt-arg1",
            help="What is this? \
                Another line if needed."
        )

# Return Namespace object contained parsed arguments
    def parse(self):
        return self.parser.parse_args()
    

# Set up logging to both the console and appropriate log files
def _setup_logging(filename):

    # Get Logger and set Level
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Define Log Format
    logDateFormat = '%m/%d/%Y %I:%M:%S %p'
    logFormat = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s", datefmt=logDateFormat)

    # Console
    log_console = logging.StreamHandler(sys.stdout)
    log_console.setFormatter(logFormat)
    logger.addHandler(log_console)

    # Log File
    filepath = f"./logging/{filename}"
    log_file = logging.FileHandler(filepath)
    log_file.setFormatter(logFormat)
    logger.addHandler(log_file)

    return logger

# Main routine for __name__ == "__main__" program direct execution
def main(args, logger):

    successful = True

    try:
        stage = "Stage"
    except Exception as e:
        logger.error(f'Failure at "{stage}" Stage: {e}')
        logger.error(f'Failure Arguemnts: {args}')
        successful = False

    return successful

# Program direct execution
if __name__ == "__main__":

    # Start Time
    start = datetime.datetime.now()

    # Logger
    logger = _setup_logging("yt_util.log")
    logger.info("Program Started")

    # Program Status
    successful = False

    # Parser
    parser = _Parser()
    args = parser.parse()
    successful = main(args, logger)

    # End Time
    end = datetime.datetime.now()

    # Diagnostics
    logger.info(f"Runtime: {end - start}")
    logger.info(f"Peak Memory Usage: {getrusage(RUSAGE_SELF).ru_maxrss/1024:,.2f} MB") # 1 MB = 1024 KB

    # Results
    if successful:
        logger.info("Program Completed Successfully")
    else:
        logger.error("Program Aborted with Error")
        sys.exit(1) # Unsuccessful Exit signaled by passing a value other than 0 or None