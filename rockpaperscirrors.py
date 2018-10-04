code:
import random
r={1:'r',2:'p',3:'s'}
a=0
b=0
while a<3 and b<3:
	x=r[random.randint(1,3)]
	p=input("enter your choice")
	print(p)
	if(x==p):
		print("draw")
	elif (x=='r'):
		if (p=='s'):
			print( "comp won")
			a+=1
		else:
			print("you won")
			b+=1
	elif (x=='p'):
		if(p=='r'):
			print("comp won")
			a+=1		
		else:
			print("you won")
			b+=1
	elif (x=='s'):
		if(p=='p'):	
			print("comp won")
			a+=1
		else:
			print("you won")
			b+=1
	if(a==3):
		print("computer wins")	
	elif(b==3):
		print("you win")


output:

enter your choicer
r
you won
enter your choices
s
you won
enter your choicep
p
draw
enter your choicer
r
you won
you win

