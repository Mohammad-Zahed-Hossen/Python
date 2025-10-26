# main.py
from inventory import Inventory
from item import Item
from file_manager import FileManager
from ui import UserInterface

class PyStockApp:
    """Main application controller"""

    def __init__(self):
        """Initialize components"""
        self.file_manager = FileManager()
        self.inventory = None
        self.ui = UserInterface()

    def start(self):
        """Load inventory and show welcome"""
        self.inventory = self.file_manager.load_inventory()
        self.ui.display_welcome(len(self.inventory))
        self.run()

    def run(self):
        """Main program loop"""
        while True:
            self.ui.show_menu()
            choice = self.ui.get_menu_choice()

            if choice == 1:
                self.add_or_update_item()
            elif choice == 2:
                self.view_inventory()
            elif choice == 3:
                self.view_by_category()
            elif choice == 4:
                self.view_statistics()
            elif choice == 5:
                self.manage_stock()
            elif choice == 6:
                self.search_items()
            elif choice == 7:
                self.create_backup()
            elif choice == 8:
                self.save_and_exit()
                break
            else:
                self.ui.show_error("Invalid choice!")

            self.ui.pause()  # Pause before showing menu again

    def add_or_update_item(self):
        """Get item details, create Item, add to inventory"""
        print("\n" + "=" * 50)
        print("ADD / UPDATE ITEM")
        print("=" * 50)

        # Get item details from user
        name, price, stock, category = self.ui.get_item_details()

        # Check if item already exists
        existing_item = self.inventory.get_item(name)

        if existing_item:
            # Item exists - ask if user wants to update
            print(f"\n⚠️  Item '{name}' already exists!")
            self.ui.display_item(existing_item)

            if self.ui.confirm_action("Do you want to update this item?"):
                # Create new item with updated details
                new_item = Item(name, price, stock, category)
                self.inventory.add_item(new_item)
                self.ui.show_success(f"Updated '{name}'")
            else:
                self.ui.show_info("Update cancelled")
        else:
            try:
                new_item = Item(name, price, stock, category)
                self.inventory.add_item(new_item)
                self.ui.show_success(f"Added new item '{name}'")
            except ValueError as e:
                self.ui.show_error(f"Could not add item: {e}")

    def view_inventory(self):
        """Display all items"""
        print("\n" + "=" * 50)
        print("VIEW ALL INVENTORY")
        print("=" * 50)

        if len(self.inventory) == 0:
            self.ui.show_warning("Inventory is empty!")
        else:
            self.ui.display_inventory(self.inventory)

    def view_by_category(self):
        """Show categories, let user select, display items"""
        print("\n" + "=" * 50)
        print("VIEW BY CATEGORY")
        print("=" * 50)

        categories = self.inventory.get_categories()

        if not categories:
            self.ui.show_warning("No categories found!")
            return

        # Display all categories with option to view all
        print("\nAvailable Categories:")
        category_list = sorted(list(categories))
        for i, cat in enumerate(category_list, 1):
            items_in_cat = self.inventory.search_by_category(cat)
            print(f"{i}. {cat} ({len(items_in_cat)} items)")
        print(f"{len(category_list) + 1}. View all categories with details")

        # Get user choice
        choice = self.ui.get_valid_integer(
            f"\nSelect category (1-{len(category_list) + 1}): ",
            min_value=1
        )

        if choice == len(category_list) + 1:
            # Show all categories with details
            self.ui.display_categories(self.inventory)
        elif 1 <= choice <= len(category_list):
            # Show items in selected category
            selected_category = category_list[choice - 1]
            items = self.inventory.search_by_category(selected_category)

            print(f"\n{'=' * 60}")
            print(f"Items in Category: {selected_category}")
            print(f"{'=' * 60}")

            for item in items:
                self.ui.display_item(item)
        else:
            self.ui.show_error("Invalid selection!")

    def view_statistics(self):
        """Calculate and display stats"""
        print("\n" + "=" * 50)
        print("INVENTORY STATISTICS")
        print("=" * 50)

        stats = self.inventory.get_statistics()
        self.ui.display_statistics(stats)

        # Show low stock items if any
        low_stock = self.inventory.get_low_stock_items()
        if low_stock:
            print(f"\n⚠️  LOW STOCK ALERTS ({len(low_stock)} items)")
            print("─" * 60)
            for item in low_stock:
                print(f"  • {item.name}: Only {item.stock} units remaining!")

    def manage_stock(self):
        """Menu for restock/sell operations"""
        print("\n" + "=" * 50)
        print("MANAGE STOCK")
        print("=" * 50)
        print("1. Restock Item (Add stock)")
        print("2. Sell Item (Reduce stock)")
        print("3. Cancel")

        choice = self.ui.get_valid_integer("Enter choice (1-3): ", min_value=1)

        if choice == 3:
            return

        # Get item name
        item_name = input("\nEnter item name: ").strip()
        item = self.inventory.get_item(item_name)

        if not item:
            self.ui.show_error(f"Item '{item_name}' not found!")
            return

        # Show current item status
        print("\nCurrent item status:")
        self.ui.display_item(item)

        if choice == 1:
            # Restock
            quantity = self.ui.get_valid_integer(
                "\nEnter quantity to add: ",
                min_value=1
            )

            if item.restock(quantity):
                self.ui.show_success(
                    f"Added {quantity} units. New stock: {item.stock}"
                )
            else:
                self.ui.show_error("Restock failed!")

        elif choice == 2:
            # Sell
            quantity = self.ui.get_valid_integer(
                "\nEnter quantity to sell: ",
                min_value=1
            )

            if item.sell(quantity):
                self.ui.show_success(
                    f"Sold {quantity} units. Remaining stock: {item.stock}"
                )

                # Check if now low stock
                if item.is_low_stock():
                    self.ui.show_warning(
                        f"'{item.name}' is now low on stock!"
                    )
            else:
                self.ui.show_error("Sale failed! Not enough stock.")

    def search_items(self):
        """Search by name or category"""
        print("\n" + "=" * 50)
        print("SEARCH ITEMS")
        print("=" * 50)
        print("1. Search by name")
        print("2. Search by category")
        print("3. Cancel")

        choice = self.ui.get_valid_integer("Enter choice (1-3): ", min_value=1)

        if choice == 3:
            return

        if choice == 1:
            # Search by name
            search_term = input("\nEnter item name (or part of name): ").strip().lower()

            # Get all items and filter by search term
            all_items = self.inventory.get_all_items()
            found_items = [
                item for item in all_items
                if search_term in item.name.lower()
            ]

            if found_items:
                print(f"\n✅ Found {len(found_items)} item(s):")
                for item in found_items:
                    self.ui.display_item(item)
            else:
                self.ui.show_warning(
                    f"No items found matching '{search_term}'"
                )

        elif choice == 2:
            # Search by category
            categories = self.inventory.get_categories()

            if not categories:
                self.ui.show_warning("No categories available!")
                return

            print("\nAvailable categories:")
            for cat in sorted(categories):
                print(f"  • {cat}")

            search_category = input("\nEnter category: ").strip()
            found_items = self.inventory.search_by_category(search_category)

            if found_items:
                print(f"\n✅ Found {len(found_items)} item(s) in '{search_category}':")
                for item in found_items:
                    self.ui.display_item(item)
            else:
                self.ui.show_warning(
                    f"No items found in category '{search_category}'"
                )

    def create_backup(self):
        """Create backup file"""
        print("\n" + "=" * 50)
        print("CREATE BACKUP")
        print("=" * 50)

        if self.ui.confirm_action("Create backup of current inventory?"):
            backup_file = self.file_manager.create_backup(self.inventory)

            if backup_file:
                self.ui.show_success(f"Backup created: {backup_file}")

                # Ask if user wants to export to CSV as well
                if self.ui.confirm_action("\nAlso export to CSV format?"):
                    csv_filename = backup_file.replace('.txt', '.csv')
                    if self.file_manager.export_to_csv(self.inventory, csv_filename):
                        self.ui.show_success(f"CSV exported: {csv_filename}")
            else:
                self.ui.show_error("Backup creation failed!")
        else:
            self.ui.show_info("Backup cancelled")

    def save_and_exit(self):
        """Save inventory and show goodbye message"""
        print("\n" + "=" * 50)
        print("SAVING AND EXITING")
        print("=" * 50)

        # Save inventory
        if self.file_manager.save_inventory(self.inventory):
            self.ui.show_success("Inventory saved successfully!")

            # Show final statistics
            print("\nFinal Statistics:")
            stats = self.inventory.get_statistics()
            self.ui.display_statistics(stats)
        else:
            self.ui.show_error("Error saving inventory!")

            if self.ui.confirm_action("Exit anyway?"):
                self.ui.show_warning("Changes were not saved!")
            else:
                return  # Don't exit, go back to menu

        # Display goodbye message
        self.ui.display_goodbye()

# Program entry point
if __name__ == "__main__":
    try:
        app = PyStockApp()
        app.start()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user")
        print("Goodbye! 👋\n")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please report this issue.\n")
