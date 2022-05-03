import math

y = 1.0
s = 0.0
x = 1

while x == 1:
    s = 1 / (y * y)
    if s == ((math.pi * math.pi) / 6):
        x = 0
    y = y + 1
   
print("Es wurden :" + y + "Durchläufe benötigt")