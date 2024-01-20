def corners_inside(rectangle1, rectangle2):
    def is_inside(x, y, rect):
        return rect[0] <= x <= rect[2] and rect[1] <= y <= rect[3]

    inside_corners = []

    # Check each corner of the second rectangle
    for corner_name, (corner_x, corner_y) in zip(['lower-left', 'upper-left', 'lower-right', 'upper-right'],
                                                  [(rectangle2[0], rectangle2[1]),
                                                   (rectangle2[0], rectangle2[3]),
                                                   (rectangle2[2], rectangle2[1]),
                                                   (rectangle2[2], rectangle2[3])]):
        if is_inside(corner_x, corner_y, rectangle1):
            inside_corners.append(corner_name)

    return inside_corners




data = []
with open('jan2023practice/billboard2/billboard.in', 'r') as infile:
    for x in range(2):
        data.append([int(x) for x in infile.readline().split()])

lawnmowerBoard = data[0]
otherBoard = data[1]

lawnLL = [lawnmowerBoard[0], lawnmowerBoard[1]]
lawnLR = [lawnmowerBoard[2], lawnmowerBoard[1]]
lawnUL = [lawnmowerBoard[0], lawnmowerBoard[3]]
lawnUR = [lawnmowerBoard[2], lawnmowerBoard[3]]
otherLL = [otherBoard[0], otherBoard[1]]
otherLR = [otherBoard[2], otherBoard[1]]
otherUL = [otherBoard[0], otherBoard[3]]
otherUR = [otherBoard[2], otherBoard[3]]

cornersCovered = [0,0,0,0]
# check if other board covers LL corner
#if (otherBoard[2] > lawnmowerBoard[0] and otherBoard[3] > lawnmowerBoard[1]) and (otherLL[0] <= lawnLL[]):
resultArea = 0
if len(corners_inside(lawnmowerBoard, otherBoard)) <= 1:
    resultArea = (lawnLR[0]-lawnLL[0]) * (lawnUL[1]-lawnLL[1])
else:
    pass

