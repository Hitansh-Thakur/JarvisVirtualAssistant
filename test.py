a_string = "My Name Is Hitansh"
first_word = a_string.split()[0]

remaining_string = a_string.replace(first_word + " ", '')
print(first_word)
print(remaining_string)