import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from item import Item
from inventory import Inventory
from file_manager import FileManager

print("=== Testing FileManager Class ===\n")

# Test 1: Create FileManager
print("Test 1: Creating FileManager...")
fm = FileManager("test_inventory.txt")
print(f"✅ FileManager created with file: {fm.filename}\n")

# Test 2: Create sample inventory
print("Test 2: Creating sample inventory...")
inventory = Inventory()
inventory.add_item(Item("Soap", 345.0, 34, "Grocery"))
inventory.add_item(Item("Oil", 456.0, 34, "Grocery"))
inventory.add_item(Item("Fish", 345.0, 8, "Food"))
inventory.add_item(Item("Meat", 678.0, 34, "Food"))
print(f"Created inventory with {len(inventory)} items\n")

# Test 3: Save inventory
print("Test 3: Saving inventory to file...")
fm.save_inventory(inventory)
print()

# Test 4: Load inventory
print("Test 4: Loading inventory from file...")
loaded_inventory = fm.load_inventory()
print(f"Loaded inventory has {len(loaded_inventory)} items")

# Display loaded items
print("\nLoaded items:")
for item in loaded_inventory.get_all_items():
    print(f"  {item}")
print()

# Test 5: Verify data integrity
print("Test 5: Verifying data integrity...")
original_items = inventory.get_all_items()
loaded_items = loaded_inventory.get_all_items()

print(f"Original count: {len(original_items)}")
print(f"Loaded count: {len(loaded_items)}")

if len(original_items) == len(loaded_items):
    print("✅ Item counts match!")
else:
    print("❌ Item counts don't match!")
print()

# Test 6: Create backup
print("Test 6: Creating backup...")
backup_file = fm.create_backup(inventory)
if backup_file:
    print(f"✅ Backup created: {backup_file}")
print()

# Test 7: Export to CSV
print("Test 7: Exporting to CSV...")
fm.export_to_csv(inventory, "test_inventory.csv")
print()

# Test 8: Test with non-existent file
print("Test 8: Loading from non-existent file...")
fm_new = FileManager("doesnt_exist.txt")
empty_inventory = fm_new.load_inventory()
print(f"Loaded {len(empty_inventory)} items (should be 0)\n")

# Test 9: Validate file lines
print("Test 9: Testing line validation...")
valid_line = "Soap|345.0|34|Grocery"
invalid_line1 = "Soap|abc|34|Grocery"  # Invalid price
invalid_line2 = "Soap|345.0|34"  # Missing category
invalid_line3 = "Soap|345.0|abc|Grocery"  # Invalid stock

print(f"Valid line: {FileManager.validate_file_line(valid_line)}")
print(f"Invalid line 1: {FileManager.validate_file_line(invalid_line1)}")
print(f"Invalid line 2: {FileManager.validate_file_line(invalid_line2)}")
print(f"Invalid line 3: {FileManager.validate_file_line(invalid_line3)}")
print()

# Test 10: Read actual file content
print("Test 10: Verifying file content...")
try:
    with open("test_inventory.txt", 'r') as f:
        content = f.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print("File not found!")

print("\n=== All Tests Complete ===")
