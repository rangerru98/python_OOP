# เขียนโปรแกรมสร้าง class ชื่อ people โดยมี attribute และ method ดังนี้
# attribute
#   name เป็นชื่อของบุคคล
#   age เป็นอายุของบุคคล
# method
#   introduce() เมื่อเรียกใช้จะพิมพ์ข้อความ
#   My name is <name>, i'm <age> year old

class people:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def introduce(self):
        print("My name is {} I'm {} year old".format(self._name,self._age))

pp01 = people('rujikorn', 21)
pp01.introduce()