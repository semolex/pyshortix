""" Set of configuration values. Override them or replace if required."""

from shorteners import SHORTENERS_LIST
from controllers import CONTROLLERS_LIST
from utils.validate import VALIDATORS_LIST

BASE_DOMAIN = 'http://127.0.0.1:5000/'
DEFAULT_SHORTENER = SHORTENERS_LIST['default_random_string']
DEFAULT_CONTROLLER = CONTROLLERS_LIST['default_controller']
DEFAULT_DATABASE = 'sqlite'
DEFAULT_DB_NAME = 'shorts.db'
DEFAULT_DB_PATH = '../'
DEFAULT_VALIDATOR = VALIDATORS_LIST['default_validate']
