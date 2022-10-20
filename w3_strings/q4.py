def changer(inputstring):
    first_char = inputstring[0]
    
    new_string = first_char + inputstring[1:].replace(first_char, '$')
    
    return new_string

print(changer('hi there brother.'))