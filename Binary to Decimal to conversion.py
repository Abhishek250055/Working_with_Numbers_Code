def bin_dec(num):
    de=0
    base=1
    while(num!=0):
        last_digit=num%10
        de+=last_digit*base
        num//=10
        base=base*2
    return de

def python_bin_dec(num):
    return int(num,2)

bi=int(input("Enter binary number: "))
print(f"dec: {bin_dec(bi)}")
# print(f"dec: {python_bin_dec(input())}")