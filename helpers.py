#in case someone wants to use a copypasta that includes these dumb characters
def replace_badchars(input):
	input = input.replace("”", "\"")
	input = input.replace("“", "\"")
	input = input.replace("’", "\'")
	return input