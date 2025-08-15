# เขียนโปรแกรมสร้าง class ชื่อ people โดยมี attribute และ method ดังนี้
# attribute
#   name เป็นชื่อของบุคคล
#   age เป็นอายุของบุคคล
# method
#   aging(year) รับ parameter 1 ตัว คือ year
#    - แสดงอายุปัจจบัน
#    - เพิ่มอายุขึ้นเท่ากับ year
#    - แสดงอายุหลังเพิ่มแล้ว

class people:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def aging(self, year):
        print("My name is {} I'm {} year old".format(self._name, self._age))
        self._age += year
        print('after aging {} year, {} new age is {} year old'.format(year,self._name,self._age))

pp01 = people('rujikorn', 21)
pp01.aging(3)