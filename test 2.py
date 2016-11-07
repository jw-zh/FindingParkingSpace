import psycopg2
import matplotlib.pyplot as plt
'''
host_name = 'localhost'
port = '5432'
user_name = 'postgres'
pwd = '123456'
db_name = 'Finding_Parking_Space'
#?????
my_connection = psycopg2.connect(host = host_name, port = port, user = user_name, password = pwd, dbname = db_name)
my_connection.autocommit = True
cur = my_connection.cursor()
cur.execute("select ST_X(ST_StartPoint(geometry)), ST_Y(ST_StartPoint(geometry)), ST_X(ST_EndPoint(geometry)), ST_Y(ST_EndPoint(geometry)) from public.\"Road\";")

road_web = {}
for x1, y1, x2, y2 in cur.fetchall():
    #print x1, y1, x2, y2
    #plt.scatter(x1, y1)
    #plt.scatter(x2, y2)
    plt.plot([x1, x2], [y1, y2])

plt.show()
'''
distances = {
    'B': {'A':5, 'C':3},
    'C': {'B':3, 'D':4, 'E':3, 'F':2},
    'D': {'C':4, 'G':1},
    'E': {'C':3},
    'F': {'C':2, 'G':2},
    'G': {'F':2, 'D':1}
    }
str_a = 'A'
str_b = 'B'
val = 5
dict = {}
dict[str_b] = val
distances[str_a] = dict
print distances