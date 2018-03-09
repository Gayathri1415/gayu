print("Enter '0' for exit.")
ch = input("Enter any character: ");
if ch == '0':
    exit();
else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    	print("an alphabet")
    else:
    	print("not an alphabet")
