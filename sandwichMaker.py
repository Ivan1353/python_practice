import pyinputplus as pyip

prices =  {
        "wheat":2, "white":2, "sourdough":2.5,"chicken":3, "turkey":3.5, "ham":3,
        "tofu":2.5, "cheddar":1.5, "Swiss":2, "mozzarella":1.5, "mayo" : 0.5,
        "mustard" : 0.5, "lettuce" : 0.5, "tomato" : 0.5
}

numberSandwiches = inputInt(min=1)
price_total = 0

for num in range(numberSandwich):
    price_sandwich = 0
    sandwich = []

    bread_type_input = pyip.inputMenu(["wheat", "white", "sourdough"], prompt="What type of bread would you like?\n")
    protein_type_input = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt="What type of protein would you like?")
    cheese_yes_no = pyip.inputYesNo()
    if cheese == "yes":
        cheese_type_input = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], prompt="What type of cheese would you like?")
    mayo_yes_no = pyip.inputYesNo(promt = "Would you like mayo on your sandwich?")
    mustard_yes_no = pyip.inputYesNo(prompt = "Would you like mustard on your sandwich?")
    lettuce_yes_no = pyip.inputYesNo(prompt = "Would you like lettuce on your sandwich?")
    tomato_yes_no = pyip.inputYesNo(prompt = "Would you like tomato on your sandwich?")

    sandwich.append(bread_type_input)
    sandwich.append(protein_type_input)
    sandwich.append(cheese_type_input)
    if mayo_yes_no == "yes":
        sandwich.append("mayo")
    if mustard_yes_no == "yes":
        sandwich.append("mustard")
    if lettuce_yes_no == "yes":
        lettuce.append("lettuce")
    if tomato_yes_no == "yes":
        tomato.append("tomato")

    for product in sandwich:
        price_sandwich += prices[product]
    price_total += price_sandwich
    print(f"Your {num}. sandwich will cost {price_sandwich}. You have {numberSandwiches-num} sandwiches left to order")

print(f"You have ordered {numberSandwiches}. Your total will cost {price_total}")
