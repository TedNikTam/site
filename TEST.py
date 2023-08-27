class Purse:

    def __init__(self, valuta, name ='Unknown'):
        self.money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balanse(self, howmuch):
        self.money = self.money + howmuch

    def top_down_balance(self, howmuch):
        if self.money - howmuch < 0:
            print('Недостаточно средств!')
            raise ValueError ('Недостаточно средств!!!')
        self.money = self.monye - howmuch

    def info(self):
        print(self.money, self.valuta, self.name)

x = Purse('USD')
y = Purse('EUR', 'Bill')
x.top_up_balanse(100)
x.info()
y.info()
x.top_down_balance(200)

