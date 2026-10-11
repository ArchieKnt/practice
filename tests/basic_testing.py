
from Defitions.Inventory import Inventory


inv = Inventory()

inv.restock("GPU", 10)

inv.reserve("order_1", "GPU", 6)

assert inv.available("GPU") == 4
assert inv.stock["GPU"] == 10

inv.sell("GPU", 4)

assert inv.available("GPU") == 0
assert inv.stock["GPU"] == 6

inv.ship("order_1")

assert inv.stock["GPU"] == 0
assert inv.available("GPU") == 0

print("All tests passed!")