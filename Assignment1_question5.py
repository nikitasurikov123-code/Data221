def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    #checks that you input an integer, not a string
    try:
        #makes sure that radius of both circles is not 0
        if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
            return "Radius must be greater than 0"
        #calculates area of both circles. (assume pi = 3.14)
        areaOfCircle1 = (3.14)*(radiusOfCircle1**2)
        areaOfCircle2 = (3.14)*(radiusOfCircle2**2)
        #checks which of the circles area is bigger
        if areaOfCircle1 > areaOfCircle2:
            smallerCircle = areaOfCircle2
            largerCircle = areaOfCircle1
        else:
            smallerCircle = areaOfCircle1
            largerCircle = areaOfCircle2
        #finds the percentage of the smaller circle in the larger one
        return (smallerCircle/largerCircle)*100
    #if input is not an int, it returns this message
    except ValueError:
        return "Radius must be an int"
print(circleAreaCoverage(5, 4))