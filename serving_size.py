# function goes here 

# ask user for serving size 

def serving_size(recipe):

    while True:
            
        try:

            serving = int(input(recipe)) 
            return serving
        
        except ValueError:
           
            print("Please enter a valid serving size")

# Main code goes here

while True:

    serving = serving_size (" How many servings does you're recipe have?: ") 
   