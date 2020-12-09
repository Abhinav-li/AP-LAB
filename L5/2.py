class Vehicle:
    def __init__(self, name, idno, mfname):
        self.name = name
        self.idno = idno
        self.mfname = mfname

    def display(self):
        print('Details: ', self.name,' ', self.idno,' ', self.mfname)

class Passengers(Vehicle):

    def __init__(self, name, idno, mfname, passengerno):
        super().__init__(name, idno,mfname)
        self.passengerno = passengerno
    
    def display(self):
        print('Details: ', self.name,' ', self.idno,' ', self.mfname, self.passengerno)

print('Vehicle Details: ')

name = (input('Enter Name: '))
idno = int(input('Enter ID no: '))
mfname = (input('Enter Manufacturer: '))

obj = Vehicle(name, idno, mfname)
obj.display()

print('Passengers Details: ')

name = (input('Enter Name: '))
idno = int(input('Enter ID no: '))
mfname = (input('Enter Manufacturer: '))
passengeres = int(input('Enter no of  Passengers: '))

obj1 = Passengers(name, idno, mfname, passengeres)
obj1.display()