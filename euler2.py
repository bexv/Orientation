# Project Euler question 2

# Set first two digits = 1, z will be the sum of the previous digits
x = 1
y = 1
z = 0
sum = 0

#loop until terms reach 4000000
while z < 4000000:
    z = x + y
    if z % 2 == 0:
        sum = sum + z
    x = y
    y = z

print (sum)