# functon go here


# ensure answer is not blank 

def not_blank(name):

    while True:

        answer = input(name)

        if answer == "":
            print("Sorry, you cannot leave this space blank... please try again")

        else:
            return answer

# main code goes here
        
while True:
     answer = not_blank ("Please enter recipe name")

     print("mmm, yummy")



        
    


