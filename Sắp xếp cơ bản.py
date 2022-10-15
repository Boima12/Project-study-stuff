#nhap vao mang a
a = []
n = int(input("muon cho bao nhieu so? : "))
gt = 0

for i in range(n):
    a.append(int(input()))

#sap sep 
for i1 in range(len(a)):
    for i2 in range(i1,len(a)):
        if a[i2] > a[i1]:
            gt = a[i1]
            a[i1] = a[i2]
            a[i2] = gt
            print("da doi vi tri cua gia tri ",i1,"=",a[i2],"sang cho ",i2,"=",a[i1],"thanh cong ! hien gio ",i1,"=",a[i1])
    print()
    print("cac gia tri trong mang sau khi da thay doi vi tri sau vong lap thu ",i1+1," la :")
    print(a)
    if i1 == len(a)-1:
        print("da hoan thanh xong viec sap xep thu tu trong mang ( ͡° ͜ʖ ͡°)")
    else:
        print()
        print("bat dau viec sap xep vong lap lan thu ",i1+2)