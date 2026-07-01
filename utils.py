def calculate_total(coffee, tea, sandwich):
    total = (coffee * 8.50) + (tea * 6.00) + (sandwich * 12.00)
    return total


def print_receipt(customer_name, coffee, tea, sandwich, total):
    print("\n===== RECEIPT =====")
    print("Customer :", customer_name)
    print("Coffee   :", coffee)
    print("Tea      :", tea)
    print("Sandwich :", sandwich)
    print("-------------------")
    print("Total = RM", format(total, ".2f"))