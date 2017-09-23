import random
import uuid

from string import ascii_lowercase
from string import ascii_uppercase
from string import digits


def _uuid_shorten(url=None, **kwargs):
    """
    Shorten function based on UUID.
    String with replaced hyphens will be returned.

    :param url: url string, used for generating UUID.
    :param kwargs: kwargs (not used).
    :return: uuid string with replaced hyphens.
    """
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, name=url)).replace('-', '')


def _random_string_shorten(url=None, **kwargs):
    """
    Shorten function, based on random string generation.
    `url` param is not used, but present for matching general signature.
    Length of 8 symbols is used for generating shorten part.

    :param url: url for shortening (not used)
    :param kwargs: kwargs (not used)
    :return: random string with digits, uppercase and lowercase ascii symbols.
    """
    shortened = ''.join(random.SystemRandom().choice(ascii_uppercase + digits + ascii_lowercase) for _ in range(8))
    return shortened

# register shorten functions
SHORTENERS_LIST = {
    'default_random_string': _random_string_shorten,
    'default_uuid': _uuid_shorten
}
