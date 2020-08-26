#area of polygon...refer http://www.wikihow.com/Calculate-the-Area-of-a-Polygon for the method
from math import tan, radians

def ar():
    num = int(input("Enter number of sides of the regular polygon: "))
    side = int(input("Enter the length of its side: "))

    angle = 360/(2 * num)                           
    angrad = radians(angle)         

    apothem = (side/2) * (1/(tan(angrad)))
    perimeter = num * side

    area = (1/2) * apothem * perimeter

    print("The area is %s" % round(area,3))

ar();
