from item import Item

class Inventory:
    """Manages a collection of inventory items"""
    def __init__(self):
        # TODO: Initialize empty dictionary to store items
        self.items = {}  # key = item_name, value = Item object

    def add_item(self, item):
        # TODO: Add or update item in inventory
        # Hint: Check if item.name already exists
        if not isinstance(item, Item):
            print("❌ Error: Must provide an Item object")
            return False
        if item.name in self.items:
          self.items[item.name] = item
          print(f"✅ Updated {item.name}")
        else:
          self.items[item.name] = item
          print(f"✅ Added {item.name}")
        return True
    def remove_item(self, item_name):
        # TODO: Remove item from inventory
        # Return True if removed, False if not found
        if item_name in self.items:
          del self.items[item_name]
          print(f"✅ Removed {item_name}")
          return True
        else:
          print(f"❌ Item '{item_name}' not found")
          return False

    def get_item(self, item_name):
        # TODO: Return Item object or None if not found
        return self.items.get(item_name)
    def get_all_items(self):
        # TODO: Return list of all Item objects
        return list(self.items.values())

    def search_by_category(self, category):
        # TODO: Return list of items in given category
        # Hint: Loop through items, filter by category
        found_item = []
        for item in self.items.values():
            if item.category.lower() == category.lower():
                found_item.append(item)
        return found_item

    def get_categories(self):
        # TODO: Return set of all unique categories
        unique_category = set()
        for item in self.items.values():
          unique_category.add(item.category)
        return unique_category

    def get_low_stock_items(self, threshold=10):
        # TODO: Return list of items with low stock
        low_stock_items = []
        for item in self.items.values():
            if item.is_low_stock(threshold):
                low_stock_items.append(item)
        return low_stock_items

    def calculate_total_value(self):
        # TODO: Calculate total inventory value
        # Hint: Sum all item.get_value()
        total = 0
        for item in self.items.values():
          total += item.get_value()
        return total

    def get_statistics(self):
        # TODO: Return dictionary with stats:
        stats = {
             "total_items": len(self.items),
             "total_value": self.calculate_total_value(),
             "categories_count": len(self.get_categories()),
             "low_stock_count": len(self.get_low_stock_items())
         }
        return stats

    def __len__(self):
        # TODO: Return number of items
        # Hint: This allows len(inventory) to work
        return len(self.items)

    def __str__(self):
        stats = self.get_statistics()
        return (f"Inventory Summary:\n"
                f"  Total Items: {stats['total_items']}\n"
                f"  Total Value: ${stats['total_value']:.2f}\n"
                f"  Categories: {stats['categories_count']}\n"
                f"  Low Stock Items: {stats['low_stock_count']}")
