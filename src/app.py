from textual.app import App
from textual.containers import Grid, VerticalScroll, Horizontal, Vertical
from textual.widgets import Placeholder, Button, Label, DataTable, Rule
from textual.containers import VerticalScroll
from gear_manager import GearManager


class PackManagerApp(App):
    CSS_PATH = "style.tcss"

    GearManager.load_Main_Container()
    current_left_gear_container = GearManager.main_container
    current_right_gear_container = GearManager.main_container


    container_list = GearManager.container_list

    def compose(self):
        with Grid():
            with VerticalScroll(classes="left"):
                
                # Current left container
                with Horizontal(classes="vertical_scroll_row"):
                    with Vertical():
                        yield Label(f"  Container: {PackManagerApp.current_left_gear_container.name}", id="left_container_name")
                        yield Label(f"  {PackManagerApp.current_left_gear_container.description}", id="left_container_description")
                        yield Label(f"  Total weight: {PackManagerApp.current_left_gear_container.total_grams}g\n", id="left_container_total_weight")

                for categoryDict in PackManagerApp.current_left_gear_container.get_Category_Dicts():
                    with Horizontal(classes="vertical_scroll_row"):
                        with Vertical():
                            yield Label(f"\n    Category: {categoryDict['category']}\n    Weight: {categoryDict['category_grams']}g\n")
                            for element in categoryDict["elements"]:
                                with Horizontal(classes="element_frame"):
                                    yield Label(f"      {element.name} | '{element.description}' | {element.grams:,}g   ")
                                    yield Button("-", classes="delete_button")
                                    yield Button(">", classes="move_button")

                

                


                with Vertical(classes="container_buttons_frame_vertical"):
                    yield Rule(line_style="heavy")
                    for container in GearManager.container_list:
                        yield Button(f"{container.name}", classes="change_container_button")

                yield Label("", classes="spacer1")
                


                # All Containers buttons
            with VerticalScroll(classes="right"):
                # Current right container
                yield Label("Container:")
                yield Placeholder(label="Not Implemented",id="plchldr")
                yield Placeholder(label="Not Implemented",id="plchldr1")
                # All Containers buttons


if __name__ == "__main__":
    PackManagerApp().run()