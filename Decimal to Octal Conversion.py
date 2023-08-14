def convertOctal(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%8)
        num = num//8
    for j in binaryArray:
        print(j, end="")


decimal_num = 21
convertOctal(decimal_num)