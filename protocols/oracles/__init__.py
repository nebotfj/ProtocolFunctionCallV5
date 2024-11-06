"""Oracle Protocols Package"""

from .chainlink import CHAINLINK_FUNCTIONS
from .pyth import PYTH_FUNCTIONS
from .uma import UMA_FUNCTIONS
from .api3 import API3_FUNCTIONS
from .tellor import TELLOR_FUNCTIONS
from .band import BAND_FUNCTIONS
from .dia import DIA_FUNCTIONS
from .umbrella import UMBRELLA_FUNCTIONS

ORACLE_PROTOCOLS = {
    'CHAINLINK': CHAINLINK_FUNCTIONS,
    'PYTH': PYTH_FUNCTIONS,
    'UMA': UMA_FUNCTIONS,
    'API3': API3_FUNCTIONS,
    'TELLOR': TELLOR_FUNCTIONS,
    'BAND': BAND_FUNCTIONS,
    'DIA': DIA_FUNCTIONS,
    'UMBRELLA': UMBRELLA_FUNCTIONS
}