from PizzaCalculator import PizzaCalculator

def get_int(prompt, default=None):
    while True:
        user_input = input(f"{prompt} (default: {default}): ") or str(default)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input! Please enter an integer.")

def get_float(prompt, default=None):
    while True:
        user_input = input(f"{prompt} (default: {default}): ") or str(default)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.")

N_pizza = get_int("How many pizzas do you want?", 2)
weight_pizza = get_float("How much dough for one pizza?", 280)
hydration = get_float("What hydration?", 70)
sour_dough_poolish = get_int("Do you want to use sour dough (1) or poolish (2)?", 1)
if sour_dough_poolish == 1:
    mode = "sour"
elif sour_dough_poolish == 2:
    mode = "poolish"
else:
    raise RuntimeError(f"Choice for sour dough or poolish ({sour_dough_poolish}) not known")


pc = PizzaCalculator(
    N_pizza = N_pizza, 
    weight_pizza = weight_pizza, 
    hydration = hydration, 
    mode = mode
)
pc.print_output()