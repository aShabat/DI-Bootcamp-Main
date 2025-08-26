from menu_manager import MenuManager  # pyright: ignore[reportImplicitRelativeImport]
from menu_item import MenuItem  # pyright: ignore[reportImplicitRelativeImport]


class MenuEditor:
    def __init__(self) -> None:
        self.__menu_manager = MenuManager()

    def add_item_to_menu(self):
        while True:
            name = input("Item name: ").strip()
            if len(name) > 30:
                print("Item name can have maximum 30 characters.")
            elif len(name) == 0:
                print("Item name can't be empty")
            else:
                break

        while True:
            price_input = input("Item price(default = 0): ")
            if price_input == "":
                price = 0
                break
            try:
                price = int(price_input)
                if price < 0:
                    print("Item price can't be negative.")
                else:
                    break
            except:
                print("Item price must be a positive integer.")

        new_item = MenuItem(name=name, price=price)
        if new_item.save():
            print("Item was added successfully.")
        else:
            print("there was an error when adding an item.")

    def remove_item_from_menu(self):
        name = input("Item name: ").strip()

        item = MenuItem(name=name)
        if item.delete():
            print("Item succesfully deleted.")
        else:
            print("there was an error when deleting an item.")

    def update_item_from_menu(self):
        while True:
            name = input("Item name: ").strip()
            if len(name) > 30:
                print("Item name can have maximum 30 characters.")
            elif len(name) == 0:
                print("Item name can't be empty")
            else:
                break
        while True:
            new_name = input("New item name: ").strip()
            if len(name) > 30:
                print("Item name can have maximum 30 characters.")
            elif len(name) == 0:
                print("Item name can't be empty")
            else:
                break

        while True:
            price_input = input("New item price(default = 0): ")
            if price_input == "":
                new_price = 0
                break
            try:
                new_price = int(price_input)
                if new_price < 0:
                    print("Item price can't be negative.")
                else:
                    break
            except:
                print("Item price must be a positive integer.")

        item = MenuItem(name=name)
        if item.update(name=new_name, price=new_price):
            print("Item was updated successfully.")
        else:
            print("there was an error when updating an item.")

    def show_item(self):
        name = input("Item name: ").strip()
        item = self.__menu_manager.get_by_name(name)
        if item is not None:
            print(f"Item: {item.name} -- {item.price} $.")
        else:
            print(f"No item with a name '{name}'.")

    def show_restaurant_menu(self):
        print("Menu:")
        for item in self.__menu_manager.all_items():
            print(f"\t{item.name} -- {item.price} $")

    def show_user_menu(self):
        while True:
            print("*" * 20)
            user_command = input(
                """
(V)iew an item
(A)dd an item
(D)elete an item
(U)pdate an item
(S)how the menu
(E)xit
your command: """
            )
            user_command = user_command[0].lower()

            print("*" * 20)
            if user_command == "v":
                self.show_item()
            elif user_command == "a":
                self.add_item_to_menu()
            elif user_command == "d":
                self.remove_item_from_menu()
            elif user_command == "u":
                self.update_item_from_menu()
            elif user_command == "s":
                self.show_restaurant_menu()
            elif user_command == "e":
                self.show_restaurant_menu()
                break
            else:
                print("Didn't recognize the command.")


if __name__ == "__main__":
    MenuEditor().show_user_menu()
