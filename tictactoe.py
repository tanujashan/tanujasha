a=[1,2,3,4,5,6,7,8,9]
def printBoard():
	print(a[0],'|',a[1],'|',a[2])
	print("-----------")
	print(a[3],'|',a[4],'|',a[5])
	print("-----------")
	print(a[6],'|',a[7],'|',a[8])
	print("-----------")

playeroneturn = True

while True:
	printBoard()
	p=int(input("choose your spot >>"))
	if(p in a):
		if playeroneturn:
			#p=input("choose your spot,player 1 >>")
			print("player 1 chose:",p)
			a[p-1]='X'
			playeroneturn= not playeroneturn
		else:
			#p=input("choose your spot,player 2 >>")
			print("player 2 chose:",p)
			a[p-1]='O'
			playeroneturn= not playeroneturn
	#check winning conditions:
		for i in (0,3,6):
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				if a[i]=='X':
					print("player 1 wins")
					exit()
				else:
					print("player 2 wins")
					exit()
		for i in range(3):
			if(a[i]==a[i+3] and a[i]==a[1+6]):
				if a[i]=='X':
					print("player 1 wins")
					exit()
				else:
					print("player 2 wins")
					exit()
			if(a[i]==a[i+])		





	else:
		continue






1 | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9
-----------
choose your spot >>1
player 1 chose: 1
X | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9
-----------
choose your spot >>4
player 2 chose: 4
X | 2 | 3
-----------
O | 5 | 6
-----------
7 | 8 | 9
-----------
choose your spot >>2
player 1 chose: 2
X | X | 3
-----------
O | 5 | 6
-----------
7 | 8 | 9
-----------
choose your spot >>5
player 2 chose: 5
X | X | 3
-----------
O | O | 6
-----------
7 | 8 | 9
-----------
choose your spot >>3
player 1 chose: 3
player 1 wins

