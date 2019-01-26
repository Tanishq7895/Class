import time
d=time.time()
def countdown(number):
    if number==0:
        print("completed")
    else:
        print(number)
        countdown(number-1)
countdown(10)
x=time.time()
print(x-d)               
