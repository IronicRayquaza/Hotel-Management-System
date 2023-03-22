importmysql.connector as ms 

mydb=ms.connect(host="localhost",user="root",passwd='',database='customer_data') 

cur=mydb.cursor() 

 

defcustomer_add(): 

ans='y' 

while ans=='y': 

no=int(input("Number of Customers :")) 

fori in range(0,no): 

customer_id=int(input("Enter The Customer ID :")) 

first_name=str(input("Enter The First Name :")) 

last_name=str(input("Enter The Last Name :")) 

gender=str(input("Enter Gender :")) 

age=int(input("Enter Age :")) 

contact=int(input("Enter Contact Number :")) 

email=str(input("Enter Email address :")) 

address=str(input("Enter Address :")) 

state=str(input("Enter State :")) 

city=str(input("Enter City :")) 

pincode=int(input("Enter Pincode :")) 

cur.execute("""insert into customer(Customer_Id, First_Name, Last_Name, Gender, age, Contact_No, Email, Address, State, City, Pincode) 

            values({},'{}','{}','{}',{},{},'{}','{}','{}','{}',{});""".format(customer_id, first_name, last_name, gender,age, contact,email,address,state,city,pincode)) 

mydb.commit() 

ans=str(input("Add More Customer Details (y/n) :")) 

 

 

cur.execute('select* from customer;') 

lst=[] 

for x in cur: 

lst.append(x) 

 

def customer(): 

globallst 

option=int(input("""Customers' Data Managing 

Choose What You Want To Do 

1) Sort Record 

2) Add Record 

3) Search For Record 

------ """)) 

if option==1: 

ans='y' 

while ans=='y': 

opt=int(input(""" 

1) Sort By Gender 

2) Sort By State 

3) Sort By City 

4) Sort By Age 

------- """)) 

 

if opt==1: 

gen=str(input("Enter Gender :")) 

cur.execute("select* from customer where gender='{}';".format(gen)) 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*170) 

print('Customer Id \t First Name \t Last Name \t Gender \t Age \t Contact \t\t\t Email \t\t\t Address \t\t\t State \t\t City \t Pincode') 

print('_'*170) 

fori in temp: 

                    print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8],'\t',i[9],'\t',i[10]) 

if opt ==2: 

sta=str(input("Enter State :")) 

cur.execute("select* from customer where state='{}';".format(sta)) 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*170) 

print('Customer Id \t First Name \t Last Name \t Gender \t Age \t Contact \t\t\t Email \t\t\t Address \t\t\t State \t\t City \t Pincode') 

print('_'*170) 

fori in temp: 

                    print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8],'\t',i[9],'\t',i[10]) 

if opt==3: 

cit=str(input("Enter City :")) 

cur.execute("select* from customer where city='{}';".format(cit)) 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*170) 

print('Customer Id \t First Name \t Last Name \t Gender \t Age \t Contact \t\t\t Email \t\t\t Address \t\t\t State \t\t City \t Pincode') 

print('_'*170) 

fori in temp: 

                    print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8],'\t',i[9],'\t',i[10]) 

if opt==4: 

ra=int(input("1) Sort By Age Range \t\t\t 2) Sort By Particular Age \n---- :")) 

ifra==1: 

mina=int(input("Minimum Age :")) 

maxa=int(input("Maximum Age :")) 

cur.execute("select* from customer where age>={} and age<={};".format(mina,maxa)) 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*170) 

print('Customer Id \t First Name \t Last Name \t Gender \t Age \t Contact \t\t\t Email \t\t\t Address \t\t\t State \t\t City \t Pincode') 

print('_'*170) 

fori in temp: 

                        print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8],'\t',i[9],'\t',i[10]) 

ifra==2: 

ag=int(input("Enter Age :")) 

cur.execute("select* from customer where age={};".format(ag)) 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*170) 

print('Customer Id \t First Name \t Last Name \t Gender \t Age \t Contact \t\t\t Email \t\t\t Address \t\t\t State \t\t City \t Pincode') 

print('_'*170) 

fori in temp: 

                        print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8],'\t',i[9],'\t',i[10]) 

ans=str(input("Want To Sort Again ? (y/n) --- :")) 

 

if option==2: 

customer_add() 

 

if option ==3: 

ans='y' 

while ans=='y': 

ser=int(input("1) Search By Name \t\t\t 2) Search By Contact Number \n3) Search By Customer Id\n---- :")) 

ifser==1: 

name=str(input("Enter Name :")) 

                p=name.split() 

fir=p[0] 

las=p[1] 

cur.execute("select* from customer where first_name='{}' and last_name='{}';".format(fir,las)) 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*170) 

print('Customer Id \t First Name \t Last Name \t Gender \t Age \t Contact \t\t\t Email \t\t\t Address \t\t\t State \t\t City \t Pincode') 

print('_'*170) 

for i in temp: 

                    print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8],'\t',i[9],'\t',i[10]) 

 

ifser==2: 

con=int(input("Enter Contact Number :")) 

cur.execute("select* from customer where contact_no={};".format(con)) 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*170) 

print('Customer Id \t First Name \t Last Name \t Gender \t Age \t Contact \t\t\t Email \t\t\t Address \t\t\t State \t\t City \t Pincode') 

print('_'*170) 

for i in temp: 

                    print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8],'\t',i[9],'\t',i[10]) 

ifser==3: 

cid=int(input("Enter Customer Id :")) 

cur.execute("select* from customer where customer_id={};".format(cid)) 

temp=[] 

for z in cur: 

temp.append(z) 

print('_'*170) 

print('Customer Id \t First Name \t Last Name \t Gender \t Age \t Contact \t\t\t Email \t\t\t Address \t\t\t State \t\t City \t Pincode') 

print('_'*170) 

fori in temp: 

                    print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7],'\t',i[8],'\t',i[9],'\t',i[10]) 

 

ans=str(input("Want To Search Again ? (y/n) -- :")) 

 
