username = "Admin"
userInput = ""
tryCount = 0  #keeps track of how many times the user has tried to login
tryLimit = 3  #its showing how many times a user can try login
timeOut = False #false indicates thaey still have more tries

while userInput != username and not timeOut:   #as long as the condition on this line are true the program continues
    if tryCount < tryLimit:
        userInput = input("Please enter your name: ") #every time they enter the username we are incrementing the guess count with the tryCount variable
        tryCount += 1
    else:
        timeOut = True

if timeOut:
    print("You have entered the wrong username, you are blocked from using this system")
else:
    print("You are logined as " + username)








