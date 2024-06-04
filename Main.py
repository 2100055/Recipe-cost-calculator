# Functions go here

def not_blank(name):
    """Make sure the response is not blank.

    This is a function that ensures the users answer
    is not blank by using if and else statements

    Args:
       not_blank(name): response = input(name)

    Returns:
       if response == "":
             print("you cannot leave this space blank... please try again")
       return response
   """

    while True:
        response = input(name)

        if response == "":
            print("You cannot leave this space blank... please try again")

        else:
            return response

# Ask user for serving size

def number_checker(recipe):
  """Make sure the response is an integer.

    This is a function that ensures the users answer
    is an integer by using try: and ValueError statements

    Args:
       number_checker(recipe): serving = int(input(recipe))

    Returns:
       "Please enter a valid serving size"
   """

  while True:
   try:

    serving = int(input(recipe))
    return serving

   except ValueError:

      print("Please enter a valid serving size")

# Main code goes here

# Ask user for recipe name

recipe_name = not_blank("Please enter recipe name: ")

if recipe_name == not_blank:
    print("mmm, yummy")

# Ask user for serving size

while True:

  serving_size = number_checker("What is your recipe serving size? (Please enter a numerical value):  ")

  if 2 <= serving_size <= 50:
    pass

  elif serving_size < 1:
    print("??... Are you sure this isn't a typo? ")
    continue

  else:
    print("This seems unlikely... please check again ")
    continue


# Ask user for ingredients and amounts

  while True:
     ingredient_amount = not_blank("List ingredients and amount needed (eg. 1 cup of flour, 2tsps milk ect.): ")

     print("Looks good!")

 # Ask user for total cost of ingredients

     while True:

        cost = number_checker(" Enter the total cost of ingredients for your recipe? (Enter number without $$): ")

        if 10 <= cost <= 150:
          pass

        elif cost < 1:
            print("Please enter a valid total cost ")
            continue

        else:

         print("This seems unlikely... please check again")
         continue

        print("nice!")
        
        

# Find the cost of ingredients per serving
        while True:

         total_cost = cost
         serving = serving_size

         print(" You have {} servings with a total cost of {} which means each serving costs {} ".format(serving, total_cost, total_cost / serving))

         break
