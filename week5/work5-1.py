class nisit :
    def __init__(self,name,year,saka,provin) :
        self.name = name
        self.year = year
        self.saka = saka
        self.provin = provin
    def split_input(self) :
        global hello
        if newtext[1] == 'หญิง' :
            hello = 'สวัสดีค่ะ ดิฉันชื่อ '
        elif newtext[1] == 'ชาย' :
            hello = 'สวัสดีครับ ผมชื่อ '
    def show_input(self) :
        print(hello,self.name,'นักศึกษาชั้นปีที่ ',self.year,'สาขา',self.saka,'มาจากจังหวัด',self.provin)
    def input_data(self) :
        print('-'*30,'แนะนำตัว','-'*60)
        return input('ชื่อ สกุล:เพศ:ชั้นปี:สาขาวิชา:จังหวัดภูมิลำเนา:\t')
    def split_data(self) :
        global name , year , saka , provin , newtext 
        text = nisit.input_data(None)
        newtext = text.split(':')
        name = newtext[0]
        year = newtext[2]
        saka = newtext[3]
        provin = newtext[4]

nisit.split_data(None)
x = nisit(name,year,saka,provin)
x.split_input()
x.show_input()
