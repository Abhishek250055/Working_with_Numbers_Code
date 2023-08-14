
def octa_dec(num):
    de=0
    base=1
    while(num!=0):
        last_digit=num%10
        de+=last_digit*base
        num//=10
        base=base*8
    return de

oc=int(input("Enter octal number: "))
print(f"dec: {octa_dec(oc)}")
