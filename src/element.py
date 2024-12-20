from category import Category


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
        wearable: bool = False,
    ):
        """Element constructor"""
        self.name: str = name
        self.grams: int = grams
        self.category: Category = category
        self.description: str = description
        self.base: bool = base
        self.wearable: bool = wearable
        self.worn: bool = False

    def to_Json(self) -> dict:
        """Return json dict used to serailize and reinitialize object"""
        return {
            "name": self.name,
            "grams": self.grams,
            "category": self.category.value,
            "description": self.description,
            "base": self.base,
            "wearable": self.wearable,
        }

    def __str__(self) -> str:
        opt = "|"
        if self.base is True:
            opt = opt + " base |"
        if self.wearable is True:
            opt = opt + " wearable |"
        return (
            f"{self.name} | {self.category} | {self.grams} | {self.description} {opt}"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)
