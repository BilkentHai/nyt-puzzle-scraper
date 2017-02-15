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