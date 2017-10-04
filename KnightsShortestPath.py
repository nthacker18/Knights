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
        [0],
        [3,2],
        [2,1,4],
        [3,2,3,2],
        [2,3,2,3,4],
        [3,4,3,4,3,4],
        [4,3,4,3,4,5,4],
        [5,4,5,4,5,4,5,6]

    ]
    """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                    COMPONENTS
    Above: this is our plot of the infinite chessboard, limited to the maximum distance
    across the chessboard. So it's technically finite. Fight me.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Below: We use the pos() function to find the distance in the respecive x and y 
    coordinates. Then we take the absolute value of each in order to traverse the
    knight's move plot.
    p1: position 1
    p2: position 2
    dX: distance in x coordinate
    dY: distance in Y coordinate
    dist: Array of distance in bot coordinates
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    """
    p1 = pos(entry)
    p2 = pos(exit)
    dX = abs(p1[0] - p2[0])
    dY = abs(p1[1] - p2[1])
    dist = [dX, dY]
   
   """ 
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                        LOGIC
   There are 3 steps within our logic:
   1) Is one of the squares on a border and is the move a single diagonal move?
        -If so, the minimum number of moves is 4. We know this from playing with the
        chessboard in the lobby.

   2) Is X-distance greater than the Y-distance?
        -if so, we need to make sure we use the x-distance to traverse "vertically" on
        our plot and use the y-distance to traverse "horizontally". While it seems
        confusing from a traditional matematics standpoint, the plot is shaped as a 
        cone of sorts so we need the loger distance to traverse the longer side of the
        cone.

   3) Otherwise the Y-distance is greater than or equal to the X-distance, meaning we
      do not need to invert the x and y axis.
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   """
    if (p1[2] or p2[2]) and (dist == [1,1]):
        print "Position {} is 4 moves away from position {}".format(str(entry), str(exit))
    
    elif(dX > dY):
        temp = Main[dX][dY]
        print "Position {} is {} moves away from position {}".format(str(entry), str(temp), str(exit))

    else:
        temp=Main[dY][dX]
        print "Position {} is {} moves away from position {}".format(str(entry), str(temp), str(exit))

    #in both the elif and else statements, temp just stores the value gained from the plot

#some tests of different cases:

knightsShortest(3, 34)
knightsShortest(8, 1)
knightsShortest(0, 63)
knightsShortest(7, 56)