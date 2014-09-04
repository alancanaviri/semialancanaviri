class Circulo:
	def __init__(self,radio):
		self.radio=radio
	def darArea(self):
		return 3.14*self.radio*self.radio
ob=Circulo(2)
print ob.darArea()