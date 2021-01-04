

class run:
	def __init__(self, question):
		if question and len(question) == 9 and len(question[0]) == 9: self.question = question
		else:
			print("error")
	def check_block4x4(self, x,y):
		if x>=0 and x<=2 and y>=0 and y<=2:    ##block1
			init_x=0
			init_y=0
		elif x>=3 and x<=5 and y>=0 and y<=2: ##block2
			init_x=3
			init_y=0
		elif x>=6 and x<=8 and y>=0 and y<=2:  ##block3
			init_x=6
			init_y=0

		elif x>=0 and x<=2 and y>=3 and y<=5:  ##block4
			init_x=0
			init_y=3
		elif x>=3 and x<=5 and y>=3 and y<=5:  ##block5
			init_x=3
			init_y=3
		elif x>=6 and x<=8 and y>=3 and y<=5:  ##block6
			init_x=6
			init_y=3

		elif x>=0 and x<=2 and y>=6 and y<=8:  ##block7
			init_x=0
			init_y=6
		elif x>=3 and x<=5 and y>=6 and y<=8:  ##block8
			init_x=3
			init_y=6
		elif x>=6 and x<=8 and y>=6 and y<=8:  ##block9
			init_x=6
			init_y=6

		for i in range(3):
			for j in range(3):
				l=1
if __name__ == '__main__':
##x=np.zeros( (9,9) ) 
	x=[[8,0,0,0,3,0,0,0,0],
	[4,0,0,0,0,0,0,0,9],
	[0,0,0,0,0,0,0,1,2],
	[6,9,4,5,0,8,3,0,7],
	[2,0,0,9,7,0,0,5,0],
	[0,0,1,3,6,2,0,0,0],
	[0,2,0,1,9,0,4,8,3],
	[1,8,3,7,4,6,0,0,5],
	[9,4,5,2,8,0,7,6,1]	
	  ]

	run(x)
	print(len(x))
	print(x)
