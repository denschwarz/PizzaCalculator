class PizzaCalculator:
    def __init__(self, N_pizza: int, weight_pizza: float, hydration: float, mode: str = "sour"):
        self.percent_spillage = 10
        self.total_weight = N_pizza*weight_pizza*(1+self.percent_spillage/100.)
        self.weight_flour = self.total_weight / (1+hydration/100)
        self.weight_water = self.weight_flour * hydration/100
        self.weight_salt = self.weight_flour * 0.03
        self.weight_yeast = None

        if mode == "poolish":
            self.percent_poolish = 30
            summary_line = "({:.0f} pizzas with {:.0f} g at {:.0f}% hydration and {:.0f}% poolish with {:.0f}% spillage)\n".format(N_pizza, weight_pizza, hydration, self.percent_poolish, self.percent_spillage)
            receipe_string = self.get_receipe_poolish()
            self.output = self.build_output(summary_line, receipe_string, mode)
        elif mode == "sour":
            self.percent_starter = 20
            summary_line = "({:.0f} pizzas with {:.0f} g at {:.0f}% hydration and {:.0f}% sour dough with {:.0f}% spillage)\n".format(N_pizza, weight_pizza, hydration, self.percent_starter, self.percent_spillage)
            receipe_string = self.get_receipe_sour_dough()
            self.output = self.build_output(summary_line, receipe_string, mode)

    def print_output(self):
        print(self.output)

    def get_receipe_poolish(self):
        # Calculate 
        weight_water_poolish = 0.5* self.total_weight * self.percent_poolish/100
        weight_flour_poolish = 0.5* self.total_weight * self.percent_poolish/100
        self.weight_yeast = weight_flour_poolish * 0.004 # 1g yeast in a poolish with 250g Water + 250g Flour
        weight_flour_rest = self.weight_flour - weight_flour_poolish
        weight_water_rest = self.weight_water - weight_water_poolish
        # Check
        if weight_flour_rest < 0:
            raise RuntimeError(f"A {self.percent_poolish} percent poolish would result in too much flour ({weight_flour_poolish}g in poolish vs a total of {weight_flour}g).")
        if weight_water_rest < 0:
            raise RuntimeError(f"A {self.percent_poolish} percent poolish would result in too much water ({weight_water_poolish}g in poolish vs a total of {weight_water}g).")
        # Build text output
        receipe_string  = "POOLISH\n"
        receipe_string += "  - {:.0f} g flour\n".format(weight_flour_poolish)
        receipe_string += "  - {:.0f} g water\n".format(weight_water_poolish)
        receipe_string += "  - {:.1f} g yeast\n".format(self.weight_yeast)
        receipe_string += self.get_line()
        receipe_string += "ADD TO POOLISH\n"
        receipe_string += "  - {:.0f} g flour\n".format(weight_flour_rest)
        receipe_string += "  - {:.0f} g water\n".format(weight_water_rest)
        receipe_string += "  - {:.1f} g salt\n".format(self.weight_salt)
        return receipe_string

    def get_receipe_sour_dough(self):
        # Calculate
        weight_starter = self.total_weight * self.percent_starter/100
        weight_sour = 0.2 * weight_starter
        weight_water_starter = 0.4 * weight_starter
        weight_flour_starter = 0.4 * weight_starter
        weight_flour_rest = self.weight_flour - (0.5 * weight_starter)
        weight_water_rest = self.weight_water - (0.5 * weight_starter)
        # Check
        if weight_flour_rest < 0:
            raise RuntimeError(f"A {self.percent_starter} percent starter would result in too much flour in poolish vs total.")
        if weight_water_rest < 0:
            raise RuntimeError(f"A {self.percent_starter} percent starter would result in too much water in poolish vs total.")
        # Build text output
        receipe_string  = "STARTER\n"
        receipe_string += "  - {:.1f} g sour dough\n".format(weight_sour)
        receipe_string += "  - {:.0f} g flour\n".format(weight_flour_starter)
        receipe_string += "  - {:.0f} g water\n".format(weight_water_starter)
        receipe_string += self.get_line()
        receipe_string += "ADD TO STARTER\n"
        receipe_string += "  - {:.0f} g flour\n".format(weight_flour_rest)
        receipe_string += "  - {:.0f} g water\n".format(weight_water_rest)
        receipe_string += "  - {:.1f} g salt\n".format(self.weight_salt)
        return receipe_string

    def get_ingredients_string(self):
        ing_string = ""
        ing_string += "  - {:.0f} g flour\n".format(self.weight_flour)
        ing_string += "  - {:.0f} g water\n".format(self.weight_water)
        ing_string += "  - {:.1f} g salt\n".format(self.weight_salt)
        if self.weight_yeast is not None:
            ing_string += "  - {:.1f} g yeast\n".format(self.weight_yeast)
        return ing_string

    def get_oven_string(self):
        oven_string  = "OVEN SETTINGS\n"
        oven_string += "  - 400°C top\n"
        oven_string += "  - 350°C bottom\n"
        oven_string += "  - 2 minutes\n"
        return oven_string

    def get_instructions(self, mode):
        instructions = "RECIPE\n"
        if mode == "sour":
            instructions += "  - Feed sour dough about 4/5 days before pizza time\n"
            instructions += "  - Make sour dough starter 3 days before pizza time\n"
            instructions += "  - Let sour dough starter rest for 3h\n"
            instructions += "  - Put starter and rest of ingredients together, knead 10-15 Min, cover with damp towel\n"
            instructions += "  - Rest for 3h (stretch and fold after 1h and again after 2h)\n"
            instructions += "  - Make portions, form balls, 72 h rest in fridge\n"
        elif mode == "poolish":
            instructions += "  - Make poolish 72 h before pizza time\n"
            instructions += "  - Start about 48 h before pizza time with making the dough from poolish\n"
            instructions += "  - Put poolish and rest of ingredients together, knead a bit, cover with damp towel, 20 Min rest\n"
            instructions += "  - Kneading, cover with damp towel, 20 Min rest\n"
            instructions += "  - Make portions, form balls, 48 h rest in fridge\n"
        instructions += "  - About 2-3 h before pizza time take balls out of fridge and let them warm to room temperature\n"
        instructions += "  - Pizza time!\n"
        return instructions

    def get_line(self):
        return "---------------------------------------\n"

    def build_output(self, summary_line, receipe_string, mode):
        outstring  = self.get_line()
        outstring += "INGREDIENTS\n"
        outstring += summary_line
        outstring += self.get_ingredients_string()
        outstring += self.get_line()
        outstring += receipe_string
        outstring += self.get_line()
        outstring += self.get_oven_string()
        outstring += self.get_line()
        outstring += self.get_instructions(mode)
        return outstring
