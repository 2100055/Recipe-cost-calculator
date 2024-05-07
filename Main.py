# functions go here

def not_blank(name):

    """ Make sure the answer is not blank."""

    while True:
        response = input(name)

        if response == "":
            print("You cannot leave this space blank... please try again")

        else:
            return response

# ask user for serving size

def number_checker(recipe):

 """ Make sure the user uses an integer."""

 while True:
    try:

        serving = int(input(recipe))
        return serving

    except ValueError:

      print("Please enter a valid serving size")

# main code goes here

# ask user for recipe name

recipe_name = not_blank("Please enter recipe name: ")

if recipe_name == not_blank:
    print("mmm, yummy")

# ask user for serving size

while True:

  serving_size = number_checker("How many servings does you're recipe have? (Please enter a numerical value):  ")

  if 2 <= serving_size <= 50:
    pass

  elif serving_size < 1:
    print("??... Are you sure this isn't a typo? ")
    continue

  else:
    print("This seems unlikely... please check again ")
    continue


# ask user for ingredients and amounts

  while True:
     ingredient_amount = not_blank("Please list you're ingredients and amount needed (eg. 1 cup of flour, 2tsps milk ect.): ")

     print("Looks good!")

 # Ask user for total cost of ingredients

     while True:

        cost = number_checker(" What is the total cost of ingredients for your recipe? (Enter number without $$): ")

        if 10 <= cost <= 150:
          pass

        elif cost < 1:
            print("Please enter a valid total cost ")
            continue

        elif cost >= 150:
         print("This seems unlikely... please check again")
         continue

# Find the cost of ingredients per serving
        while True:

         total_cost = cost
         serving = serving_size

         print(" You have {} servings with a total cost of {} which means each serving costs {} ".format(serving, total_cost, total_cost / serving))
