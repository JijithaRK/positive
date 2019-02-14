b=input()
if b.isalpha:
	x=b.lower()
	if(x=="a" or x=="e" or  x=="i" or x=="o" or x=="u"):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
