# FnClassObject
# ฟังก์ชั่นที่ทำงานร่วมกับ Class และ Object

# isinstance และ dir คือฟังก์ชั่นที่ทำงานร่วมกับ class และ object
# โดยมีรายละเอียด ดังนี้
# isinstance => เช็คว่า object นี้ถูกสร้างจาก class ที่เรานิยามหรือไม่
# dir => แสดง attribute และ method
# __class__ => แสดงชื่อ class และ object

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {} '.format(self.department))

emp1 = Employee('รุจิกร', 50000, 'ปวส.2')
emp2 = Employee('บัวระบัติ', 25000, 'HTD2')
emp3 = Employee('alther', 20000, 'นักกีฬา')
emp4 = Employee('plim', 50000, 'HR')

print(isinstance(emp1, Employee)) # ตรวจสอบว่า object ถูกสร้างจาก class ที่ตรวจสอบไหม
print(dir(emp1))
print(dir(emp1.showData()))
print(emp1.__class__)