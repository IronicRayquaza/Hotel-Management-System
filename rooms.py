importmysql.connector as ms 

mydb=ms.connect(host="localhost",user="root",passwd='',database='rooms') 

cur=mydb.cursor() 

 

cur.execute('select* from room;') 

lst=[] 

for x in cur: 

lst.append(x) 

 

defroom_managing(): 

globallst 

print() 

option=int(input("""Choose From The Given Options --: 

1) Database Of All Rooms 

2) Database Of Rooms That Are Booked 

3) Modify Booked Rooms Database 

4) Modify Rooms Database 

------ :""")) 

print() 

if option==1: 

print('_'*120) 

print('Room Id \t\t Room No \t Type \t\t Cost \t\t Status \t\t\t Description') 

print('_'*120) 

fori in lst: 

ifi[2]=='Deluxe': 

                print(i[0],'\t\t',i[1],'\t\t',i[2],'\t\t',i[3],'\t\t',i[4],'\t\t','\t',i[5]) 

else: 

                print(i[0],'\t\t',i[1],'\t\t',i[2],'\t',i[3],'\t\t',i[4],'\t\t','\t',i[5]) 

if option==2: 

cur.execute("select* from booked_rooms;") 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*120) 

print('Room Id \t Room No \t Type \t\t Cost \t\t Status \t\t Check In Date \t\t Check Out Date \t Checked Out') 

print('_'*120) 

for j in temp: 

            print(j[0],'\t\t',j[1],'\t',j[2],'\t',j[3],'\t',j[4],'\t',j[5],'\t',j[6],'\t',j[7]) 

 

elif option==3: 

ans='y' 

while ans=='y': 

opt=int(input("""Choose An Option --: 

1) Update Checked Out Column 

----- :""")) 

ser=int(input("Enter Room ID For The Room To Update -- :")) 

cout=str(input("Has The Person Checked Out ? (y/n) :")) 

ifcout.upper()=='Y': 

cur.execute("update booked_rooms set Checked_Out='{}' where Room_Id={};".format(cout,ser)) 

mydb.commit() 

print("Record Updated") 

ans=str(input("Want To Update Another Record ? (y/n) --- :")) 

print() 

 

elif option==4: 

ans='y' 

while ans=='y': 

opt=int(input("""Choose An Option --: 

1) Update Cost Of Room 

---- :""")) 

ser=int(input("Enter Room ID For The Room To Update -- :")) 

newcost=int(input("Enter New Cost For The Room :")) 

cur.execute("update room set cost={} where Room_Id={};".format(newcost,ser)) 

mydb.commit() 

print("Record Updated") 

ans=str(input("Want To Update Another Record ? (y/n) --- :")) 

print() 
