def show_menu():
    print("\n" + "="*40)
    print("📦 PyStock Inventory Management System")
    print("="*40)
    print("1. Add/Update Item")
    print("2. View All Inventory")
    print("3. View Categories & Stock")
    print("4. Save & Exit")
    print("="*40)

def main():
  global inventory
  inventory = load_inventory()
  print(f"📦 Loaded {len(inventory)} items from storage")
  while True:
    show_menu()
    choice = input("Enter a choice: ")

    if choice == "1":
      add_update_item(inventory)
    elif choice == "2":
      view_item(inventory)
    elif choice == "3":
      view_stock(inventory)
    elif choice == "4":
      save_inventory(inventory)
      break
    else:
      print("Invalid Choice!")


def get_valid_int_score(prompt):
  while True:
    try:
      score = int(input(prompt))
      if score >= 0:
        return score
      else:
        print("❌ Please enter a positive number.")
    except ValueError:
      print("❌ Please enter a valid Score.")

def get_valid_float_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if score >= 0:
                return score
            else:
                print("❌ Please enter a positive number.")
        except ValueError:
            print("❌ Please enter a valid number (e.g., 15.50)")

def add_update_item(current_inventory):
  item_name = input("Enter an item name: ")
  item_exist = item_name in current_inventory

  price_data = get_valid_float_score("Enter Price: ")
  Stock_data = get_valid_int_score("Enter Stock: ")
  category_data = input("Enter Category: ")

  if item_exist:
    current_inventory[item_name].update({"price": price_data, "stock": Stock_data, "category": category_data})
    print(f"Updated {item_name}")
  else:
    current_inventory[item_name] = {
      "price": price_data,
      "stock": Stock_data,
      "category": category_data
    }
    print(f"Added new item '{item_name}'")

def view_item(current_inventory):
  print("--- Current Inventory ---")
  for items_name, details in current_inventory.items():
    print(f"{items_name} (category: {details['category']})")
    print(f"price: {details['price']: .2f} | stock: {details['stock']}")

def view_stock(current_inventory):
    categories = set()
    for items_data in current_inventory.values():
        categories.add(items_data["category"])
    print("Available Categories:", categories)

    category_choice = input("Enter category to view items (or press Enter to skip): ")
    if category_choice:
        print(f"\n--- Items in category: {category_choice} ---")
        found_items = False
        for item_name, details in current_inventory.items():
            if details["category"].lower() == category_choice.lower():
                print(f"{item_name} - Price: ${details['price']:.2f} | Stock: {details['stock']}")
                found_items = True
        if not found_items:
            print("No items found in this category.")

def save_inventory(current_inventory, filename="PyStock.txt"):
    try:
        with open(filename, "w") as file:
            for item_name, details in current_inventory.items():
                file.write(f"{item_name}|{details['price']}|{details['stock']}|{details['category']}\n")
        print("✅ Inventory saved successfully!")
    except Exception as e:
        print(f"❌ Error saving inventory: {e}")

def load_inventory(filename="PyStock.txt"):
    inventory = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                inventory[parts[0]] = {
                  "price" : float(parts[1]),
                  "stock" : int(parts[2]),
                  "category" : parts[3]
                }
    except FileNotFoundError:
        print("No existing inventory file found. Starting with empty inventory.")
    except Exception as e:
        print(f"Error loading inventory: {e}")
    return inventory

main()

