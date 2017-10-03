def pos(thing):
    row = thing/8
    col = thing % 8
    arr = [col, row]
    return arr
#The function above finds the location on an (X, Y) plane for the index
    
def knightsShortest(entry,exit):
    Main=[
        #This is a BFS plot of a starting point up til the very corners of the chess board that holds the moves needed.
        [5,4,5,4,5,4,5,6],
        [4,3,4,3,4,5,4],
        [3,4,3,4,3,4],
        [2,3,2,3,4],
        [3,2,3,2],
        [2,1,4],
        [3,2],
        [0]
        #Based off of how we entered the data, we start from the last index in Main and move backwards.
    ]
    p1 = pos(entry)
    p2 = pos(exit)
    #Set a variable for the position for exit and entry using the pos function defined previously.
    d1 = abs(p1[0] - p2[0])
    d2 = abs(p1[1] - p2[1])
    dist = [d1, d2]
    #Finds the absolute value of x distance and the y distance between two points.
    if(d1 > d2):
        temp=Main[len(Main)-d1][d2-1]
        #Sets a variable of the longer of the (X,Y) of distance and finds the index of the opposite axis in the index of the array
        print "Position {} is {} moves away from position {}".format(str(entry), str(temp), str(exit))

    else:
        temp=Main[len(Main)-d2][d1-1]
        #Sets a variable of the longer of the (X,Y) of distance and finds the index of the opposite axis in the index of the array
        print "Position {} is {} moves away from position {}".format(str(entry), str(temp), str(exit))


knightsShortest(3, 34)
    