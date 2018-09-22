while True:
	n=input("enter q to quit and enter r to roll the dise")

	if(n=='q'):
		print("bye")
		exit()
	elif(n=='r'):
		import random
		r=random.randint(1,6)
		print(r)
		exit()

	 	