
#Instance Method
class Laptop:
    storage_type="SSD"
    
    def __init__(this, ram, rom):
        this.ram=ram
        this.rom=rom
        
    def get_info(this):
        print(f"laptop has {this.ram} and {this.rom} {this.storage_type}") #accessing the class attribute and instanc attribut so this is 
        #instance mthod
    
    @classmethod
    def get_storage(this):
        print(f"laptop is {this.storage_type} ") ##its only accessing class attribute so this is class instance
        
    @staticmethod #not have any compalcery parameter 
    def cal_discount(price, discount):
        return price *(100-discount)/100

l1= Laptop("16GB", "512GB")
l1.get_info() #instance method
Laptop.get_storage()  #class method
print(l1.cal_discount(40000,10)) #static method