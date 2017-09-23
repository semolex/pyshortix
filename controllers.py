import sqlite3

from abc import abstractmethod

import config


class BaseController:
    """
    Base class for controllers.
    Used as parent for other controller classes to implement same interface.
    All inherited classes should implement `connect\fetch\make` methods so they can be used seamlessly.
    Initialization uses data from `config` module - so override or change it if needed.

    """
    def __init__(self):
        self.domain = config.BASE_DOMAIN
        self.db_name = config.DEFAULT_DB_NAME
        self.shorten_func = config.DEFAULT_SHORTENER

    def shorten(self, url):
        """
        Method that used defined shortening function.
        Look at `config` module to see what you using.

        :param url: url to be shorten
        :return: result of calling shortening function
        """
        return self.shorten_func(url)

    @abstractmethod
    def connect(self, **kwargs):
        """
        Abstract method that represents database connection.
        Can be empty if database connection is not performed in usual way.

        :param kwargs: kwargs for making connection
        """
        pass

    @abstractmethod
    def fetch(self, short_url):
        """
        Abstract method that represent fetching full URL from storage by using it shortened part (`short_url`).

        :param short_url: short part of the URL
        :return: full versions of URL
        """
        pass

    @abstractmethod
    def make(self, url):
        """
        Abstract method that represents `shorten, save and return result` actions.
        Passed URL is usually stored with shortened version so short version can be used to find full URL.
        Shortened version should be returned as result.
        :param url: URL that needs to be shortened
        :return: shortened version of URL
        """
        pass


class DefaultController(BaseController):
    """
    Default controller, based on `SQLite` usage.
    Do not uses any security handlers, so it is better to use it for demo, testing or internal use.
    """

    def connect(self, **kwargs):
        """
        Implements `connect` method from abstract class.
        Creates connection for db.
        """
        return sqlite3.connect(self.db_name)

    def fetch(self, short_url):
        """
        Implements `fetch` method from abstract class.
        Fetches record db.
        """
        conn = self.connect()
        url = conn.execute("SELECT full_url FROM urls WHERE short_part = '%s'" % short_url).fetchone()[0]
        conn.close()
        return url

    def make(self, url):
        """
        Implements `make` method from abstract class.
        Create short URL, store it in database and return for usage.
        """
        short_part = self.shorten(url)
        conn = self.connect()
        conn.execute("INSERT INTO urls VALUES ('%s', '%s')" % (short_part, url))
        conn.commit()
        conn.close()
        return '{}{}'.format(self.domain, short_part)

# register controllers
CONTROLLERS_LIST = {
    'default_controller': DefaultController
}
