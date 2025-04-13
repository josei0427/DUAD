def the_phrase(string):
	if string == "":
		raise ValueError("It's empy, no phrase or word introduced.")
	else:
		new_string = ""
		for i in reversed(string): 
			new_string += i
	return new_string