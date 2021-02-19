# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
def get_price(quantity, item_price):
    base_price = get_base_price(quantity, item_price)
    discount_factor = get_discount_factor(base_price)
   
    return base_price * discount_factor

def get_base_price(quantity, item_price):
    return quantity * item_price

def get_discount_factor(base_price):
    if base_price > 1000: 
        return 0.95
    else: 
        return 0.98