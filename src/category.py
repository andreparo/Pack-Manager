from enum import Enum


class Category(Enum):
    """Gear cathegory"""

    BACKPACK = 1
    SLEEP = 2  # * Everything like hammocks, tents, tarps, sleeping bags, quilts, underquilts, sleeping pads, liners
    COOKING = 3  # * Including stoves, fuel, pots, sporks
    CLOTHES = 4
    FOOD = 5
    WATER = 6
    ELECTRONICS = 7
    OTHER = 8
