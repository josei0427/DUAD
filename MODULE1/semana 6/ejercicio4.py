def the_phrase(string):
	new_string = ""
	for i in reversed(string): 
		new_string += i
	return new_string

result = the_phrase("Me gusta el ROCK")
print(result)