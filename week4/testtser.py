from datetime import datetime
num_people = int(input('Enter number of competitor : '))
list_info, list_name ,list_score ,list_time ,list_hit ,liststage_pt ,liststage_per =[], [], [], [], [], [], []

for i in range (num_people) :
    info = input("Please enter (name,score,time) => ")
    list_info.append(info)
    splitinfo = info.split(",")
    list_name.append(splitinfo[0])
    list_score.append(splitinfo[1])
    list_time.append(splitinfo[2])
    list_hit.append(float(list_score[i])/float(list_time[i]))
    liststage_pt.append(((list_hit[i])/(max(list_hit)))*50)



now = datetime.today()
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print("-"*70+"\n{0:-<15}{1:-<10}{2:-<8}{3:-<20}{4:-<15}{5:-<20}{6}".format('No.','Points','TIME','CompetitorName','Hit factor','State Points','State Percents'))
for i in range (num_people):
    print("{0: <15}{1: <10}{2: <8}{3: <13}{4: <15}".format(list_name[i],list_score[i],list_time[i],'%4f'%list_hit[i],liststage_pt[i]))