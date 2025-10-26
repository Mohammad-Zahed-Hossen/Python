# ui.py
from item import Item

class UserInterface:
    """Handles all user interaction"""

    @staticmethod
    def show_menu():
        """Display main menu"""
        print("\n" + "=" * 50)
        print("    PyStock Inventory Management v2.0")
        print("=" * 50)
        print("1. Add/Update Item")
        print("2. View All Inventory")
        print("3. View by Category")
        print("4. Inventory Statistics")
        print("5. Manage Stock (Restock/Sell)")
        print("6. Search Items")
        print("7. Create Backup")
        print("8. Save & Exit")
        print("=" * 50)

    @staticmethod
    def get_menu_choice():
        """Get and validate menu choice"""
        while True:
            choice = UserInterface.get_valid_integer(
                "Enter your choice (1-8): ",
                min_value=1
            )

            if 1 <= choice <= 8:
                return choice
            else:
                UserInterface.show_error("Please choose between 1 and 8!")

    @staticmethod
    def get_item_details():
        """Prompt for all item details and return tuple"""
        print("\n--- Enter Item Details ---")

        name = input("Item name: ").strip()
        while not name:
            UserInterface.show_error("Name cannot be empty!")
            name = input("Item name: ").strip()

        price = UserInterface.get_valid_float("Price: $", min_value=0.01)
        stock = UserInterface.get_valid_integer("Stock quantity: ", min_value=0)

        category = input("Category: ").strip()
        while not category:
            UserInterface.show_error("Category cannot be empty!")
            category = input("Category: ").strip()

        return (name, price, stock, category)

    @staticmethod
    def display_item(item):
        """Print formatted item details"""
        print(f"\n{'─' * 60}")
        print(f"📦 {item.name}")
        print(f"{'─' * 60}")
        print(f"  💰 Price:      ${item.price:.2f}")
        print(f"  📊 Stock:      {item.stock} units")
        print(f"  🏷️  Category:   {item.category}")
        print(f"  💵 Total Value: ${item.get_value():.2f}")

        if item.is_low_stock():
            print(f"  ⚠️  Status:     LOW STOCK!")
        else:
            print(f"  ✅ Status:     In Stock")
        print(f"{'─' * 60}")

    @staticmethod
    def display_inventory(inventory):
        """Print all items in formatted table"""
        items = inventory.get_all_items()

        if not items:
            print("\n📭 Inventory is empty!")
            return

        print(f"\n{'═' * 80}")
        print(f"{'CURRENT INVENTORY':^80}")
        print(f"{'═' * 80}")

        # Table header
        print(f"{'Item Name':<20} {'Price':>10} {'Stock':>10} {'Category':<15} {'Value':>12}")
        print(f"{'─' * 80}")

        # Table rows
        for item in items:
            value = item.get_value()
            status = "⚠️" if item.is_low_stock() else "  "
            print(f"{status}{item.name:<18} ${item.price:>8.2f} {item.stock:>10} "
                  f"{item.category:<15} ${value:>10.2f}")

        print(f"{'═' * 80}")
        print(f"Total Items: {len(items)} | "
              f"Total Value: ${inventory.calculate_total_value():.2f}")
        print(f"{'═' * 80}")

    @staticmethod
    def display_categories(inventory):
        """Show categories and item counts"""
        categories = inventory.get_categories()

        if not categories:
            print("\n📭 No categories found!")
            return

        print(f"\n{'═' * 60}")
        print(f"{'INVENTORY CATEGORIES':^60}")
        print(f"{'═' * 60}")

        for category in sorted(categories):
            items_in_category = inventory.search_by_category(category)
            total_value = sum(item.get_value() for item in items_in_category)

            print(f"\n📁 {category}")
            print(f"{'─' * 60}")
            print(f"  Items: {len(items_in_category)}")
            print(f"  Total Value: ${total_value:.2f}")

            # List items in this category
            for item in items_in_category:
                status = "⚠️" if item.is_low_stock() else "✅"
                print(f"    {status} {item.name} - {item.stock} units @ ${item.price:.2f}")

        print(f"\n{'═' * 60}")

    @staticmethod
    def display_statistics(stats):
        """Show inventory statistics beautifully"""
        print(f"\n{'╔' + '═' * 58 + '╗'}")
        print(f"║{'INVENTORY STATISTICS':^58}║")
        print(f"{'╠' + '═' * 58 + '╣'}")

        print(f"║  📦 Total Items:        {stats['total_items']:>30} ║")
        print(f"║  💰 Total Value:        ${stats['total_value']:>29.2f} ║")
        print(f"║  🏷️  Categories:         {stats['categories_count']:>30} ║")
        print(f"║  ⚠️  Low Stock Items:    {stats['low_stock_count']:>30} ║")

        print(f"{'╚' + '═' * 58 + '╝'}")

    @staticmethod
    def get_valid_integer(prompt, min_value=0):
        """Get validated integer input"""
        while True:
            try:
                value = int(input(prompt))
                if value >= min_value:
                    return value
                else:
                    UserInterface.show_error(
                        f"Please enter a number >= {min_value}"
                    )
            except ValueError:
                UserInterface.show_error("Please enter a valid integer!")

    @staticmethod
    def get_valid_float(prompt, min_value=0.0):
        """Get validated float input"""
        while True:
            try:
                value = float(input(prompt))
                if value >= min_value:
                    return value
                else:
                    UserInterface.show_error(
                        f"Please enter a number >= {min_value}"
                    )
            except ValueError:
                UserInterface.show_error("Please enter a valid number!")

    @staticmethod
    def confirm_action(message):
        """Ask yes/no confirmation"""
        while True:
            response = input(f"{message} (yes/no): ").strip().lower()
            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            else:
                UserInterface.show_error("Please enter 'yes' or 'no'")

    @staticmethod
    def show_success(message):
        """Display success message"""
        print(f"✅ {message}")

    @staticmethod
    def show_error(message):
        """Display error message"""
        print(f"❌ {message}")

    @staticmethod
    def show_info(message):
        """Display info message"""
        print(f"ℹ️  {message}")

    @staticmethod
    def show_warning(message):
        """Display warning message"""
        print(f"⚠️  {message}")

    @staticmethod
    def pause():
        """Pause and wait for user to press Enter"""
        input("\nPress Enter to continue...")

    @staticmethod
    def clear_screen():
        """Clear the screen (optional, works on most terminals)"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_welcome(item_count):
        """Display welcome message with item count"""
        print("\n" + "═" * 60)
        print(f"{'🏪 PyStock Inventory Management System':^60}")
        print("═" * 60)
        print(f"✅ Loaded {item_count} items from storage")
        print("═" * 60)

    @staticmethod
    def display_goodbye():
        """Display goodbye message"""
        print("\n" + "═" * 60)
        print(f"{'Thank you for using PyStock!':^60}")
        print(f"{'See you next time! 👋':^60}")
        print("═" * 60 + "\n")
