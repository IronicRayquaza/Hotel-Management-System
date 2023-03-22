import datetime 

import time 

importmysql.connector as ms 

 

mydb=ms.connect(host='localhost',user='root',password='',database='rooms') 

cur  =mydb.cursor() 

#sql command for gathering 'rooms' table data 

cur.execute('select Room_no,type,cost,status,description\ 

from room where status="Available";') 

lst=[] 

for x in cur: 

lst.append(x) 

 

 

def booking():                  #booking function 

globallst                    #declaring global variable 

check_in=str(input("Enter date for check in (dd/mm/yyyy)  : ")) 

check_out=str(input("Enter date for check out (dd/mm/yyyy)  : ")) 

ddi=int(check_in[0:2]) 

ifcheck_in[3]==0: 

mmi=int(check_in[4:6]) 

else: 

mmi=int(check_in[3:5]) 

yyi=int(check_in[6:]) 

ddo=int(check_out[0:2]) 

ifcheck_out[3]==0: 

mmo=int(check_out[4:6]) 

else: 

mmo=int(check_out[3:5]) 

yyo=int(check_out[6:]) 

 

    #using datetime module to get proper date 

cin=datetime.date(yyi,mmi,ddi) 

cout=datetime.date(yyo,mmo,ddo) 

 

booking.m=str(yyi)+'-'+str(mmi)+'-'+str(ddi) 

booking.n=str(yyo)+'-'+str(mmo)+'-'+str(ddo) 

 

days=(cout-cin).days                #counting days 

 

print('Searching for Available Rooms......') 

time.sleep(3) 

print() 

print("Available Rooms :") 

print('_'*100) 

print('Room no \t Type \t\t Cost \t\t Status \t\t\t Description') 

print('_'*100) 

fori in lst: 

ifi[1]=='Deluxe': 

            print(i[0],'\t\t',i[1],'\t\t',i[2],'\t\t',i[3],'\t\t',i[4]) 

else: 

            print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t\t',i[4]) 

print() 

print('NOTE* The Cost is for Per Persons Per Night') 

print() 

opt=int(input("""Bottom bar - 

1. Apply Filters                        2. Select From Above 

Choose Here :""")) 

if opt==1: 

print() 

room_type=int(input("""Select Room Type : 

1. Standard             2. Deluxe             3. Premium 

-->""")) 

ifroom_type==1:                            #standard room type 

cur.execute('select room_no,type,cost,status,description from room where type="standard" and status="available"') 

            temp1=[] 

for z in cur: 

temp1.append(z) 

            tmp1=lst 

print('_'*100) 

print('Room no \t Type \t\t Cost \t Status \t\t Description') 

print('_'*100) 

for j in temp1: 

                print(j[0],'\t\t',j[1],'\t',j[2],'\t',j[3],'\t',j[4]) 

print() 

choose=int(input("Enter the Room no. of the room you would like to book ;")) 

for c in temp1: 

if c[0]==choose: 

cost=c[2] 

 

cur.execute("update room set status='Booked' where Room_No={};".format(choose)) 

mydb.commit() 

            booking.ch=choose 

 

print("Proceeding....") 

time.sleep(1) 

print("Enter your details here :") 

adult=int(input("Enter number of adults :")) 

child=int(input("Enter number of children :")) 

roo=int(input("Enter number of rooms :")) 

print("Calculating Total Charges .......") 

time.sleep(2) 

            r=0 

ifroo>1: 

                r=(50/100)*cost*roo 

else: 

                r=0 

total=(cost*adult*days)+((25/100)*cost*child*days) + r 

print("Your Room is Booked") 

 

print("The total charge is :", total) 

print('*****************************************************') 

print("""You Will Be Required to Submi the Further Details At The Hotel 

                     Under The Unique Customer Id Provided""") 

print("Hoping For Your Safe and Comfortable Stay") 

print('*****************************************************') 

print('Thanks For Your Visit') 

 

if room_type==2:                            #deluxe type room 

cur.execute("select room_no,type,cost,status,description from room where type='deluxe' and status='available'") 

            temp1=[] 

for z in cur: 

temp1.append(z) 

            tmp1=lst 

print('_'*100) 

print('Room no \t Type \t Cost \t Status \t\t Description') 

print('_'*100) 

for j in temp1: 

                print(j[0],'\t\t',j[1],'\t',j[2],'\t',j[3],'\t',j[4]) 

print() 

choose=int(input("Enter the Room no. of the room you would like to book ;")) 

for c in temp1: 

if c[0]==choose: 

cost=c[2] 

cur.execute("update room set status='Booked' where Room_No={};".format(choose)) 

mydb.commit() 

            booking.ch=choose 

 

print("Proceeding....") 

time.sleep(1) 

print("Enter your details here :") 

adult=int(input("Enter number of adults :")) 

child=int(input("Enter number of children :")) 

roo=int(input("Enter number of rooms :")) 

print("Calculating Total Charges .......") 

time.sleep(2) 

            r=0 

ifroo>1: 

                r=(50/100)*cost*roo 

else: 

                r=0 

total=(cost*adult*days)+((25/100)*cost*child*days) + r 

print("Room is Booked") 

 

print("The total charge is :", total) 

print('*****************************************************') 

print("""You Will Be Required to Submi the Further Details At The Hotel 

                    Under The Unique Customer Id Provided""") 

print("Hoping For Your Safe and Comfortable Stay") 

print('*****************************************************') 

print('Thanks For Your Visit') 

 

ifroom_type==3:                                #premium type room 

cur.execute('select room_no,type,cost,status,description from room where status="Available" and type="Premium"') 

            temp1=[] 

for z in cur: 

temp1.append(z) 

            tmp1=lst 

print('_'*100) 

print('Room no \t Type \t\t Cost \t Status \t\t Description') 

print('_'*100) 

for j in temp1: 

                print(j[0],'\t\t',j[1],'\t',j[2],'\t',j[3],'\t',j[4]) 

print() 

choose=int(input("Enter the Room no. of the room you would like to book ;")) 

for c in temp1: 

if c[0]==choose: 

cost=c[2] 

 

cur.execute("update room set status='Booked' where Room_No={};".format(choose)) 

mydb.commit() 

            booking.ch=choose 

 

print("Proceeding....") 

time.sleep(1) 

print("Enter your details here :") 

adult=int(input("Enter number of adults :")) 

child=int(input("Enter number of children :")) 

roo=int(input("Enter number of rooms :")) 

print("Calculating Total Charges .......") 

time.sleep(2) 

            r=0 

ifroo>1: 

                r=(50/100)*cost*roo 

else: 

                r=0 

total=(cost*adult*days)+((25/100)*cost*child*days) + r 

print("Room is Booked") 

 

print("The total charge is :", total) 

print('*****************************************************') 

print("""You Will Be Required to Submi the Further Details At The Hotel 

                    Under The Unique Customer Id Provided""") 

print("Hoping For Your Safe and Comfortable Stay") 

print('*****************************************************') 

print('Thanks For Your Visit') 

 

if opt==2: 

choose=int(input("Enter the Room no. of the room you would like to book ;")) 

for c in lst: 

if c[0]==choose: 

cost=c[2] 

 

cur.execute("update room set status='Booked' where Room_No={};".format(choose)) 

mydb.commit() 

        booking.ch=choose 

 

print("Proceeding....") 

time.sleep(1) 

print("Enter your details here :") 

adult=int(input("Enter number of adults :")) 

child=int(input("Enter number of children :")) 

roo=int(input("Enter number of rooms :")) 

print() 

print("Calculating Total Charges .......") 

time.sleep(2) 

        r=0 

ifroo>1: 

            r=(50/100)*cost*(roo-1) 

else: 

            r=0 

total=(cost*adult*days)+((25/100)*cost*child*days) + r 

print("Room is Booked") 

print("The total charge is :", total) 

 

print('*****************************************************') 

print("""You Will Be Required to Submit the Further Details At The Hotel 

                Under The Unique Customer Id Provided""") 

print("         Hoping For Your Safe and Comfortable Stay") 

print('*****************************************************') 
