class thermometer():
    def temperature(self,x):
        if(x>36.4 and x<37.4):
            print("you are fine")
        else:
            print("you are not fine")
x=float(input("what is your temperature"))
f=thermometer()
f.temperature(x)
