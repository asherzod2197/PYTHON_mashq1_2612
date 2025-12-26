class Hisoblagich:
    def __init__(self):
        self.natija = 0         

    def qo'sh(self, son):
        self.natija += son
        print(f"+ {son} qo'shildi → hozir: {self.natija}")

    def ayir(self, son):
        self.natija -= son
        print(f"- {son} ayirildi → hozir: {self.natija}")

    def ko'paytir(self, son):
        self.natija *= son
        print(f"× {son} ko'paytirildi → hozir: {self.natija}")

    def bo'l(self, son):
        if son == 0:
            print("Xato: 0 ga bo'lib bo'lmaydi!")
        else:
            self.natija /= son
            print(f"÷ {son} bo'lindi → hozir: {self.natija}")

    def tozalash(self):
        self.natija = 0
        print("Hisoblagich tozalandi → 0")


calc = Hisoblagich()

calc.qo'sh(8)     
calc.ko'paytir(5)  
calc.ayir(12)       
calc.bo'l(4)          
calc.qo'sh(3.5)     

calc.tozalash()       
