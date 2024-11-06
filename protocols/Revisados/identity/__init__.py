"""Identity Protocols Package"""

from .polygon_id import POLYGON_ID_FUNCTIONS
from .brightid import BRIGHTID_FUNCTIONS
from .civic import CIVIC_FUNCTIONS

IDENTITY_PROTOCOLS = {
    'POLYGON_ID': POLYGON_ID_FUNCTIONS,
    'BRIGHTID': BRIGHTID_FUNCTIONS,
    'CIVIC': CIVIC_FUNCTIONS
}