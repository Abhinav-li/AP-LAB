import cmath

r = int(input("Enter real number "))

i = int(input('Enter imaginary number '))

com = complex(r,i)

print('Sine is ', cmath.sin(com))
print('Square Root is ', cmath.sqrt(com))
print('Log is ', cmath.log(com))

