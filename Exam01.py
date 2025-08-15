class Driver:
    def __init__(self, HP, generated_money):
        self.HP = HP
        self.gerenated_money = generated_money

    def driver(self):
        self.HP = self.HP - 10
        self.gerenated_money = self.gerenated_money + 10

    def care(self):
        self.HP = self.HP + 10
        self.gerenated_money = self.gerenated_money - 10

    def report(self):
        print("HP =", self.HP, "gerenated =", self.gerenated_money)

driver_A = Driver(100, 100)
driver_A.driver()
driver_A.report()
driver_A.care()
driver_A.report()