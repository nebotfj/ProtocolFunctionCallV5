"""Infrastructure Protocols Package"""

from .the_graph import THE_GRAPH_FUNCTIONS
from .pocket import POCKET_FUNCTIONS
from .arweave import ARWEAVE_FUNCTIONS

INFRASTRUCTURE_PROTOCOLS = {
    'THE_GRAPH': THE_GRAPH_FUNCTIONS,
    'POCKET': POCKET_FUNCTIONS,
    'ARWEAVE': ARWEAVE_FUNCTIONS
}