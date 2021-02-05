class nisit :
    def __init__(self,name,year,saka,provin) :
        self.name = name
        self.year = year
        self.saka = saka
        self.provin = provin
    def split_input(self) :
        global hello
        if text[1] == 'หญิง' :
            hello = 'สวัสดีค่ะ ดิฉันชื่อ '
        elif text[1] == 'ชาย' :
            hello = 'สวัสดีครับ ผมชื่อ '
    def show_input(self) :
        print(hello,self.name,'นักศึกษาชั้นปีที่ ',self.year,'สาขา',self.saka,'มาจากจังหวัด',self.provin)

def input_data() :
    global name , year , saka , provin , text
    print('-'*30,'แนะนำตัว','-'*60)
    data = input('ชื่อ สกุล:เพศ:ชั้นปี:สาขาวิชา:จังหวัดภูมิลำเนา:\t')
    text = data.split(':')
    name = text[0]
    year = text[2]
    saka = text[3]
    provin = text[4]

input_data()
x = nisit(name,year,saka,provin)
x.split_input()
x.show_input()