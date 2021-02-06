'''global aaa 
class market :
    def __init__(self,name = [],price = []) :
        self.name = name
        self.price = price
    @classmethod
    def input_data(cargo_name) :
        
        return cargo_name(input('เพิ่มรายการสินค้า : '),input('เพิ่มราคาสินค้า : '))

while True :
    call = market.input_data()
    x=market(cargo_name)
    
    print(x.name)'''
global ddd
class StackOverflowUser:

    def __init__(self, name, userid, rep): 
        self.name = name
        self.userid = userid
        self.rep = rep

    #@classmethod
    def from_input(self):
        
        return input('Name: '),int(input('User ID: ')), int(input('Reputation: '))

    def show(self) :
        print(self.name,self.userid,self.rep)
aaa = {}
user = StackOverflowUser.from_input(None)
'''s1 = str(user)
print(s1)
print(type(s1))'''
aaa = user[0]
bbb = user[1]
ccc = user[2]
print(aaa,bbb,ccc)
'''x=StackOverflowUser(aaa,bbb,ccc)
x.show()'''