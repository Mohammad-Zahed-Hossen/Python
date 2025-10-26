import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from item import Item
from inventory import Inventory

print("=== Testing Inventory Class ===\n")

# Create inventory
inv = Inventory()
print(f"Initial size: {len(inv)}\n")

# Test 1: Add items
print("Test 1: Adding items...")
soap = Item("Soap", 345.0, 34, "Grocery")
oil = Item("Oil", 456.0, 34, "Grocery")
fish = Item("Fish", 345.0, 8, "Food")  # Low stock!

inv.add_item(soap)
inv.add_item(oil)
inv.add_item(fish)
print(f"Total items: {len(inv)}\n")

# Test 2: Get all items
print("Test 2: Getting all items...")
all_items = inv.get_all_items()
for item in all_items:
    print(f"  {item}")
print()

# Test 3: Search by category
print("Test 3: Searching by category...")
grocery_items = inv.search_by_category("Grocery")
print(f"Found {len(grocery_items)} grocery items:")
for item in grocery_items:
    print(f"  {item.name}")
print()

# Test 4: Get categories
print("Test 4: Getting categories...")
categories = inv.get_categories()
print(f"Categories: {categories}\n")

# Test 5: Low stock items
print("Test 5: Checking low stock...")
low_stock = inv.get_low_stock_items(threshold=10)
print(f"Found {len(low_stock)} low stock items:")
for item in low_stock:
    print(f"  {item.name} - {item.stock} units")
print()

# Test 6: Total value
print("Test 6: Calculating total value...")
total_value = inv.calculate_total_value()
print(f"Total inventory value: ${total_value:.2f}\n")

# Test 7: Statistics
print("Test 7: Getting statistics...")
stats = inv.get_statistics()
print("Statistics:")
for key, value in stats.items():
    print(f"  {key}: {value}")
print()

# Test 8: Update item
print("Test 8: Updating item...")
updated_soap = Item("Soap", 350.0, 50, "Grocery")
inv.add_item(updated_soap)
item = inv.get_item("Soap")
print(f"Updated item: {item}\n")

# Test 9: Remove item
print("Test 9: Removing item...")
inv.remove_item("Fish")
print(f"Items remaining: {len(inv)}\n")

# Test 10: Inventory summary
print("Test 10: Inventory summary...")
print(inv)

print("\n=== All Tests Complete ===")
