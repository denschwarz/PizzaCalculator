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
sour_dough_poolish = get_int("Do you want to use sour dough (1) or poolish (2)?", 2)
if sour_dough_poolish == 1:
    weight_sour_dough = get_float("How much sour dough?", 180)
elif sour_dough_poolish == 2:
    percent_poolish = get_float("How much percent of the dough should be poolish?", 30)
else:
    raise RuntimeError(f"Choice for sour dough or poolish ({sour_dough_poolish}) not known")

percent_spillage = 10 # typical spillage of 10%
total_weight = N_pizza*weight_pizza*(1+percent_spillage/100.)

weight_flour = total_weight / (1+hydration/100)
weight_water = weight_flour * hydration/100
weight_salt = weight_flour * 0.03

if sour_dough_poolish == 1:
    weight_water_poolish = 0.5*weight_sour_dough
    weight_flour_poolish = 0.5*weight_sour_dough
elif sour_dough_poolish == 2:
    weight_water_poolish = 0.5* total_weight * percent_poolish/100
    weight_flour_poolish = 0.5* total_weight * percent_poolish/100
else:
    raise RuntimeError(f"Choice for sour dough or poolish ({sour_dough_poolish}) not known")
weight_flour_rest = weight_flour - weight_flour_poolish
weight_water_rest = weight_water - weight_water_poolish

if weight_flour_rest < 0:
    raise RuntimeError(f"A {percent_poolish} percent poolish would result in too much flour ({weight_flour_poolish}g in poolish vs a total of {weight_flour}g).")
if weight_water_rest < 0:
    raise RuntimeError(f"A {percent_poolish} percent poolish would result in too much water ({weight_water_poolish}g in poolish vs a total of {weight_water}g).")

if sour_dough_poolish==2:
    weight_yeast = weight_flour_poolish * 0.004 # 1g yeast in a poolish with 250g Water + 250g Flour
else:
    weight_yeast = 0
print("---------------------------------------")
print("INGREDIENTS")
if sour_dough_poolish==2:
    print("({:.0f} pizzas with {:.0f} g at {:.0f}% hydration and {:.0f}% poolish with {:.0f}% spillage)".format(N_pizza, weight_pizza, hydration, percent_poolish,percent_spillage))
else:
    print("({:.0f} pizzas with {:.0f} g at {:.0f}% hydration and {:.0f}% g sour dough with {:.0f}% spillage)".format(N_pizza, weight_pizza, hydration, weight_sour_dough,percent_spillage))

print("  - {:.0f} g flour".format(weight_flour))
print("  - {:.0f} g water".format(weight_water))
print("  - {:.1f} g salt".format(weight_salt))
print("  - {:.1f} g yeast".format(weight_yeast))
if sour_dough_poolish==2:
    print("---------------------------------------")
    print("POOLISH")
    print("  - {:.0f} g flour".format(weight_flour_poolish))
    print("  - {:.0f} g water".format(weight_water_poolish))
    print("  - {:.1f} g yeast".format(weight_yeast))
    print("---------------------------------------")
    print("ADD TO POOLISH")
else:
    print("---------------------------------------")
    print("ADD TO SOUR DOUGH")
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
if sour_dough_poolish==2:
    print("  - Make poolish 72h before pizza time")
else:
    print("  - Make sour dough starter at least 5 days before pizza time")
print("  - Start about 48h before pizza time with making the dough from poolish")
print("  - Put poolish and rest of ingredients together, knead a bit, cover with damp towel, 20 Min rest")
print("  - Kneading, cover with damp towel, 20 Min rest")
print("  - Make portions, form balls, 48h rest in fridge")
print("  - About 4h before pizza time take balls out of fridge and let them warm to room temperature")
print("  - Pizza time!")
