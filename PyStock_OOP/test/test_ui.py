# test_ui.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from item import Item
from inventory import Inventory
from ui import UserInterface

print("=== Testing UserInterface Class ===\n")

# Test 1: Display messages
print("Test 1: Message displays...")
UserInterface.show_success("This is a success message")
UserInterface.show_error("This is an error message")
UserInterface.show_info("This is an info message")
UserInterface.show_warning("This is a warning message")
print()

# Test 2: Menu display
print("Test 2: Menu display...")
UserInterface.show_menu()
print()

# Test 3: Get valid integer
print("Test 3: Get valid integer...")
print("(Try entering: abc, -5, then 10)")
num = UserInterface.get_valid_integer("Enter a number: ", min_value=0)
print(f"You entered: {num}\n")

# Test 4: Get valid float
print("Test 4: Get valid float...")
print("(Try entering: xyz, -2.5, then 15.99)")
price = UserInterface.get_valid_float("Enter price: $", min_value=0.01)
print(f"You entered: ${price:.2f}\n")

# Test 5: Confirm action
print("Test 5: Confirm action...")
confirmed = UserInterface.confirm_action("Do you want to continue?")
print(f"Result: {confirmed}\n")

# Test 6: Display single item
print("Test 6: Display single item...")
item = Item("Test Soap", 345.50, 5, "Grocery")
UserInterface.display_item(item)
print()

# Test 7: Display inventory
print("Test 7: Display inventory...")
inventory = Inventory()
inventory.add_item(Item("Soap", 345.0, 34, "Grocery"))
inventory.add_item(Item("Oil", 456.0, 34, "Grocery"))
inventory.add_item(Item("Fish", 345.0, 8, "Food"))
UserInterface.display_inventory(inventory)
print()

# Test 8: Display categories
print("Test 8: Display categories...")
UserInterface.display_categories(inventory)
print()

# Test 9: Display statistics
print("Test 9: Display statistics...")
stats = inventory.get_statistics()
UserInterface.display_statistics(stats)
print()

# Test 10: Get item details
print("Test 10: Get item details...")
print("Enter sample item details:")
details = UserInterface.get_item_details()
print(f"\nYou entered: {details}")
new_item = Item(*details)
print(f"Created item: {new_item}\n")

# Test 11: Welcome and goodbye
print("Test 11: Welcome and goodbye messages...")
UserInterface.display_welcome(3)
UserInterface.display_goodbye()

print("=== All Tests Complete ===")
