def calculate_total(price, quantity):
    # Missing code: Validate customer input
    if price <= 0:
        return "invalid price"
    if quantity <= 0:
        return "invalid quantity"
    
    # Return statement filling the 3 blanks: return [price] [*] [quantity]
    return price * quantity