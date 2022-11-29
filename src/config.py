from dotenv import load_dotenv
from orator import DatabaseManager, Model
import os
import logging

# Init environment
load_dotenv(dotenv_path='.env.yaml')

# Enable debug mode.
DEBUG = os.getenv("debug")
MODE = os.getenv("mode")

# Init log
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",filename='logs/log.log', level=logging.INFO)

DB = DatabaseManager({
    'mysql': {
        'driver': os.getenv("driver"),
        'host': os.getenv("host"),
        'database': os.getenv("database"),
        'user': os.getenv("user"),
        'password': os.getenv("password"),
        'prefix': ''
    }
})

Model.set_connection_resolver(DB)
