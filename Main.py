import sys
from Thompson import match
# Main.py accept args in the following formats [regex, string], [regex, ""]
# If one arg is input, the match function will compare the regex against an emtpy string.
# It will return to the user if a match is found or not.


# Ensures two args, a regex and a string.
if(len(sys.argv) == 3):
	print(f"Regex: {sys.argv[1]}\tString: {sys.argv[2]}")
	if (match(sys.argv[1], sys.argv[2]) == True):
		print("Match found.")
	else:
		print("Match not found.")
elif(len(sys.argv) == 2):
	# Allows for a blank string.
	print(f"Regex: {sys.argv[1]}\tString: NULL")
	if (match(sys.argv[1], "") == True):
		print("Match")
	else:
		print("Match not found.")
else:
	print("Invalid input, please enter a regex and a string.")

