.. activecode:: lst_st
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Recursion
    :subchapter: pythondsSierpinskiTriangle
    :topics: Recursion/pythondsSierpinskiTriangle
    :from_source: T
    :caption: Drawing a Sierpinski Triangle
    :nocodelens:

    #Recursive example of the Sierpinski Triangle.

    import turtle

    def drawTriangle(points,color,myTurtle):
    #Draws a triangle using the diven points and color.
        myTurtle.fillcolor(color)
        myTurtle.up()
        myTurtle.goto(points[0][0],points[0][1])
        myTurtle.down()
        myTurtle.begin_fill()
        myTurtle.goto(points[1][0],points[1][1])
        myTurtle.goto(points[2][0],points[2][1])
        myTurtle.goto(points[0][0],points[0][1])
        myTurtle.end_fill()

    def getMid(p1,p2):
        return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def sierpinski(points,degree,myTurtle):
        colormap = ['blue','red','green','white','yellow',
                    'violet','orange']
        drawTriangle(points,colormap[degree],myTurtle)
        if degree > 0:
            sierpinski([points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])],
                    degree-1, myTurtle) #Recursive call
            sierpinski([points[1],
                            getMid(points[0], points[1]),
                            getMid(points[1], points[2])],
                    degree-1, myTurtle) #Recursive call
            sierpinski([points[2],
                            getMid(points[2], points[1]),
                            getMid(points[0], points[2])],
                    degree-1, myTurtle) #Recursive call

    def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    sierpinski(myPoints,3,myTurtle)
    myWin.exitonclick()

    main()