import math

# Parent class
class Triangle :

	# Class Attribute
	edge = 3
	
# Child class (inherits from Triangle() class)
class Equilateral(Triangle) :
	def __init__(self, base, height) :
		self.base = base
		self.height = height
		
	def Area(self) :
		return "The area is {}".format(0.5 * self.height * self.base)
	
	def Perimeter(self) :
		return "The perimeter is {}".format(3 * self.base)
	

# Child class (inherits from Triangle() class)
class Isosceles(Triangle) :
	def __init__(self, base, height) :
		self.base = base
		self.height = height
		
	def Area(self) :
		return "The area is {}".format(0.5 * self.height * self.base)
	
	def Perimeter(self) :
		return "The perimeter is {}".format(self.base + (2 * (math.sqrt(self.height**2 + ((self.base**2)/4)))))
		
class Quadrangle :
	
	# Class Attribute
	edge = 3
	
# Child class (inherits from Quadrangle() class)
class Square(Quadrangle) :
	def __init__(self, length, width) :
		self.length = length
		self.width = width
		
	def Area(self) :
		return "The area is {}".format(self.length * self.width)
		
	def Perimeter(self) :
		return "The area is {}".format(2 * (self.length + self.width))

# Child class (inherits from Quadrangle() class)
class Trapezoid(Quadrangle) :
	def __init__(self, base1, base2, height) :
		self.base1 = base1
		self.base2 = base2
		self.height = height
		
	def Area(self) :
		return "The area is {}".format((self.base1 + self.base2) * self.height / 2)
		
	def Perimeter(self) :
		return "The area is {}".format(base1 + base2 + height + math.sqrt((base1 - base2)**2 + height**2))
		
# Child class (inherits from Quadrangle() class)
class Parallelogram(Quadrangle) :
	def __init__(self, base, height) :
		self.base = base
		self.height = height
		
	def Area(self) :
		return "The area is {}".format(self.base * self.height)
		
	def Perimeter(self) :
		return "The area is {}".format(2 * (self.base + (self.height / math.sin(45))))