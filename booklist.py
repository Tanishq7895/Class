#python
import time
booklist=["diary of a wimpy kid","harry potter" ,"geronimo stilton"]
print("welcome to my book store")
print("press 1 to see the booklist ")
print("press 2 to add something to a booklist")
print("press 3 to delete")
print("press 4 find something from the booklist")
print("press 5 to stop the program")
print("press 6 to know the number of items in the booklist")
print("press 7 to replace thing from the booklist")
print("press 8 to reverse booklist")
x=int(input("what would you like to do "))
while True:
	if x==1:
		print(booklist)
		break
	if x==2:
		f=str(input("what would you like to add?"))
		booklist.append(f)
		print("this is the new booklist ", booklist)
		break
	if x==3:
		print(booklist)
		h=int(input("what number of the object in the  list would you like to delete ?"))
		del booklist[h]
		print(booklist)
		break
	if x==4:
		print(booklist)
		d=str(input("what do you like to find"))
		m=booklist.index(d)
		print("you book " , d , " is found on number " ,m )
		break
	if x==5:
		print("thanks for visiting my bookstore")
		break
	if x==6:
		print(len(booklist))
		break
	if x==7:
		print(booklist)
		hg=int(input("what number of the object in the  list would you like to replace ?"))
		time.sleep(0.001)
		ha=str(input("with what would you like to replace the book  "))
		booklist[hg]=ha
		print(booklist)
		break
	if x==8:
		print("this is the booklist right now: " , booklist)
		h=booklist.reverse()
		print("this is the booklist after reversing it: " , h)
		break
