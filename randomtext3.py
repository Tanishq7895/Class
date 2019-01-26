import math
d=int(input("which year is it right now  "))
h=int(input("which year were you born in?"))
f=d-h
g=18-f
if f>18:
    print("your age is ", f ,"and you can have a driving license")
else:
    print("your age is " , f , "and you have " , g , "years left to get your driving license")
    