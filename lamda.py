f= str(input("what is you first name"))
h= str(input("what is your last name"))
fullname=lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(fullname(f,h))