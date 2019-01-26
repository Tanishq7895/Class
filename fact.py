y=int(input("what  is the number you thought of "))
x=1
ans=1
if (y==0):	
	print("0")
else:
	while(x<=y):
		ans=ans*x
		x=x+1
	print(ans)

