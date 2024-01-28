def get_valid_input(prompt, input_type):
    while True:
        user_input = input(prompt)
        try:
            if input_type == "int":
                user_input = int(user_input)
                if user_input < 0:
                    raise ValueError
            elif input_type == "bool":
                user_input = user_input.lower()
                if user_input not in ['y', 'n']:
                    raise ValueError
            break
        except ValueError:
            if input_type == "int":
                print("Please enter a positive integer!")
            elif input_type == "bool":
                print('Please answer "Y" or "N".')
    return user_input


def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    pizza_price = 12
    delivery_cost = 2.5 if num_pizzas < 5 and delivery_required else 0
    total_price = num_pizzas * pizza_price + delivery_cost

    if is_tuesday:
        total_price *= 0.5  # 50% discount on Tuesdays

    if used_app:
        total_price *= 0.75  # 25% discount for app orders

    return round(total_price, 2)


def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas = get_valid_input("How many pizzas ordered? ", "int")
    delivery_required = get_valid_input("Is delivery required? (Y/N) ", "bool")
    is_tuesday = get_valid_input("Is it Tuesday? (Y/N) ", "bool")
    used_app = get_valid_input("Did the customer use the app? (Y/N) ", "bool")

    total_price = calculate_total_price(num_pizzas, delivery_required == 'y', is_tuesday == 'y', used_app == 'y')

    print(f"\nTotal Price: £{total_price:.2f}.")


if __name__ == "__main__":
    main()
