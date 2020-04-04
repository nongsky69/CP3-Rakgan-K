numX = int(input("จำนวนชั้น พิรามิด : "))
blankX = " "
for x in range(1, numX + 1):
    print(blankX * (numX - x), "*" * x + "*" * (x - 1))
