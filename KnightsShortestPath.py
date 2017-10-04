""" knightsPath() solution
        -Bret Farley
        -Nicolas Thacker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This program is designed with the intention of finding the shortest path that a
knight can take to get from one square on a chessboard to another. The function
knightsShortest() takes in 2 numbers which represent the the start and end point
expressed as indecies [0-63]. After studying chess theory, we decided to solve the
problem by utilizing a map of an infinite chessboard with all the minimum knight 
moves plotted on it. After some reflection, we realized there were certain test
cases (particularly moving diagonally along an edge piece) that our code did not 
work with. We are currently editing that.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The pos() function is designed to take in an index along the chessboard and return
an x and y coordinate along with a boolean that determines whether or not the index
in question is along a border.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
def pos(thing):
    row = thing/8
    col = thing % 8
    if (row == 0 or row == 7) or (col == 0 or col == 7):
        isEdge = True
    else:
        isEdge = False
    arr = [col, row, isEdge]
    return arr

    
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
    #testBy=[0,1,2,3,4,5,6,7,8,15,16,23,24,31,32,39,40,47,48,55,56,63]
    p1 = pos(entry)
    p2 = pos(exit)
    #Set a variable for the position for exit and entry using the pos function defined previously.
    d1 = abs(p1[0] - p2[0])
    d2 = abs(p1[1] - p2[1])
    dist = [d1, d2]
    #Finds the absolute value of x distance and the y distance between two points.
    if (p1[2] or p2[2]) and (dist == [1,1]):
        print "Special case: moving diagonally while next to border. Position {} is 4 moves away from position {}".format(str(entry), str(exit))
    elif(d1 > d2):
        # for i in range(0,len(testBy)):
            # if entry==testBy[i]:
            #     Main[6][1]=4     
            #If the entry spot is an edge piece, the moves to reach the spot directly diagonal to it goes from 2 to 4.
        temp = Main[len(Main)-d1][d2-1]
       #Sets a variable of the longer of the (X,Y) of distance and finds the index of the opposite axis in the index of the array
        print "Position {} is {} moves away from position {}".format(str(entry), str(temp), str(exit))

    else:
        # for x in range(0,len(testBy)):
        #     if entry==testBy[x]:
        #         Main[6][1]=4
             #If the entry spot is an edge piece, the moves to reach the spot directly diagonal to it goes from 2 to 4.
        temp=Main[len(Main)-d2][d1-1]
        #Sets a variable of the longer of the (X,Y) of distance and finds the index of the opposite axis in the index of the array
        print "Position {} is {} moves away from position {}".format(str(entry), str(temp), str(exit))


knightsShortest(3, 34)
knightsShortest(8, 1)
knightsShortest(0, 63)
    