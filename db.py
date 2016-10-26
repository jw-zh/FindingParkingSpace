#coding=utf-8
import psycopg2
import math
import matplotlib as plt

host_name = 'localhost'
port = '5432'
user_name = 'postgres'
pwd = '12345678'
db_name = 'Finding_Parking_Space'

my_connection = psycopg2.connect(host = host_name, port = port, user = user_name, password = pwd, dbname = db_name)
my_connection.autocommit = True
cur = my_connection.cursor()

class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''
    COUNT = 0

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
    def __init__(self, start_point, end_point, length):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length

class Road(LineString):
    def __init__(self, id, floor):
        self.id = id
        self.floor = floor
