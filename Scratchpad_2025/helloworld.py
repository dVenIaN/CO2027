print("Hello world")
print("Hello Enyonam")

def betterPrint(astring, endl):
    for char in astring:
        print(char, endl)


astring = "You have not sent a parameter"
#astring = "Hurrah hurrah"

betterPrint(astring, 1)
betterPrint("Hello You", 1)