class Base():
    def getno(self):
     self.a=("enter no")
    def show(self):
        print(self.a)

class Derrived(Base):
    def getvalue(self):
       self.b=("enter no")

    def show(self):
        print(self.b)
b=Base()     
d=Derrived()
b.getno()
b.show()
d.getvalue()
d.show()