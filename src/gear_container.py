class GearContainer:
    """A container for elements, can be everything from a pack to a closet"""

    def __init__(
        self, name: str, description: str = "", referenceList: list[str] = None
    ):
        """Container Constructor"""
        self.name: str = name
        self.description: str = description

        self.element_container: list[object] = []
        self.reference_list: list[str] = referenceList
        self.total_grams: int = 0

    def load_Elements(self, elementList: list[object]) -> None:
        """Saves element that match the referenceList"""
        if self.reference_list is None:
            return None
        for element in elementList:
            n = element.name
            for ref in self.reference_list:
                if n == ref:
                    self.add_Element(element)
                    break

    def add_Element(self, element: object) -> None:
        """Add single element to the list"""
        self.element_container.append(element)
        self.total_grams += element.grams

    def add_Element_List(self, elementList: list[object]) -> None:
        """Add list of elements to gear container"""
        for el in elementList:
            self.add_Element(el)

    def extract_Element_References_List(self) -> list[str]:
        """Extract list of element names"""
        out = []
        for el in self.element_container:
            out.append(el.name)
        return out

    def to_Json(self) -> dict:
        """Return json dict used to serailize and reinitialize object"""
        return {
            "name": self.name,
            "description": self.description,
            "element_references": self.extract_Element_References_List(),
        }

    def __str__(self) -> str:
        return f"{self.name} | '{self.description}' | {self.extract_Element_References_List()}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


    def get_Category_Dicts(self) -> list[dict]:
        """Return elements divided by category in separate dict"""
        out = []
        for element in self.element_container:
            
            newCategory = True
            for categoryDict in out:
                if categoryDict["category"] == element.category.name:
                    newCategory = False
                    categoryDict["elements"].append(element)
                    categoryDict["category_grams"] += element.grams
            
            if newCategory is True:
                out.append({"category": element.category.name, "category_grams": element.grams, "elements": [element]})

        return out

            