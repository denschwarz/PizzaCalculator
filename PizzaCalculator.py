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
percent_poolish = get_float("How much percent of the dough should be poolish?", 100)

percent_spillage = 13 # typical spillage of 13%
total_weight = N_pizza*weight_pizza*(1+percent_spillage/100.)

# total_weight = weight_flour + weight_water | weight_water = hydration/100 * weight_flour
# total_weight = weight_flour + hydration*weight_flour/100
# total_weight = (1+hydration/100) * weight_flour

weight_flour = total_weight / (1+hydration/100)
weight_water = weight_flour * hydration/100
weight_salt = weight_flour * 0.03
weight_yeast = weight_flour * 0.0015



# weight_water_poolish = 0.5* total_weight * percent_poolish/100
weight_water_poolish = weight_water * percent_poolish/100
weight_flour_poolish = weight_water_poolish

weight_flour_rest = weight_flour - weight_flour_poolish
weight_water_rest = weight_water - weight_water_poolish

print("---------------------------------------")
print("INGREDIENTS")
print("({:.0f} pizzas with {:.0f} g at {:.0f}% hydration and {:.0f}% poolish with {:.0f}% spillage)".format(N_pizza, weight_pizza, hydration, percent_poolish,percent_spillage))
print("  - {:.0f} g flour".format(weight_flour))
print("  - {:.0f} g water".format(weight_water))
print("  - {:.1f} g salt".format(weight_salt))
print("  - {:.1f} g yeast".format(weight_yeast))
print("---------------------------------------")
print("POOLISH")
print("  - {:.0f} g flour".format(weight_flour_poolish))
print("  - {:.0f} g water".format(weight_water_poolish))
print("  - {:.1f} g yeast".format(weight_yeast))
print("---------------------------------------")
print("ADD TO POOLISH")
print("  - {:.0f} g flour".format(weight_flour_rest))
print("  - {:.0f} g water".format(weight_water_rest))
print("  - {:.1f} g salt".format(weight_salt))
print("---------------------------------------")
print("OVEN SETTINGS")
print("  - 400°C top")
print("  - 350°C bottom")
print("  - 2 minutes")
print("---------------------------------------")
print("RECIPE")
print("  - Make poolish 24h before pizza time")
print("  - Start about 5h before pizza time with making the dough from poolish")
print("  - Put poolish and rest of ingredients together, knead a bit, cover with damp towel, 20 Min rest")
print("  - kneading, cover with damp towel, 20 Min rest")
print("  - make one large dough ball, cover with damp towel, 45 Min rest")
print("  - again, make one large dough ball, cover with damp towel, 45 Min rest")
print("  - make portions, form balls, 2-2.5 h rest")
print("  - Pizza time!")
