list = []
x=0
for i in range(1,6):
    n1=input("หยิบสินค้าค้าชิ้นที่ %d\t"%i)
    list.append(n1)

print("สินค้าที่อยู่ในตะกร้านี้")
for n in range(0,5):
    print(n+1,'. ',list[n])

print("1.",list[0])
print("2.",list[1])
print("3.",list[2])
print("4.",list[3])
print("5.",list[4])