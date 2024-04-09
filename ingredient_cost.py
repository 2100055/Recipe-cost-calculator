#Functions go here

#Make sure cost is a numerical value

def number_checker(recipe):


    while True:
            
        try:

            serving = int(input(recipe)) 
            return serving
        
        except ValueError:
           
            print("Please enter a numerical value.") 


# Main code goes here

while True:

    cost = number_checker (" What is the total cost of ingredients for your recipe? (Enter number without $$): ")  

    if  10<= cost <= 150:
        pass

    elif cost <10:
       print("you're recipe is very cheap")

    else:
      print("??... Are you sure this isn't a typo")  
    
                