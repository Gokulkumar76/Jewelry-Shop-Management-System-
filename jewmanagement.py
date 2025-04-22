class JewelryItem:
    def __init__(self, item_id, name, type_, weight, price, stock):
        self.item_id = item_id
        self.name = name
        self.type = type_
        self.weight = weight
        self.price = price
        self.stock = stock

    def display(self):
        print(f"ID: {self.item_id}, Name: {self.name}, Type: {self.type}, "
              f"Weight: {self.weight}g, Price: ${self.price}, Stock: {self.stock}")
# this to create a object using it
class JewelryShop:
    def __init__(self):
        self.inventory = []

    def add_item(self):
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        type_ = input("Enter type (e.g., ring, necklace): ")
        weight = float(input("Enter weight in grams: "))
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        item = JewelryItem(item_id, name, type_, weight, price, stock)
        self.inventory.append(item)
        print("Item added successfully!\n")
# tis is to view jewls
    def view_items(self):
        if not self.inventory:
            print("No items in inventory.")
            return
        print("\n--- Inventory ---")
        for item in self.inventory:
            item.display()
        print()

    def search_item(self):
        keyword = input("Enter item name or type to search: ").lower()
        found = False
        for item in self.inventory:
            if keyword in item.name.lower() or keyword in item.type.lower():
                item.display()
                found = True
        if not found:
            print("No matching items found.\n")

    def sell_item(self):
        item_id = input("Enter item ID to sell: ")
        quantity = int(input("Enter quantity to sell: "))
        for item in self.inventory:
            if item.item_id == item_id:
                if item.stock >= quantity:
                    item.stock -= quantity
                    total_price = item.price * quantity
                    print(f"Sold {quantity} x {item.name}. Total: ${total_price:.2f}\n")
                    return
                else:
                    print("Not enough stock.\n")
                    return
        print("Item not found.\n")

    def run(self):
        while True:
            print("1. Add Item\n2. View Items\n3. Search Item\n4. Sell Item\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.view_items()
            elif choice == '3':
                self.search_item()
            elif choice == '4':
                self.sell_item()
            elif choice == '5':
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid choice.\n")

if __name__ == "__main__":
    shop = JewelryShop()
    shop.run()
