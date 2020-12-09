import math
try:
    x = int(input('Enter a number: '))
    print('Sine is ' , math.sin(x))
    print('Square root is ' , math.sqrt(x))
    print('Log is ' ,math.log(x))

except:
    print('Not a number')
