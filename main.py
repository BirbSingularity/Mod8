class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                if ItemToPurchase.item_price != 0:
                    item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0:
                    item.item_quantity = ItemToPurchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    command = ''
    while command != 'q':
        print(menu)
        command = input("Choose an option:\n")
        if command == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_desc = input("Enter the item description:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase()
            new_item.item_name = item_name
            new_item.item_description = item_desc
            new_item.item_price = item_price
            new_item.item_quantity = item_quantity
            cart.add_item(new_item)
        elif command == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        elif command == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            item_to_modify = ItemToPurchase()
            item_to_modify.item_name = item_name
            item_to_modify.item_quantity = quantity
            cart.modify_item(item_to_modify)
        elif command == 'i':
            cart.print_descriptions()
        elif command == 'o':
            cart.print_total()


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
