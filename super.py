# super
# เมื่อต้องการเรียกใช้งานคูณสมบัติต่าง ๆ ในคลาสแม่
# เช่น Constructor, Method, Attribute
# super().__init__(name)
class Employee:
    #class variable
    minsalary = 12000
    maxsalary = 50000
    companyName = 'บริษัท XYZ จำกัด'


    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self.__department = department


    def _showData(self):
        print('ชื่อพนักงาน = '+self.__name)
        print('เงินเดือน = '+str(self.__salary))
        print('แผนก = '+self.__department)


class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self, name, salary):
        super().__init__(name, salary,self.__departmentName)
        super()._showData()

class Programmer(Employee):
    __departmentName = ('แผนกพัฒนาระบบ')
    def __init__(self, name, salary):
        super().__init__(name, salary,self.__departmentName)
        super()._showData()

class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self, name, salary):
        super().__init__(name, salary,self.__departmentName)
        super()._showData()

account = Accounting('นัท', 35000)
programmer = Programmer('โย', 50000)
sale = Sale('หนึ่ง', 25000)
