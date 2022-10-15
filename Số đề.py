import random, time

a = 0
b = 0
c = 0

print("SỐ ĐỀ !!!")
time.sleep(3)

while a<80000:
    a = random.randrange(10000,80002)
    b = random.randrange(0,100)
    c = random.randrange(0,10)
    print("đang tính toán số đề... :",a,"    điểm nhân phẩm hiện có :",b, "      số chuyện lạ diễn ra quanh xóm :",c)

a = random.randrange(0,100)
print("đã tìm được con số đề thích hợp --",a,"--bạn có muốn đánh con số đề này không?, Y/N")

c = 0
while c == 0:
    tl = input(str())
    if tl == "Y" or tl == "y" or  tl == "N" or  tl == "n":
        c += 1
        if a == 27 and (tl == "Y" or tl == "y"):
            print("BẠN ĐÃ TRÚNG SỐ ĐỀ VỚI CON SỐ",a,", giờ bạn đã có tiền để uống trà sữa mà không phải bom hàng nữa, xin chúc mừng bạn")
        elif (tl == "Y" or tl == "y") and a != 27:
            print("có lẽ ông trời đã không độ bạn rồi, thôi thua keo này mình khỏi bày keo khác vì giờ hết tiền rồi :d")
        elif tl == "N" or tl == "n" :
            print("bạn đã quyết định tu dưỡng tịnh tâm, không cá độ số đề nữa, điểm nhân phẩm của bạn +1")
    else : print("vui lòng nhập chữ Y hoặc N !!!")

#all the code here was written by Cao Hoang Phuoc Bao (handsomer)