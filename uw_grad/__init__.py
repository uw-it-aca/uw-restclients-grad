"""
This is the interface for interacting with the UW Libraries Web Service.
"""

import logging
from dateutil.parser import parse
from uw_pws import PWS
from uw_grad.dao import Grad_DAO
from restclients_core.exceptions import DataFailureException


logger = logging.getLogger(__name__)
DAO = Grad_DAO()
UWPWS = PWS()


def get_resource(url):
    response = DAO.getURL(url, {})
    logger.info("%s ==status==> %s" % (url, response.status))

    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)

    logger.debug("%s ==data==> %s" % (url, response.data))
    return response.data


def parse_datetime(date_string):
    if date_string and len(date_string):
        return parse(date_string)
    return None
