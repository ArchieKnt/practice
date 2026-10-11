class Inventory:
    def __init__(self):
        self.stock = {}

    def restock(self, sku, qty):
        if qty <= 0:
            raise ValueError("Invalid quantity")

        self.stock[sku] = self.stock.get(sku, 0) + qty

    def sell(self, sku, qty):
        if qty <= 0:
            raise ValueError("Invalid quantity")

        if self.stock.get(sku, 0) < qty:
            raise ValueError("Insufficient stock")

        self.stock[sku] -= qty