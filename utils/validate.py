from urllib.parse import urlparse


def default_validation(url):
    """
    Default simple validation function.
    Uses `urllib.parse.urlparse` for checking schema of given URL.
    :param url: URL string for validating
    :return: boolean that indicates if URL valid
    """
    return bool(urlparse(url).scheme)

# register validators
VALIDATORS_LIST = {
    'default_validate': default_validation
}
