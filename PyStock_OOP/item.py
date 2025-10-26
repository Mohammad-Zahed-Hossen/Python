# from typing import Type
class Item:
    """Represents a single inventory item"""
    MIN_PRICE = 0.1
    MIN_STOCK = 0
    def __init__(self, name, price, stock, category):
      # Hint: Use self.attribute_name = value
        self.name = name
        self.price = float(price)
        self.stock = int(stock)
        self.category = category
        if self.price < self.MIN_PRICE:
          raise ValueError(f"Price must be at least {self.MIN_PRICE}")
        if self.stock < self.MIN_STOCK:
          raise ValueError("Stock cannot be negative!")


    def update_price(self, new_price):
      # Hint: Check if new_price > 0
        try:
          new_price = float(new_price)
          if new_price >= self.MIN_PRICE:
            self.price = new_price
            return True
          else:
            print(f"❌ Price must be at least ${self.MIN_PRICE}")
            return False
        except (ValueError, TypeError):
          print("❌ Please enter a valid price number")
          return False

    def restock(self, quantity):
      # Hint: Validate quantity is positive
        try:
          quantity = int(quantity)
          if quantity > 0:
            self.stock += quantity
            return True
          else:
            print("❌ Quantity must be positive")
            return False
        except (ValueError, TypeError):
          print("❌ Please enter a valid quantity number")
          return False

    def sell(self, quantity):
      # Hint: Check if quantity <= self.stock
      # Return True if successful, False if not enough stock
      try:
        quantity = int(quantity)
        if quantity <= 0:
          print("❌ Quantity must be positive")
          return False
        if self.stock >= quantity:
          self.stock -= quantity
          return True
        else:
          print(f"❌ Not enough stock! Only {self.stock} available")
          return False
      except (ValueError, TypeError):
        print("❌ Please enter a valid quantity number")
        return False

    def get_value(self):
        return self.price * self.stock

    def is_low_stock(self, threshold=10):
      # Return True/False
        if self.stock < threshold:
          print("Stock is below threshold level...")
          return True
        else:
          return False

    def __str__(self):
        # Example: "Soap - $345.00 (34 in stock) [Grocery]"
        return f"{self.name} - ${self.price:.2f} ({self.stock} in stock) [{self.category}]"

    def to_file_format(self):
        # TODO: Return string in format: "name|price|stock|category"
        return f"{self.name} | {self.price} | {self.stock} | {self.category}"

    @staticmethod
    def from_file_format(line):
      # Hint: Split by "|", convert types, return Item(...)
      try:
        parts = line.strip().split('|')
        if len(parts) != 4:
          raise ValueError("Invalid file format!")
        name = parts[0].strip()
        price = float(parts[1].strip())
        stock = int(parts[2].strip())
        category = parts[3].strip()
        return Item(name, price, stock, category)
      except (ValueError, IndexError) as e:
            print(f"❌ Error parsing line: {e}")
            return None

