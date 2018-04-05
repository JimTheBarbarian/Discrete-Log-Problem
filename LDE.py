from elisha import gcd2

class SuperTuple:
	def __init__(self, *args): 
		self.L = list(args)
	
	def __add__(self, other_tuple): 
		L = [sum(x) for x in zip(self.L, other_tuple.L)]
		return SuperTuple(*L) 

	def __sub__(self, other_tuple): 
		L = [x[0] - x[1] for x in zip(self.L, other_tuple.L)]
		return SuperTuple(*L) 

	def __mul__(self,other):
		if (type(other) == int) or (type(other) == float): 
			L = [other*x for x in self.L]
			return SuperTuple(*L)
		else: 
			raise TypeError("I only know how to multiply by a scalar")

	def __rmul__(self, other): 
		''' Left Multiplication just calls the method for right multiplication ''' 
		return self.__mul__(other)

	def __getitem__(self,key):
		return self.L[key]

	def __setitem__(self,key,value):
		self.L[key] = value 

	def __str__(self):
		return str(self.L)


def LDE(a,b,x):
	""" make sure a is larger than b
	"""
	DEBUG = False 

	x1 = SuperTuple(1,0)
	r = a % b
	q = a // b
	x2 = SuperTuple(0,1)
	if DEBUG: 
		print(f"{x1}")
		print(f"{x2}")
	if x % gcd2(a,b) != 0:
		raise TypeError("the gcd has to divide x my dude")
	while r > 0:
		x1 = x1 - q*x2
		x1, x2 = x2, x1 
		if DEBUG: 
			print(f"{x2}") 
		a = b  
		b = r 
		r = a % b 
		q = a // b
	print((x / gcd2(a,b)) * x2)
