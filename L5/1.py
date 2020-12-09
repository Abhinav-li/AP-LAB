class Employee:
    emplist = []
    def __init__(self, eid, name, sal, dept):
        self.data = (eid, name, sal, dept)
        Employee.emplist.append(self.data)

    def display(self):
        print('Details ', self.data)
    
    @staticmethod
    def search(eid):
        for i in Employee.emplist:
            if(eid == i[0]):
                print('Employee Found: ', i)
                return
        else:
            print('Not found')


n = int(input('Enter number of Employees: '))


for i in range(n):
    eid = int(input('Enter Employee Id: '))
    name = (input('Enter Name: '))
    sal = int(input('Enter salary: '))
    dept = input('Enter Department: ')

    obj = Employee(eid, name, sal, dept)

x = int(input('Enter id to search: '))
Employee.search(x)


