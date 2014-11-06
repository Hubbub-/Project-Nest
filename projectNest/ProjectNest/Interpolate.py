def map(value, leftMin, leftMax, rightMin, rightMax):

    #Figure out how wide3 each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    #Compute the scale factor between the right and left values
    scaleFactor = float(rightSpan) / float(leftSpan)

    mapedValue = rightMin + (value - leftMin) * scaleFactor

    return mapedValue

#[------------------------Testing------------------------------------]#

#print Map(3, 0, 10, 0, 100)
