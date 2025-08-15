# AccessModifier
# คือระดับในการเข้าถึง class attribute method และอื่นๆ ในภาษาวัตถุ
# โดยมีประโยชน์อย่างมากในเรื่องของการกำหนดระดับการเข้าถึง
# สิทธิในการเข้าใช้งาน การซ้อนข้อมูล และอื่นๆ

# Public คือการประกาศระดับการเข้าถึงที่เข้มงวดน้อยที่สุด หรือกล่าวได้ว่าใคร ๆ ก็สามารถเข้าถึงและเรียกใช้งานได้

# protected(_) เป็นการประกาศระดับการเข้าถึงเฉพาะคลาสของตัวมันเองและคลาสลูกที่สืบทอดคุณสมบัติไปใช้เท่านั้น

# private(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของตัวมันเองเท่านั้นที่มีสิทธิใช้งานได้

class Employee:
    def __init__(self, name, salary, department):
        # public attribute
        self.name = name
        self.salary = salary
        self.department = department

    # public method
    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {} '.format(self.department))

emp1 = Employee('รุจิกร', 50000, 'ปวส.2')
emp1.salary = 51000
emp1.showData()