from src.category import Category


class Element:
    """Class representing an element in equipment gear"""

    def __init__(
        self,
        name: str,
        grams: int,
        category: Category,
        *,
        description: str = "",
        base: bool = True,
        wearable: bool = False
    ):
        """Element constructor"""

        self.name: str = name
        self.grams: int = grams
        self.base: bool = base
        self.wearable: bool = wearable
        self.worn: bool = False


    
    to_Json