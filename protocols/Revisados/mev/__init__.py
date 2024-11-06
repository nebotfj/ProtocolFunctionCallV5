"""MEV Protection Protocols Package"""

from .cowswap import COWSWAP_FUNCTIONS
from .rook import ROOK_FUNCTIONS
from .eden import EDEN_FUNCTIONS

MEV_PROTOCOLS = {
    'COWSWAP': COWSWAP_FUNCTIONS,
    'ROOK': ROOK_FUNCTIONS,
    'EDEN': EDEN_FUNCTIONS
}