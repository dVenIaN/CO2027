#set your variables
timeofday = "Afternoon"

#loop till user says no
for count in range(7) :
    timeofday = input("what is the time of day? ")
    if (timeofday == "Morning"):
        print("Good Morning")
    elif (timeofday == "Afternoon") :
        print("Good Afternoon")
    else :
        print ("Good Night")

