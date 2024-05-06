# function goes here 

# ask user for serving size 

def number_checker(recipe):

    while True:
            
        try:

            serving = int(input(recipe)) 
            return serving
        
        except ValueError:
           
            print("Please enter a valid serving size")

# Main code goes here
while True:


   serving_size = number_checker ("How many servings does you're recipe have? (Please enter a numerical value):  ")

   if 1 <= serving_size <= 50:
       pass

   elif serving_size <1:
    print("??... Are you sure this isn't a typo? ")
    continue


   else:
    print("This seems unlikely... please check again ")  
