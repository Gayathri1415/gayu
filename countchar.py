while True:
	print("Enter 'x' for exit.")
	string = input("Enter any string: ")
	if string == 'x':
		break
	else:
		char = input("Enter a character to count: ")
		val = string.count(char)
		print(val,"\n")
		
