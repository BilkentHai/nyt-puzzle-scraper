import sys, os

# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

from scraper import scrape
from pymongo import MongoClient
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name

    logger.info("Your cron function " + name + " ran at " + str(current_time))

    connection_string = open("connection_string", "r").read()

    db = MongoClient(connection_string).huseyin
    puzzles = db.puzzles


    puzzle = scrape()

    puzzles.insert_one(puzzle)