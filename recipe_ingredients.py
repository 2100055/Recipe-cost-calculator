#Functions go here:

# ensure answer is not blank 

def not_blank(name):
    

    while True:

        answer = input(name)

        if answer == "":
            print("Sorry, you cannot leave this space blank... please try again")

        else:
            return answer

while True:
 ingredient_amount = not_blank("Please list you're ingredients and the amount of each is needed for you're recipe: ")
 
 print("Looks good!")
