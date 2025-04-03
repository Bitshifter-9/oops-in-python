class hlo: # class
    name="pranav"
s1=hlo() # object
print(s1.name)

class car:
    colour="red"
    brand="bugati"
print(car().colour,car().brand)

class hlo1: 
    name="pranav"
    def __init__(self):
        print("hlo world")
        print(self) # it is giving location 
s1=hlo1() # object

class hlo2: 
   
    def __init__(self,fullname):
        self.name=fullname

s1=hlo2("pranav")
print(s1.name) # object
print(hlo2("pranav").name+" 2")  

class hlo3:
    coll="nst"
print(hlo3.coll) 
print(hlo3().coll)

class hlo4:
    coll="nst"
    def __init__(self,coll):
        self.coll=coll
print(hlo4.coll) # here print(hlo4().coll) is not working
print(hlo4("nst-p").coll) 

class hlo5:
    coll="nst"
    def __init__(self,name):
        self.nam=name
    def x(self):
        return("hlo"+" "+self.nam)
print(hlo5("pranav").x())
 
class h1:
    @staticmethod #decorator
    def x():
        print(" pranav without self , you need to use @staticmethod ")
h1.x()

class bank:
    def __init__(self,balance):
        self.balanc=balance

    def get_bala(self):
        return self.balanc
    def get_amount(self,amo):
        return self.get_bala()+amo
print(bank(100).get_amount(101))