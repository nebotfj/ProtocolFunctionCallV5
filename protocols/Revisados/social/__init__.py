"""Social Protocols Package"""

from .lens import LENS_FUNCTIONS
from .farcaster import FARCASTER_FUNCTIONS
from .friend_tech import FRIEND_TECH_FUNCTIONS

SOCIAL_PROTOCOLS = {
    'LENS': LENS_FUNCTIONS,
    'FARCASTER': FARCASTER_FUNCTIONS,
    'FRIEND_TECH': FRIEND_TECH_FUNCTIONS
}