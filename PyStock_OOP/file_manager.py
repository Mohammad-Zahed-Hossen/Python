# file_manager.py
from inventory import Inventory
from item import Item
from datetime import datetime

class FileManager:
    """Handles file operations for inventory persistence"""

    def __init__(self, filename="PyStock.txt"):
        """Initialize with filename"""
        self.filename = filename

    def load_inventory(self):
        """Read file, create Item objects, return Inventory"""
        inventory = Inventory()  # Create NEW Inventory object

        try:
            with open(self.filename, 'r') as file:  # Use self.filename!
                lines = file.readlines()  # Read ALL lines

                loaded_count = 0
                for line in lines:
                    line = line.strip()  # Remove whitespace

                    if not line:  # Skip empty lines
                        continue

                    # Validate line format first
                    if self.validate_file_line(line):
                        item = Item.from_file_format(line)
                        if item:  # If successfully created
                            inventory.add_item(item)
                            loaded_count += 1
                    else:
                        print(f"⚠️ Skipping invalid line: {line}")

                print(f"✅ Loaded {loaded_count} items from {self.filename}")

        except FileNotFoundError:
            print(f"📁 No existing file '{self.filename}' found. Starting with empty inventory.")

        except Exception as e:
            print(f"❌ Error loading inventory: {e}")

        return inventory  

    def save_inventory(self, inventory):
        """Write all items to file"""
        try:
            with open(self.filename, 'w') as file:
                # Get all Item objects (not dict items!)
                items = inventory.get_all_items()

                for item in items:
                    # Convert each item to file format and write
                    line = item.to_file_format()
                    file.write(line + '\n')  # Add newline!

                print(f"✅ Saved {len(items)} items to {self.filename}")
                return True

        except Exception as e:
            print(f"❌ Error saving inventory: {e}")
            return False

    def create_backup(self, inventory):
        """Save to backup file with timestamp"""
        try:
            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_filename = f"PyStock_backup_{timestamp}.txt"

            with open(backup_filename, 'w') as file:
                items = inventory.get_all_items()

                for item in items:
                    file.write(item.to_file_format() + '\n')

                print(f"✅ Backup created: {backup_filename}")
                return backup_filename

        except Exception as e:
            print(f"❌ Error creating backup: {e}")
            return None

    def export_to_csv(self, inventory, csv_filename):
        """Export inventory to CSV format"""
        try:
            with open(csv_filename, 'w') as file:
                # Write CSV header
                file.write("Name,Price,Stock,Category,Total Value\n")

                # Write each item
                items = inventory.get_all_items()
                for item in items:
                    value = item.get_value()
                    line = f"{item.name},{item.price},{item.stock},{item.category},{value:.2f}\n"
                    file.write(line)

                print(f"✅ Exported to CSV: {csv_filename}")
                return True

        except Exception as e:
            print(f"❌ Error exporting to CSV: {e}")
            return False

    @staticmethod
    def validate_file_line(line):
        """Check if line has correct format (name|price|stock|category)"""
        try:
            parts = line.strip().split('|')

            # Must have exactly 4 parts
            if len(parts) != 4:
                return False

            float(parts[1])
            int(parts[2])

            if not parts[0] or not parts[3]:
                return False

            return True

        except (ValueError, IndexError):
            return False
