#Project Euler problem 3
#largest prime factor of 600851475143

i = 2
c = 600851475143

while i * i < c:
    while c % i == 0:
        c = c / i
    i = i + 1

print (c)

