# ชื่อ ,เงินเดือน
class Employee: #การสร้าง class
    # สร้าง method
    def detail(self, name, salary, department):
        # สร้าง Attribute
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {} '.format(self.department))

# Attribute เป็นกลไกลที่กำหนดคุณสมบัติให้กับ class
# การสร้าง Attribute
    # self.name = ชื่อพนักงาน
    # self.salary = เงินเดือน
    # self.age = อายุของพนักงาน

# method เป็นกลไกลที่กำหนดพฤติกรรมให้กับ class
# การสร้าง Method
#   def getName(self):
#       return self.name
# การเรียกใช้งาน
#   ชื่อวัตถุ.getName()

# คีย์เวิร์ด self
#   การสร้างคีย์เวิร์ด self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
#   ให้บอกตัวตนของวัตถุนั้น ๆ เช่น การกำหนดคุณสมบัติต่าง ๆ ในวัตถุ

# constructor
# เป็น method พิเศษที่ถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ(ไม่ระบุก็ได้)
# โครงสร้างconstructor
#   def __init__(self):

# การสร้างวัตถุ

emp1 = Employee()
emp1.detail('รุจิกร', 50000, 'ปวส1')
emp1.showData()

emp2 = Employee()
emp2.detail('บัวระบัติ', 25000, 'HTD2')
emp2.showData()

emp3 = Employee()
emp3.detail('alther', 20000, 'นักกีฬา')
emp3.showData()