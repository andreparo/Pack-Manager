from gear_manager import GearManager
from category import Category

if __name__ == "__main__":
    GearManager.load_Main_Container()
    GearManager.create_New_Container("test container 2", "this container doesn't exist")
    GearManager.create_New_Container("test container 5", "this container doesn't exist")
    GearManager.delete_Container("test container 2")

    #GearManager.create_New_Element("test 8", 0, category=Category.OTHER, description="test item 1")
    GearManager.delete_Element("test 8")
