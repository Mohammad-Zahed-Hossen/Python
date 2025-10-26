# test_item.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from item import Item

print("=== Testing Item Class ===\n")

# Test 1: Create item
print("Test 1: Creating item...")
soap = Item("Soap", 345.0, 34, "Grocery")
print(soap)  # Uses __str__
print("✅ Item created successfully\n")

# Test 2: Update price
print("Test 2: Updating price...")
result = soap.update_price(350.0)
print(f"Update successful: {result}")
print(f"New price: ${soap.price}\n")

# Test 3: Invalid price
print("Test 3: Invalid price...")
result = soap.update_price(-10)
print(f"Update successful: {result}\n")

# Test 4: Restock
print("Test 4: Restocking...")
result = soap.restock(10)
print(f"Restock successful: {result}")
print(f"New stock: {soap.stock}\n")

# Test 5: Sell
print("Test 5: Selling...")
result = soap.sell(5)
print(f"Sale successful: {result}")
print(f"Remaining stock: {soap.stock}\n")

# Test 6: Sell too many
print("Test 6: Selling more than available...")
result = soap.sell(100)
print(f"Sale successful: {result}\n")

# Test 7: Low stock check
print("Test 7: Checking low stock...")
is_low = soap.is_low_stock(50)
print(f"Is low stock: {is_low}\n")

# Test 8: Calculate value
print("Test 8: Calculating value...")
value = soap.get_value()
print(f"Total value: ${value:.2f}\n")

# Test 9: File format
print("Test 9: File format conversion...")
file_line = soap.to_file_format()
print(f"File format: {file_line}")

# Test 10: Create from file
print("\nTest 10: Creating from file format...")
new_item = Item.from_file_format(file_line)
print(f"Loaded item: {new_item}\n")

print("=== All Tests Complete ===")
