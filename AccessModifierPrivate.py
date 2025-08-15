class Employee:
    def __init__(self, name, salary, department):
        # public attribute
        self._name = name
        self._salary = salary
        self._department = department

    # public method
    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน = {}'.format(self._salary))
        print('แผนก = {}'.format(self._department))

emp1 = Employee('วิบูลย์', 50000, 'วิชาการ')
emp1._salary = 51000
emp1._showData()