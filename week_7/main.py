from food_order import calculate_total

def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))
        
        # Fill in the total blank
        total = calculate_total(price, quantity)
        
        # Handle the error string returns so it doesn't try to format a string as a float
        if isinstance(total, str):
            print(f"Error: {total}")
        else:
            print(f"Total Payment = RM {total:.2f}")
            
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()