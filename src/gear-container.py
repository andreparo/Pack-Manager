class GearContainer:
    """A container for elements, can be everything from a pack to a closet"""

    def __init__(self, name: str, description: str = ""):

        self.name: str = name
        self.description: str = description

        self.element_container = []
        self.total_grams: int = 0

    

    def add_Element(self, element: object) -> None:
        """Add single element to the list"""
        self.element_container.append(element)
        self.total_grams += element.grams

    
    def add_Element_List(self, elementList: list[object]) -> None:
        """Add list of elements to gear container"""
        for el in elementList:
            self.add_Element(el)