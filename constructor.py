# constructor
    # เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
    # โครงสร้าง Constructor
        # def __init__(self):
        #     pass

# destructor
# เป็น method พิเศาตรงข้างกับ constructor จะถูกใช้งานเมื่อ
# สิ้นสุดการทำงานของ class หรือจูกทำก่อนจะสลาย object
# ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
# โครงสร้าง
# def __del__(self):
# pass

# การสร้าง Constructor

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {} '.format(self.department))

    # มีหรือไม่มีก็ได้ destrutor
    def __del__(self):
        print('call destructor')

emp1 = Employee('รุจิกร', 50000, 'ปวส.2')
emp1.showData()

emp2 = Employee('บัวระบัติ', 25000, 'HTD2')
emp2.showData()

emp3 = Employee('alther', 20000, 'นักกีฬา')
emp3.showData()

emp4 = Employee('plim', 50000, 'HR')
emp4.salary = 20000
emp4.showData()