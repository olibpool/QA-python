temperature = 40

'''
if temperature > 40:
    print('too hot')
    print('argh')
    if temperature > 50:
        print('AAH')
print('too cold')
'''

# temp=40 then it will print: too hot, argh, too cold
# temp=60 then it will print: too hot, argh, AAH, too cold
# temp=20 it will print: too cold

# we can fix it by the following:
if 50 >= temperature > 40:
    print('too hot')
    print('argh')
    if temperature > 50:
        print('AAH')
elif(temperature < 40):
    print('too cold')
    
#exercise 5

temperature = 40
if temperature > 30:
    print('too hot')
    print('aagh')
if (temperature < 0):
    print('too cold')
if temperature > 0:
    print('perfect')
    
# temp=20 then it will print: perfect
# temp=40 then it will print: too hot, perfect
# temp=-10 it will print: too cold

#excerise 6

temperature = 40
if temperature > 30:
    print('too hot')
    print('aagh')
if (temperature < 0):
    print('too cold')
else:
    print('perfect')
    
# now the final statement will only print if the one above is False, before it was independent of this statements.

#exercise 7

temperature = 40
if temperature > 30:
    print('too hot')
    print('aagh')
elif (temperature < 0):
    print('too cold')
else:
    print('perfect')
    
# here each conditional is only evaluated if the one above it is False, which means that the code will run faster since it will.
# not execute unneccessary code. Also we can perform less comparisions, as the last statement is now only an else statement,
# which means the interpreter does not need to do more work.
