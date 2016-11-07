#coding=utf-8
import psycopg2
import math
import matplotlib as plt
from MyClass import *

host_name = 'localhost'
port = '5432'
user_name = 'postgres'
pwd = '12345678'
db_name = 'Finding_Parking_Space'

my_connection = psycopg2.connect(host = host_name, port = port, user = user_name, password = pwd, dbname = db_name)
my_connection.autocommit = True
cur = my_connection.cursor()
cur.execute("select \"ID\", \"Floor\", ST_X(ST_StartPoint(geometry)), ST_Y(ST_StartPoint(geometry)), ST_X(ST_EndPoint(geometry)), ST_Y(ST_EndPoint(geometry)) from public.\"Road\";")

seg_list = []
for id, floor, x1, y1, x2, y2 in cur.fetchall():
    road = Road(id, floor, Point(x1, y1), Point(x2, y2))
    seg_list.append(road)
    road.DrawLine()
plt.show()