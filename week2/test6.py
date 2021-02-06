list_order = []
for i in range(1,6):
    n1=input("หยิบสินค้าค้าชิ้นที่ %d\t"%i)
    list_order.append(n1)

print("สินค้าที่อยู่ในตะกร้านี้")
for n in range(0,len(list_order)):
    print('{0}{1}{2}'.format(n+1,'. ',list_order[n]))