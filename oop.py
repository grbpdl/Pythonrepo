# A simple example class
class Test:
    def fun(self):#self is used if there is no argument then self acts as pointer in c
    	print (f"Hello {self.name}")

    @staticmethod #we dont have to use self 
    def fun1():
    	print("good morling")

obj = Test()
obj.name="gaurab"
obj.fun()
obj.fun1()
Test.a=6 #it is class instance
Test.b=6
obj.b=5# it is object instance(it has more priority if both instance are present)
print(obj.a)
print(obj.b)

# A Sample class with init method
class Person:

	# init method or constructor ,same as constuctor in c
	def __init__(self, name): #self is always passed and other arguments inatialized as self.argument
		self.name = name

	def say_hi(self):
		print(' my name is', self.name)

p = Person('Gaurab')
p.say_hi()

# An empty class
class null:
    pass