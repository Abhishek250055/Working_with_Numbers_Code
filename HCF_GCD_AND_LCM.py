#HCF

def hcf(num1,num2):
    for i in range(1,(num1+1 or num2+1)):
        if num1%i==0 and num2%i==0:
            hcf=i
    return hcf

def lcm(num1,num2):
    lcm=(num1*num2)//hcf(num1,num2)
    return lcm

num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))
print(f"HCF: {hcf(num1,num2)}")
print(f"LCM: {lcm(num1,num2)}")
