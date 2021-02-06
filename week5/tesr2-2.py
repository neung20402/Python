import os
class market :
    def __init__(self,name_list = ['มาม่า','ลาบ','ส้มตำ','ข้าวแกง'],price_list = [12 , 60 , 40 , 25]) :
        self.name = name_list
        self.price = price_list
    def list_def(self) :
        print('{0:-<15}{1:-<15}{2:-<15}'.format('-','รายการสินค้ามีดังนี้','-'))
        print('{0: <10}{1: <30}{2: <10}'.format('ลำดับ','ชื่อส้นค้า','ราคาสินค้า'))
        for x in range(0,len(self.name)) :
            print('{0: <10}{1: <25}{2: <5}บาท'.format(x+1,self.name[x],self.price[x]))
    def choose(self) :
        print('*'*15,'หนึ่งโภชนา','*'*15)
        print('\tแสดงรายการวินค้า [a]\n\tเพิ่มรายการสินค้า [s]\n\tออกจากระบบ [x]')
    def input_choise(self) :
        global choise
        choise = input('กรุณาเลือกคำสั่ง :\t')
    def from_input_name(self) -> str:
        return input('เพิ่มราคาสินค้า : ')
    def from_input_price(self) -> int :
        return input('เพิ่มชื่อสินค้า : ')
    def add_list(self) : 
        while True :
            print('เพิ่มรายการสินค้า หากต้องการออก กรอก exit')
            add_name = market.from_input_name(None)
            if add_name == 'exit' :
                break
            else :
                add_price = market.from_input_price(None)
                self.name.append(add_name)
                self.price.append(add_price)
            add = input('ต้องการเพิ่มสิ้นค้าอีกหรือไม่ [y/n] : ')
            if add == 'n' :
                break
            elif add == 'y' :
                os.system('cls')

while True :
    x = market()
    x.choose()
    x.input_choise()
    if choise == 'a' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        x.list_def()
    if choise == 's' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        x.add_list()
    if choise == 'x' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง :\t',choise)
        close = input('ต้องการปิดโปรแกรมใช่หรือไม่ [y/n] : ')
        if close == 'n' :
            os.system('cls')
        if close == 'y' :
            os.system('cls')
            print('ปิดโปรแกรมเรียบร้อย')
            break