def changer(string1, string2):
    result = string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:]
    
    return result

print(changer('oliver', 'smith'))