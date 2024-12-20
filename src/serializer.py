from pathlib import PurePath
from element import Element
from category import Category
from gear_container import GearContainer
import os
import json
from icecream import ic


class Serializer:

    __PROJECT_DIR_PATH = PurePath(__file__).parent.parent
    __GEAR_CONTAINERS_PATH = __PROJECT_DIR_PATH.joinpath("data", "gear_containers.json")
    __ELEMENTS_PATH = __PROJECT_DIR_PATH.joinpath("data", "elements.json")

    __elements: list[dict] = []
    __containers: list[dict] = []

    @classmethod
    def serialize_Element(cls, element: object, save: bool = True) -> None:
        """Save element to json file"""
        if element is not None:
            cls.__elements.append(element.to_Json())
        else:
            cls.__elements = []
        if save is True:
            with open(cls.__ELEMENTS_PATH, "w") as elementJson:
                json.dump(cls.__elements, elementJson)

    @classmethod
    def serialize_Elements_List(cls, elementList: list[object]) -> None:
        """Save element list to json file"""
        elementList = list(set(elementList))
        cls.__elements = []
        lastListIndex = len(elementList) - 1
        if lastListIndex == -1:
            cls.serialize_Element(None, save=True)
            return None
        for i in range(lastListIndex):
            cls.serialize_Element(elementList[i], save=False)
        cls.serialize_Element(elementList[lastListIndex], save=True)

    @classmethod
    def load_All_Elements(cls) -> list[object]:
        """Load all existing elements from json files"""
        with open(cls.__ELEMENTS_PATH, "r") as elementJson:
            cls.__elements = json.load(elementJson)
        out = []
        for elementDict in cls.__elements:
            out.append(
                Element(
                    name=elementDict["name"],
                    grams=elementDict["grams"],
                    category=Category(elementDict["category"]),
                    description=elementDict["description"],
                    base=elementDict["base"],
                    wearable=elementDict["wearable"],
                )
            )
        return list(set(out))

    @classmethod
    def serialize_Container(cls, container: object, save: bool = True) -> None:
        """Save container to json file, elements are turned into a reference by name, if save is false, only appending to class list"""
        if container is not None:
            cls.__containers.append(container.to_Json())
        else:
            cls.__containers = []

        if save is True:
            with open(cls.__GEAR_CONTAINERS_PATH, "w") as containersJson:
                json.dump(cls.__containers, containersJson)

    @classmethod
    def serialize_Containers_List(cls, containerList: list[object]) -> None:
        """Save container list to json file, elements are turned into a reference by name"""
        containerList = list(set(containerList))
        cls.__containers = []
        lastListIndex = len(ic(containerList)) - 1
        if lastListIndex == -1:
            cls.serialize_Container(None, save=True)
            return None

        for i in range(lastListIndex):  # Serialize all elements the last one
            cls.serialize_Container(containerList[i], save=False)
        # Serialize the last one and save all
        cls.serialize_Container(containerList[ic(lastListIndex)], save=True)

    @classmethod
    def load_All_Containers(cls) -> list[object]:
        """Load all existing containers from json files"""
        with open(cls.__GEAR_CONTAINERS_PATH, "r") as containersJson:
            cls.__containers = json.load(containersJson)
        out = []
        for containerDict in cls.__containers:
            out.append(
                GearContainer(
                    name=containerDict["name"],
                    description=containerDict["description"],
                    referenceList=containerDict["element_references"],
                )
            )
        return list(set(out))
