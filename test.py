

class run:
	def __init__(self, question):
		if question and len(question) == 9 and len(question[0]) == 9: self.question = question
		else:
			print("error")
	def check_block4x4(self, question):

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
