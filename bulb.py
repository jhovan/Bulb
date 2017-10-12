#Gallardo Valdez Jose Jhovan
#01/10/2016
#Light more light challenge PC/UVa: 110701/10110

#bulb class
class Bulb:
	#constructor
	def __init__(self):
		self.state=False

	#returns yes or not, depending on the state of the bulb
	def __str__(self):
		if self.state:
			return "yes"
		else:
			return "no"

	#change the bulb state
	def change(self):
		if self.state:
			self.state=False
		else:
			self.state=True

#receive the inputs

n=input()
inputs=[]

while n!=0:
	inputs.append(n)
	n=input()

#for each input verifies the bulb state in every path and prints the final state
for y in inputs:
	bulb=Bulb()
	for x in range(1,y+1):
		if y%x==0:
			bulb.change()
	print str(bulb)