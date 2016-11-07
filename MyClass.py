import math
import matplotlib.pyplot as plt

class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''
    
    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.X = x
        self.Y = y

    def move(self, dx, dy):
        '''Determines where x and y move'''
        self.X = self.X + dx
        self.Y = self.Y + dy

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx ** 2 + dy ** 2)

class LineString(object):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = start_point.distance(end_point)
    def DrawLine(self):
        point_list = []
        point_list.append([self.start_point.getX(), self.start_point.getY()])
        point_list.append([self.end_point.getX(), self.end_point.getY()])
        plt.plot(*zip(*point_list))
        #plt.show()

class Road(LineString):
    def __init__(self, id, floor, start_point, end_point):
        LineString.__init__(self, start_point, end_point)
        self.id = id
        self.floor = floor
        self.length = start_point.distance(end_point)

'''Testing
'''
point_a = Point(1, 4)
point_b = Point(5, 1)
line_c = LineString(point_a, point_b)
road_d = Road(1, 2, point_a, point_b)
#road_d.DrawLine()
#plt.plot(point_a, point_b)
#'''
