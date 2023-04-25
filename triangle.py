side1 = int(input('Enter side one: '))
side2 = int(input('Enter side two: '))
side3 = int(input('Enter side three: '))

scalene = 0
rightangled = 0
isoceles = 0
equilateral = 0

if sum([side1,side2,side3]) <= (max([side1,side2,side3])*2):
    print('Does Not Form A Triangle!!!')
else:
    if len({side1,side2,side3}) == len([side1,side2,side3]):
        scalene = 1
    if len({side1,side2,side3}) == 2:
        isoceles = 1
    if len({side1,side2,side3}) == 1:
        isoceles = 1
        equilateral = 1
    if ((max([side1,side2,side3]))**2)*2 == sum([side1**2,side2**2,side3**2]):
        rightangled = 1
print('The triangle is:\n' + scalene*' -Scalene\n' + isoceles*' -Isoceles\n' + equilateral*' -Equilateral\n' + rightangled*' -Rightangled')
    