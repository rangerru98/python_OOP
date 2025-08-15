# เขียนโปรแกรมสร้าง class Tree โดยมี attribute และ method ดังนี้
# attribute
#     height เป็นความสูงต้นไม้
#     width เป็นกว้างต้นไป
#     generated_money เป็นเงินที่หาใต้
# method
#     feed_A() ท่าหน้าที่แสดงด่าเงินที่หาใต้ และความกว่างของต้นไม้หลังจากให้ปียชนิด A
#     โดยจะลด generated_money 10 หน่วย แต่จะเพิ่ม wigth 12 หน่วย
#     feed_8() ท่าหน้าที่แสดงด่าเงินที่หาใด และความสูงของต้นไม่หลังจากให้ปียชนิด B
#     โดยจะลด generated_money 8 หน่วย แต่จะเพิ่ม height 10 หนวย
#     sell() ท่าหน้าที่แสดงตาจ่านวนเงินที่นายต้นไม่ใต้ โดย generated_money จะเพิ่มเท่ากับ
#     width * height ** 0.8

class Tree:
    def __init__(self, height, width, generated_money):
        self.height = height
        self.width = width
        self.generated_money = generated_money

    def feed_A(self):
        self.generated_money = self.generated_money - 10
        self.width = self.width + 12

    def feed_B(self):
        self.generated_money = self.generated_money - 8
        self.height = self.height + 10

    def sell(self):
        self.generated_money = self.generated_money + self.width * self.height ** 0.8
        print("width =", self.width, "Height =", self.height)
        print("generated_money =", self.generated_money)

Tree_A = Tree(10, 10, 1000)
Tree_A.feed_A()
Tree_A.feed_B()
Tree_A.sell()

print("")

Tree_B = Tree(23, 8, 254)
Tree_B.feed_A()
Tree_B.feed_B()
Tree_B.sell()

print("")

Tree_C = Tree(300, 14, 8850)
Tree_C.feed_A()
Tree_C.feed_B()
Tree_C.sell()
