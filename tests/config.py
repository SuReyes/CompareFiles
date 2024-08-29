import cx_Oracle
from crate_common.config import BaseConfiguration

BASE_CONFIG = BaseConfiguration("automated-api-access-code-service")
BASE_CONFIG.load()
LOG_ROTATION_CONFIG = {"max_size": 50000, "keep": 3}
logger = BASE_CONFIG.get_logger("config", LOG_ROTATION_CONFIG)


def get_logger(logger_name):
    """Retrieve a new logger configured as expected

    Uses the environment variables "LOG_LEVEL" and "LOG_PATH"

    Args:
        logger_name (str): The name to use for the logger.

    Returns:
        A logger.
    """
    return BASE_CONFIG.get_logger(logger_name, LOG_ROTATION_CONFIG)


def get(key, default=None):
    """Lookup the value for the requested configuration key

    This checks environment variables first, then falls back to the cloud configuration, if set

    Args:
        key (str): The configuration key whose value is to be retrieved.
        default: The default value to use if no other value was found.

    Returns:
        The value of the key, or the default
    """
    return BASE_CONFIG.get(key, default)


def get_edb_conn():
    url = BASE_CONFIG.get("datasource.edb.url")
    user = BASE_CONFIG.get("datasource.edb.username")
    password = BASE_CONFIG.get("datasource.edb.password")
    connection_url = f"{user}/{password}@{url}"
    conn = cx_Oracle.connect(connection_url)
    return conn
