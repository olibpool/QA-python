def char_counter(string):
    
    string_unique = set(list(string))
    
    counts = {char: 0 for char in string_unique}
    
    for char in string_unique:
        counts[char] = string.count(char)
        
    print(counts)
        
        
char_counter('hi there')