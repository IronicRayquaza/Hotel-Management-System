import booking 

import rooms 

import customer 

import mysql.connector as ms 

 

mydb=ms.connect(host='localhost',user='root',password='') 

cur=mydb.cursor() 

 

print('\ \ \ \ \ \ \ \  ---    WELCOME TO AZURE HOTEL    --- / / / / / / / /') 

print() 

print('_'*60) 

action=int(input(""" 

(**1**)-- Access To Booking Site                   (**2**)-- Staff Members Only 

 

Choose Your Option -- :""")) 

 

if action==1: 

    booking.booking() 

    cur.execute("use rooms;") 

    p=booking.booking.m 

    q=booking.booking.n 

 

    cur.execute("insert into booked_rooms(Room_Id, Room_No, Type, Cost, Status) select Room_Id, Room_No, Type, Cost, Status from room where Room_No={};".format(booking.booking.ch)) 

    cur.execute("update booked_rooms set Check_In='{}' where room_no={};".format(p,booking.booking.ch)) 

    cur.execute("update booked_rooms set Check_Out='{}' where room_no={};".format(q,booking.booking.ch)) 

    mydb.commit() 

 

if action==2: 

    print("ACCESS TO STAFF SITE GRANTED") 

    ans='y' 

    while ans=='y': 

        print() 

        print("-------------------------------------------") 

        print() 

        act=int(input(""" DATABASE MANAGING 

1) Manage The Database Of Rooms 

2) Manage The Database Of Customers 

----- :""")) 

        print() 

        if act==1: 

            rooms.room_managing() 

 

        if act==2: 

            customer.customer() 

        print() 

        print() 

        ans=str(input("Type 'y' To Go Back To Database Managing")) 

        print() 

print() 

print('_'*60) 

print("/ / / / / *** THANKS FOR VISITING *** \ \ \ \ \ ") 

print('_'*60) 
