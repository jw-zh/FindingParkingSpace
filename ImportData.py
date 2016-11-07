#coding=utf-8
#psycopg2 为连接 Postgres 必要的 module，需用到其中 psycopg2.connent() 函数
import psycopg2
#User information，根据具体情况进行修改
#host_name = '10.192.72.119'
host_name = 'localhost'
port = '5432'
user_name = 'postgres'
pwd = '12345678'
db_name = 'FindingParkingSpace'
#连接数据库
my_connection = psycopg2.connect(host = host_name, port = port, user = user_name, password = pwd, dbname = db_name)
my_connection.autocommit = True
cur = my_connection.cursor()
'''一个执行 query 并 print 出来的示例
cur.execute("select * from public.\"Floor\";")

for id, floor_num, geom, height in cur.fetchall():
    print id, floor_num, geom, height
'''
#读取 .csv 文件时用到的 module
import csv
#打开当前 directory 下的文件，'rb' mode: read in binary
csv_file = file('Road.csv','rb')
#reader 用来存储读进来的数据，一条记录为一行
reader = csv.reader(csv_file)
#对每一条数据进行 insert 操作
for line in reader:
    #SQL Script: INSERT DATA
    #分别对应于 Elevator, ParkingSpace, Road 表的 INSERT 语句
    #insert_str = 'INSERT INTO public.\"Elevator\" (\"ID\", \"Floor\", \"Geometry\") VALUES (' + line[0] + ',' + line[1] + ',POINT' + line[2] + ');'
    #insert_str = 'INSERT INTO public.\"ParkingSpace\"(\"ID\", \"Floor\", \"Geometry\", \"ParkingNumber\", \"District\", \"VehicleType\", \"PlateNumber\", \"IfOccupied\") VALUES (' + line[0] + ',' + line[1] + ',POINT' + line[2] + ',\'' + line[3] + '\', \'' + line[4] + '\', \'' + line[5] + '\', \'' + line[6] + '\', ' + line[7] + ');'
    #insert_str = 'INSERT INTO public.\"Road\" (\"ID\", \"Floor\", \"Geometry\") VALUES (' + line[0] + ',' + line[1] + ',\'(' + line[2] + ')\');'
    insert_str = 'INSERT INTO public.\"Road\"(\"ID\", \"Floor\", geometry) VALUES (' + line[0] + ',' + line[1] + ',ST_GeomFromText(\'LINESTRING' + line[2] + '\',4326));'
    #用于测试 INSERT Script 是否正确
    #print insert_str
    #---------------------------------------------------------------------------
    #Commit & Execute 上面的 Script
    try:
        cur.execute(insert_str)
    #如果出现错误（如 Syntax Error），则在console中 print -> Failed
    except:
        print "Failed"

#关闭已打开的 .csv 文件
csv_file.close()
