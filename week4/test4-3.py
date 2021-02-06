import datetime
con = int(input('Enter Condtion : '))
loop = int(input('\nEnter Number of competitor : '))
print('-'*30)
name_list , score_list , time_list , hit_fac_list = [] , [] , [] , []
for i in range(loop) :
    input_data = input('Please Enter (name,score,time)')
    split_data = input_data.split(',')
    name_list.append(split_data[0])
    score_list.append(split_data[1])
    time_list.append(split_data[2])
    hit_fac_list.append(int(score_list[i])/float(time_list[i]))

for x in range(loop) :
    y = x
    for y in range(loop) :
        if hit_fac_list[x] > hit_fac_list[y] :      #หากตำแหน่งในลูปก่อนมีค่ามากกว่าลูปหลัง จะเข้าเงื่อนไข
            q,w,e,r = hit_fac_list[x],name_list[x],score_list[x],time_list[x]           #นำ list ที่มีค่าในตำแหน่งนั้นๆมากกว่าไปเก็บไว้ในตัวแปรใหม่
            hit_fac_list[x],name_list[x],score_list[x],time_list[x] = hit_fac_list[y],name_list[y],score_list[y],time_list[y]   #นำค่าที่น้อยกว่าไปแทนที่ใน list ที่มีค่ามากกว่า
            hit_fac_list[y],name_list[y],score_list[y],time_list[y] = q,w,e,r   #นำค่าที่เก็บไว้ในตัวแปรใหม่มาแทนที่ลงใน list ที่มีค่าน้อยกว่า 
                                                                                #จะทำให้เกิดการหมุนเวียน นำ list ที่ตำแหน่งหลังที่มีค่ามากกว่ามาแทนลงใน list ตำแหน่งก่อนที่มีค่าน้อยกว่า
                                                                                #ทำให้เกิดการเรียงจากค่ามากกว่าไปน้อยกว่าภายใน list นั้นๆ

date_now = datetime.datetime.now()
show_date = date_now.strftime('%G-%m-%d %H:%M:%S')
print('Shotgun ',date_now.strftime('%A'),' Training ',date_now.strftime('%Y'))
print('Condtion : ',con)
print(show_date)
print('-'*120)
print('{0: <15}{1: <15}{2: <15}{3: <20}{4: <15}{5: <15}{6}'.format('No.','PTS','TIME','COMPETITOR#name','HIT FACTOR','STATE POINTS','STATE PECCENT'))
print('-'*120)
for i in range(loop) :
    ste_po = (hit_fac_list[i]/max(hit_fac_list))*50
    ste_pe = (ste_po/((max(hit_fac_list)/max(hit_fac_list)*50)))*100
    print('{0: <15}{1: <15}{2: <15}{3: <20}{4: <15}{5: <15}{6}'.format(i+1,score_list[i],time_list[i],name_list[i],'%.4f'%hit_fac_list[i],'%.4f'%ste_po,'%.4f'%ste_pe))