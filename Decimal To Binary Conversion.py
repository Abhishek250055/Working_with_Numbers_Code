# Decimal To Binary Conversion

def dec_bin(num):
    l=[]
    while num>0:
        l.append(num%2)
        num//=2
       
    for i in l:
        print(i , end="")

de=int(input("enter number: "))
print(dec_bin(de))