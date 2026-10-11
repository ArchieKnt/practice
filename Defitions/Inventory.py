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

    def available(self, sku):
        total = self.stock.get(sku, 0)
        reserved = self.reserved.get(sku, 0)

        return total - reserved

    def reserve(self, order_id, sku, qty):
        if qty <= 0:
            raise ValueError("Invalid quantity")

        if order_id in self.reservations:
            raise ValueError("Duplicate order")

        if self.available(sku) < qty:
            raise ValueError("Insufficient stock")

        self.reservations[order_id] = (sku, qty)

        self.reserved[sku] = (
            self.reserved.get(sku, 0) + qty
        )

    def ship(self, order_id):
        if order_id not in self.reservations:
            raise KeyError("Unknown order")

        sku, qty = self.reservations[order_id]

        self.stock[sku] -= qty
        self.reserved[sku] -= qty

        del self.reservations[order_id]

    def cancel(self, order_id):
        if order_id not in self.reserveations:
            raise KeyError("Unknown order")

        sku, qty = self.reservations[order_id]

        reserved[sku] -= qty

        del self.reservations[order_id]

        