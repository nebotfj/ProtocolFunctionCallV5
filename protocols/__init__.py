"""Protocol Functions Package"""

# Import existing protocols
from .uniswap import UNISWAP_FUNCTIONS
# ... (previous imports remain the same)

# Import new protocol categories
from .options import OPTIONS_PROTOCOLS
from .oracles import ORACLE_PROTOCOLS
from .perps import PERPETUAL_PROTOCOLS
from .derivatives import DERIVATIVES_PROTOCOLS

# Update PROTOCOLS dictionary
PROTOCOLS.update({
    'OPTIONS': OPTIONS_PROTOCOLS,
    'ORACLES': ORACLE_PROTOCOLS,
    'PERPETUALS': PERPETUAL_PROTOCOLS,
    'DERIVATIVES': DERIVATIVES_PROTOCOLS
})