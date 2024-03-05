import utility  # module (file)
import shopping.more_shopping.shopping_cart  # package (folder containing module)

from utility import divide  # function
from shopping.more_shopping.shopping_cart import buy  # function

print(utility.divide(4, 2))
print(shopping.more_shopping.shopping_cart.buy("Apple"))

print(divide(4, 2))
print(buy("Apple"))
