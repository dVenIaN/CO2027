txt = "I love apples, apple are my favorite fruit"

#x = txt.count("apple")

#print(x)

#a = "listen" 
#b = "silent"
#a = "Triangle"
#b = "Integral"
#a = "apple"
#b = "pale"
#a = "Astronomer"
#b = "Moon starer"
a = "Hello!"
b = "oLleh"

isanag = False
tempa = list()
tempb = list()

#change to lowercase
a = a.lower()
a=a.replace(" ", "") 
b = b.lower()
b=b.replace(" ", "")

for i in a:
  if (i.isalpha()):
  	tempa.append(i)
 
for i in b:
  if (i.isalpha()):
  	tempb.append(i)

print(len(tempa))
print(len(tempb))

if (len(tempb)) == (len(tempa)):
	for x in tempa:
		print(x)
		print(tempb)
	
		counter = len(tempb) 
		for i in range(counter):
			if x == tempb[i]:
				print(i)
				tempb.pop(i)
				break
	
	counter = len(tempb) 
	
	if counter == 0:
		print("is an anagram")
	else :
		print("not an anagram")

		
    
else:
    print("not an anagram")
    
  

        
    
  
        