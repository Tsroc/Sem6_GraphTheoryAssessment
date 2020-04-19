import sys
from Thompson import match
from Thompson import information as ThompsonInformation
# Main.py accept args in the following formats [regex, string], [regex, ""]
# If one arg is input, the match function will compare the regex against an emtpy string.
# It will return to the user if a match is found or not.


# Ensures two args, a regex and a string.
keywords = {"help"}

def listKeywords():
	keywordList = "Valid args: "
	for keyword in keywords:
		keywordList += keyword
	print(keywordList)
	
def information():
	print("Main.py accept args in the following formats:")
	print("\t[regex, string]: will match this string to the regex")
	print("\t[regex]: will match an empty string to the regex")
	

def commandline():
	if(len(sys.argv) == 3):
		print(f"Regex: {sys.argv[1]}\tString: {sys.argv[2]}")
		if (match(sys.argv[1], sys.argv[2]) == True):
			print("Match found.")
		else:
			print("Match not found.")
	elif(len(sys.argv) == 2):
		# Allows for keyword.
		# Allows for a blank string.
		
		# Determine if an argument has been entered or a blank string.
		args = sys.argv[1] 	# Unsure of a better way how to get first char in a string within an array.
		if(args[:2] == "--"):
			if(args[2:] in keywords):
				# Valid command keyword entered.
				if(args[2:] == "help"):
					listKeywords()
					print()
					information()
					print()
					ThompsonInformation()
				
			else:
				print("Invalid command.")
				listKeywords()
			
		
		elif (match(args, "") == True):
			print(f"Regex: {sys.argv[1]}\tString: NULL")
			print("Match")
		else:
			print("Match not found.")
	else:
		print("Invalid input, please enter a regex and a string.")


	
commandline()