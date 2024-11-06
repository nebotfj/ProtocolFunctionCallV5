"""Privacy Protocols Package"""

from .aztec import AZTEC_FUNCTIONS
from .railway import RAILWAY_FUNCTIONS

PRIVACY_PROTOCOLS = {
    'AZTEC': AZTEC_FUNCTIONS,
    'RAILWAY': RAILWAY_FUNCTIONS
}