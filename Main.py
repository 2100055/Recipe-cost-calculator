# functon goes here


# ensure answer is not blank 

def not_blank(name):  

    while True:

        response = input(name)

        if response == "":
            print("Sorry, you cannot leave this space blank... please try again")

        else:
            return response    
           

# ask user for serving size 

def number_checker(recipe):


    while True:
            
        try:

            serving = int(input(recipe)) 
            return serving
        
        except ValueError:
           
            print("Please enter a valid serving size") 



# main code goes here

#ask user for recipe name

recipe_name = not_blank("Please enter recipe name: ")

if recipe_name == not_blank:
    print("mmm, yummy")

# ask user for serving size

serving_size = number_checker (" How many servings does you're recipe have? (Please enter a numerical value):  ")

if 2 <= serving_size <= 20:
    pass

elif serving_size <2:
    print("You're recipe has very few servings")


else:
    print("??... Are you sure this isn't a typo")  

#ask user for ingredients and amounts

while True:
 ingredient_amount = not_blank("Please list you're ingredients and the amount of each is needed for you're recipe: ")
 
 print("Looks good!")

 #Ask user for total cost of ingredients


 while True:

    cost = number_checker (" What is the total cost of ingredients for your recipe? (Enter number without $$): ")  

    if  10<= cost <= 150:
        pass

    elif cost <10:
       print("you're recipe is very cheap")

    else:
      print("??... Are you sure this isn't a typo")  


#Find the cost of ingredients per serving

    total_cost = cost
    serving = serving_size

    print(" You have {} servings with a total cost of {} which means each serving costs {} ".format(serving, total_cost, total_cost / serving))




   