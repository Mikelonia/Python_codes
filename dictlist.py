#To test my knowledge of Dictionaries

Names = {"Ade" : 25,
"Tola" : 32,
"Jeremiah" : 23,
"Juliet" : 34,
"Taiwo" : 33
}

def gettheirfiles(Names):
	for name, age in Names.items():
		print(f"Mike loves {name}, who is {age} years old")

gettheirfiles(Names)
print(f"thank you, you now know my favourite persons".upper())
