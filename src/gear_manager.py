from serializer import Serializer
from element import Element
from gear_container import GearContainer
from category import Category
from icecream import ic


class GearManager:
    """Manage all operations on gear containers and elements"""

    # * Container with all elements
    main_container: object = None
    container_list: list[object] = []

    @classmethod
    def load_Main_Container(cls) -> None:
        """Load ................................."""
        elementsList: list[object] = Serializer.load_All_Elements()
        # Remove duplicates
        elementsList = list(set(elementsList))
        cls.main_container = GearContainer("main", description="All your gear elements")
        cls.main_container.add_Element_List(elementsList)

        cls.container_list = Serializer.load_All_Containers()

        for container in cls.container_list:
            container.load_Elements(elementsList)

        Serializer.serialize_Elements_List(elementList=elementsList)

        ic(cls.main_container)
        ic(cls.container_list)

    # * Create new container     (copy existing)
    @classmethod
    def create_New_Container(
        cls, name: str, description: str, *, copyExistingByName: str | None = None
    ) -> None:
        """Create new container, if copyExistingByName is not None, a new container with that name will be created"""
        if copyExistingByName is None:
            # Avoid container duplication
            for existingContainer in cls.container_list:
                if name == existingContainer.name:
                    return None
            # Add new empty container
            newCont = GearContainer(name, description)
            cls.container_list.append(newCont)
            Serializer.serialize_Containers_List(cls.container_list)
        else:
            # Avoid container duplication
            if name == copyExistingByName:
                return None
            for existingContainer in cls.container_list:
                if copyExistingByName == existingContainer.name:
                    # Add container copy with new name and description
                    newCont = existingContainer.copy()
                    newCont.name = name
                    newCont.description = description
                    cls.container_list.append(newCont)
                    Serializer.serialize_Containers_List(cls.container_list)
                    return None

    # * Delete container
    @classmethod
    def delete_Container(cls, name: str) -> None:
        """Delete container by name"""
        for ind, existingContainer in enumerate(cls.container_list):
            if name == existingContainer.name:
                cls.container_list.pop(ind)
                Serializer.serialize_Containers_List(cls.container_list)
                return None

    # * Create new element
    @classmethod
    def create_New_Element(
        cls,
        name: str,
        grams: int,
        category: Category,
        *,
        description: str = "",
        base: bool = True,
        wearable: bool = False
    ) -> None:
        """Add new element to main container"""
        newElement = Element(
            name, grams, category, description=description, base=base, wearable=wearable
        )
        cls.main_container.add_Element(newElement)
        Serializer.serialize_Elements_List(cls.main_container.element_container)

    # * Delete element
    @classmethod
    def delete_Element(cls, name: str) -> None:
        """Remove element from main container and from all containers"""
        mainContList: list[object] = cls.main_container.element_container
        for ind, el in enumerate(mainContList):
            if el.name == name:
                mainContList.pop(ind)
                break

        cls.main_container.element_container = mainContList
        Serializer.serialize_Elements_List(cls.main_container.element_container)

        for container in cls.container_list:
            tmpContList: list[object] = container.element_container
            for ind, el in enumerate(tmpContList):
                if el.name == name:
                    tmpContList.pop(ind)
                    break
            container.element_container = tmpContList
        Serializer.serialize_Containers_List(cls.container_list)

    # * Add existing element to container
    @classmethod
    def add_Element_To_Container(cls, element: str, container) -> None:
        """Add already existing element to specified container"""
        # Search target container
        targetCont = None
        for cont in cls.container_list:
            if cont.name == container:
                targetCont = cont
                break
        # Search element
        targetElement = None
        for el in cls.main_container.element_container:
            if el.name == element:
                targetElement = el
                break
        # If container or element are not found
        if targetCont is None or targetElement is None:
            return None

        targetCont.add_Element(el)
        Serializer.serialize_Containers_List(cls.container_list)

    # * Remove element from container
    @classmethod
    def remove_Element_From_Container(cls, element: str, container) -> None:
        """Remove already existing element from specified container"""
        # Search target container
        targetCont = None
        for cont in cls.container_list:
            if cont.name == container:
                targetCont = cont
                break
        if targetCont is None:
            return None
        # Search element
        targetElement = None
        for ind, el in enumerate(targetCont.element_container):
            if el.name == element:
                targetCont.element_container.pop(ind)
                break
        # If container or element are not found
        if targetCont is None or targetElement is None:
            return None
        Serializer.serialize_Containers_List(cls.container_list)
