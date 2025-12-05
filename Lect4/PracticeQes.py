
class Product:
    count=0
    
    def __init__(self,  name,price):
        self.name=name
        self.price=price
        Product.count+=1
        
    @classmethod
    def get_total_Pdct(self):
        print(f"{self.count}")
        
    @staticmethod
    def cal_discount(price,per):
        print(price*(100-per)/100)
        
p1=Product(1233,"cover")
p1.get_total_Pdct()
p2=Product("Shooes",124422)
p3=Product("Shooes",124422)
p4=Product("Shooes",124422)
p5=Product("Shooes",124422)

p1.get_total_Pdct()