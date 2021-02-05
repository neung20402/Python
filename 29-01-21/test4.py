'''aaa = {'aaa':555,'bbb':666,'ccc':777}
print(aaa.popitem())
print(aaa.popitem())

if n == 'ชนิดคำศัพท์' :
    for x , y in type_dict.items():
        if m == x :
            print(x,y,'\t',end=' ')

for m,n in add_dict.items() :
        if n == 'คำศัพท์' :
            print('\t',m,'\t',end=' ')
        
        if n == 'ความหมาย' :
            print(m,'\t') 

x = 0
num = [100,1,2,3,4]
for x in num :
    print(x)
    num.remove(1)
    num.append(10)
    #print(x)
    if x == 10 :
        break

    for m,n in type_dict.items() :
        for o in add_dict.keys() :
            if m == o :
                print(m,n,'\t',end=' ')
                #del add_dict[m]
                #add_dict[k]=v'''

'''a = 0
wer = {444:777,555:888}
asd = list(wer.items())
while True :
    a +=1
    for x,y in asd:
        #print(x,y)
        wer[666]=999
        asd = list(wer.items())
        for m,n in asd :
            print(m,n)
            #print(asd)
    
        #print(asd[a-1])
        print(asd[-1])
        if '(666, 999)' == asd[-1] :
            break
        #print(wer)
#popdict = dict_1.pop()
#print(popdict)'''

'''d = {'a': [1], 'b': [1, 2], 'c': [], 'd':[]}

for i in d.copy():
    print(d[i])
    if not d[i]:
        d.pop(i)       
print(d)
d
{'a': [1], 'b': [1, 2]}'''

'''thisdict = {'asd':['n.',2,3],'wer':[4,5,6]}
thislist = thisdict['asd']
for x in thislist :
    print(x,'\t',end=' ')'''

'''thislist = ['n.','n.']
for x in thislist :
    print(x)
    del thislist[0]
    for y in thislist :
        print(x,y)'''

'''def expo(n,p) :
    return n**p
num = int(input())
power = expo(2,p=num)

print(power)'''

loop = int(input('Enter NUmber for Loop : '))
max = 0
for i in range(loop) :
    num_max = int(input('Enter Number : '))
    if max <= num_max :
        max = num_max

print(max)