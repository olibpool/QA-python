def inger(string):
    if string[3:] == 'ing':
        return string + 'ly'
    elif len(string) < 3:
        return string
    else:
        return string + 'ing'
    
    
print(inger('abd'))
print(inger('string'))
print(inger('am'))