import mysql.connector as sq
conn=sq.connect(host='localhost', user='root', database='asa_jobs', passwd='tiger12@', charset='utf8')
cursor=conn.cursor()


def dbntbcr():
    cursor.execute("SHOW DATABASES")
    databases=cursor.fetchall()
    #droping database if exists
    if ('asa_jobs',) in databases:
        query1="DROP DATABASE asa_jobs "
        cursor.execute(query1)
        conn.commit()

    #creating database
    query2="CREATE DATABASE asa_jobs"
    cursor.execute(query2)
    conn.commit()

    #using database
    query3="USE asa_jobs"
    cursor.execute(query3)

    #creating table JOBSEEKERS
    query4="CREATE TABLE JOBSEEKERS(fname varchar(15) not null, lname varchar(15), emid varchar(50) not null unique, mobno varchar(12) unique,city varchar(20) not null, state varchar(15) not null, pincode int not null, userid varchar(25) not null primary key, passw varchar(25) not null)"
    cursor.execute(query4)
    conn.commit()

    #creating table EMPLOYER
    query5="CREATE TABLE EMPLOYER(company_name varchar(50) not null, emid varchar(50) not null, compsize int, ceo varchar(25) not null, comp_addre varchar(100) not null, teleno varchar(12), coid varchar(20) not null primary key, passw varchar(30) not null)"
    cursor.execute(query5)
    conn.commit()

    #creating table JOBDESC
    query6="create table JOBDESC (coid varchar(20), job varchar(20), salary varchar(7), expmon varchar(3), expyr varchar(3), quali varchar(20), woco enum('Part Time','Full Time'), location varchar(15), foreign key(coid) references EMPLOYER(coid))"                  
    cursor.execute(query6)
    conn.commit()

    #entering dummy records
    fname='Atharva'
    lname='Tarate'
    emid='atharvatarate@gmail.com'
    mobno='9657202085'
    city='Pune'
    state='Mahrashtra'
    pincode='411001'
    userid='atta'
    passw='atta123'
    q5="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q5)
    conn.commit()
    ###################
    fname='Aditya'
    lname='Lawand'
    emid='adityalawand@gmail.com'
    mobno='9234561788'
    city='Satara'
    state='Mahrashtra'
    pincode='442231'
    userid='adila'
    passw='awmjedf'
    q6="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q6)
    conn.commit()
    ##################
    fname='Aanchal'
    lname='Yadav'
    emid='aanchalyadav@gmail.com'
    mobno='9657292087'
    city='Agra'
    state='UP'
    pincode='422023'
    userid='aaya'
    passw='jysegfhud'
    q7="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q7)
    conn.commit()
    ##################
    fname='Sanket'
    lname='Latambale'
    emid='sanlat2323@gmail.com' 
    mobno='9665368085'
    city='Ahmednagar'
    state='Mahrashtra'
    pincode='414001'
    userid='sanlat'
    passw='vasusa'
    q8="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q8)
    conn.commit()
    ##################
    fname='Sneha'
    lname='Basu'
    emid='didiforpm@gmail.com'
    mobno='8227202085'
    city='Kolkata'
    state='West Bengal'
    pincode='700001' 
    userid='seba'
    passw='phule'
    q9="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q9)
    conn.commit()
    ###################
    fname='Sahil'
    lname='Terse'
    emid='sahilterse@gmail.com'
    mobno='8774763544'
    city='Ratnagiri'
    state='Mahrashtra'
    pincode='415612'
    userid='sahte'
    passw='egouhrg'
    q10="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q10)
    conn.commit()
    ###################
    fname='Sayyed'
    lname='Faiz'
    emid='chicha@gmail.com'
    mobno='9655552085'
    city='Pune'
    state='Mahrashtra'
    pincode='411023'
    userid='faiz'
    passw='hrjddhjth'
    q11="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q11)
    conn.commit()
    ##################
    fname='Shivam'
    lname='Phasale'
    emid='shivamphasale@gmail.com'
    mobno='9222222085'
    city='Aurangabad'
    state='Mahrashtra'
    pincode='400023'
    userid='shiph'
    passw='jgcdjjfj'
    q12="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q12)
    conn.commit()
    ###################
    fname='Aryan'
    lname='Sarkar'
    emid='mishtydohi@gmail.com'
    mobno='8737202085'
    city='Kolkata'
    state='West Bengal'
    pincode='700003'
    userid='Sarkar'
    passw='nhklufitd'
    q13="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q13)
    conn.commit()
    ##################
    fname='Aditya'
    lname='Patel'
    emid='adityapatel@gmail.com'
    mobno='9633332085'
    city='Panchmarhi'
    state='MP'
    pincode='461881'
    userid='adipa'
    passw='bbljjghvtik'
    q14="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q14)
    conn.commit()
    #################
    coname='Mysoft Inc.'
    emid='mysoft@gmail.com'
    cosize=150
    ceo='Sanjay Murgan'
    coadd='Plot No.33, Mysoft Industries, Palgar(W), Maharashtra, India'
    telno='02023476543'
    coid='mysoft'
    passw='mysoft11'
    qq1="insert into EMPLOYER values('{}','{}',{},'{}','{}','{}','{}','{}')".format(coname,emid,cosize,ceo,coadd,telno,coid,passw)
    cursor.execute(qq1)
    conn.commit()
    ################
    coname='Spanx'
    emid='spanx@gmail.com'
    cosize=50
    ceo='Deepak Yevale'
    coadd='Plot No.45, Spanx Industrial Zone, Andheri(W), Maharashtra, India'
    telno='02023576543'
    coid='spanx'
    passw='spanx13'
    qq2="insert into EMPLOYER values('{}','{}',{},'{}','{}','{}','{}','{}')".format(coname,emid,cosize,ceo,coadd,telno,coid,passw)
    cursor.execute(qq2)
    conn.commit()
    ################
    coname='Chakki Garments'
    emid='chakkigar@gmail.com'
    cosize=100
    ceo='Sandeep Chakka'
    coadd='Plot No.12, Chakki Garments Ltd., Kolkata(E), West Bengal, India'
    telno='02023578743'
    coid='ckga'
    passw='ckga66'
    qq3="insert into EMPLOYER values('{}','{}',{},'{}','{}','{}','{}','{}')".format(coname,emid,cosize,ceo,coadd,telno,coid,passw)
    cursor.execute(qq3)
    conn.commit()

    ###############
    #entering dummy records for JOBDESC
    ###############
    coid="ckga"
    job="Salesman"
    salary="25000"
    expmon="5"
    expyr="5"
    quali="BCom(Sales)"
    woco="Part Time"
    location="Pune"
    qqq1="insert into JOBDESC values('{}','{}','{}','{}','{}','{}','{}','{}')".format(coid,job,salary,expmon,expyr,quali,woco,location)
    cursor.execute(qqq1)
    conn.commit()
    ################
    coid="mysoft"
    job="Executive Manager"
    salary="70000"
    expmon="0"
    expyr="5"
    quali="MBA(Managemenrt)"
    woco="Full Time"
    location="Chennai"
    qqq2="insert into JOBDESC values('{}','{}','{}','{}','{}','{}','{}','{}')".format(coid,job,salary,expmon,expyr,quali,woco,location)
    cursor.execute(qqq2)
    conn.commit()
    ################
    coid="spanx"
    job="IT Manager"
    salary="50000"
    expmon="3"
    expyr="4"
    quali="BTech(CS)"
    woco="Full Time"
    location="Hyderabad"
    qqq3="insert into JOBDESC values('{}','{}','{}','{}','{}','{}','{}','{}')".format(coid,job,salary,expmon,expyr,quali,woco,location)
    cursor.execute(qqq3)
    conn.commit()
    ################
    coid="ckga"
    job="Sales Manager"
    salary="65000"
    expmon="0" 
    expyr="2"
    quali="MCom(Sales)"
    woco="Full Time"
    location="Pune"
    qqq4="insert into JOBDESC values('{}','{}','{}','{}','{}','{}','{}','{}')".format(coid,job,salary,expmon,expyr,quali,woco,location)
    cursor.execute(qqq4)
    conn.commit()
    ################
    coid="spanx"
    job="HR Manager"
    salary="40000"
    expmon="3"
    expyr="4"
    quali="MBA(Management)"
    woco="Full Time"
    location="Hyderabad"
    qqq5="insert into JOBDESC values('{}','{}','{}','{}','{}','{}','{}','{}')".format(coid,job,salary,expmon,expyr,quali,woco,location)
    cursor.execute(qqq5)
    conn.commit()
    ################


def seereg():
    fname=input("First Name - ")
    lname=input("Last Name - ")
    emid=str(input("Email ID - "))
    mobno=int(input("Mobile no. - "))
    print("Location: ")
    city=input("City- ")
    state=input("State- ")
    pincode=int(input("Pincode- "))
    userid=input("User ID - ")
    passw=input("Password- ")
    cpasswd=input("Confirm password- ")
    while passw!=cpasswd:
        print('Not Matching')
        print("Re-enter Password")
        passw=input("Password- ")
        cpasswd=input("Confirm password- ")


    q1="insert into JOBSEEKERS values('{}', '{}', '{}', {}, '{}', '{}', {}, '{}', '{}')".format(fname,lname,emid,mobno,city,state,pincode,userid,passw)
    cursor.execute(q1)
    conn.commit()

def empreg():
    coname=input('Enter your company name- ')
    emid=input('Enter company email id- ')
    cosize=int(input('Enter number of employees- '))
    ceo=input('Enter CEO name- ')
    coadd=input('Enter company address- ')
    telno=input('Enter company telephone number- ')
    coid=input('Enter company ID- ')
    passw=input('Enter password- ')
    cpassw=input('Confirm password- ')
    while passw!=cpassw:
        print('Not Matching')
        print("Re-enter Password")
        passw=input("Password- ")
        cpassw=input("Confirm password- ")
    qq1="insert into EMPLOYER values('{}','{}',{},'{}','{}','{}','{}','{}')".format(coname,emid,cosize,ceo,coadd,telno,coid,passw)
    cursor.execute(qq1)
    conn.commit()

def seelog():
    useridc=input('Enter your username- ')
    q1="select * from JOBSEEKERS where userid='{}'".format(useridc)
    cursor.execute(q1)
    data=cursor.fetchone()

    #checking whether this userid is present in our database
    #if it is present then we will ask for password
    #else -"INVALID USER"
    if (data!= None):
        passwd=input( 'Enter your password- ')
    #checking if the password is correct or not
        if (passwd in data):
            q="select fname from JOBSEEKERS where userid='{}'".format(useridc)
            cursor.execute(q)
            na=cursor.fetchone()
            nas=na[0]
            print('LOGIN SUCCESSFUL......Welcome',nas)
            print()
            print("What would you like to do: ")
            print("1.Update Profile \n2.Search a Job")
            print()
            selocho=int(input("Enter your choice: "))
            print()
            if (selocho==1):
                print("What do you want to update ?")
                print("1.First Name \n2.Last Name \n3.Email id \n4.Mobile No. \n5.Address")
                print()
                fi=int(input("Enter Your Choice: "))
                print()
                if (fi==1):
                    ufn=input("Enter First Name: ")
                    qc="update JOBSEEKERS set fname='{}' where userid='{}'".format(ufn,useridc)
                    cursor.execute(qc)
                    conn.commit()
        
                if (fi==2):
                    uln=input("Enter Last Name: ")
                    qc="update JOBSEEKERS set lname='{}' where userid='{}'".format(uln,useridc)
                    cursor.execute(qc)
                    conn.commit()

                if (fi==3):
                    uem=input("Enter Email id: ")
                    qc="update JOBSEEKERS set emid='{}' where userid='{}'".format(uem,useridc)
                    cursor.execute(qc)
                    conn.commit()

                if (fi==4):
                    umn=input("Enter Mobile No: ")
                    qc="update JOBSEEKERS set mobno='{}' where userid='{}'".format(umn,useridc)
                    cursor.execute(qc)
                    conn.commit()

                if (fi==5):
                    uc=input("Enter City: ")
                    us=input("Enter State: ")
                    up=int(input("Enter Pincode: "))
                    qc1="update JOBSEEKERS set city='{}' where userid='{}'".format(uc,useridc)
                    cursor.execute(qc1)
                    conn.commit()
                    qc2="update JOBSEEKERS set state='{}' where userid='{}'".format(us,useridc)
                    cursor.execute(qc2)
                    conn.commit()
                    qc3="update JOBSEEKERS set pincode='{}' where userid='{}'".format(up,useridc)
                    cursor.execute(qc3)
                    conn.commit()
            elif (selocho==2):
                ty=input('Enter job you want: ')
                loc=input('Enter job location you want: ')
                print('-'*10) 
                qqqq1="select e.coid, company_name, emid, job, salary, location from EMPLOYER e, JOBDESC j where(e.coid=j.coid and location='{}'and job='{}')".format(loc,ty)
                cursor.execute(qqqq1)
                data=cursor.fetchall()
                if (data==[]):
                    print('Sorry. No Job Available')
                else:
                    for i in data:
                        print('Company Name: ',i[1])
                        print('Email: ',i[2])
                        print('Job: ',i[3])
                        print('Salary: ',i[4])
                        print('Location: ',i[5])
                        print('-'*10)
                
            
        else :
            print('INCORRECT PASSWORD')
    else:
        print('INVALID USERNAME')

def jobentry():
    coid=input('Enter compamy id- ')

    qqc="select * from EMPLOYER where coid='{}'".format(coid)
    cursor.execute(qqc)
    data=cursor.fetchone()

    if (data!=None):
        passwd=input( 'Enter your password- ')
        if (passwd in data):
            q="select company_name from EMPLOYER where coid='{}'".format(coid)
            cursor.execute(q)
            na=cursor.fetchone()
            nas=na[0]
            print('LOGIN SUCCESSFUL')
            print('WELCOME',nas)
            job=input('Enter Job Name- ')
            salary=input('Enter Approx. Salary- ')
            print('Experience Details')
            expmon=input('Enter No. of months- ')
            expyr=input('Enter No. of years- ')
            quali=input('Enter Min. Qualification Expected- ')
            woco=input('Full Time or Part Time- ')
            location=input('Enter job location- ')

            qqq1="insert into JOBDESC values('{}','{}','{}','{}','{}','{}','{}','{}')".format(coid,job,salary,expmon,expyr,quali,woco,location)
            cursor.execute(qqq1)
            conn.commit()
        else :
            print('INCORRECT PASSWORD')
    else:
        print('INVALID USERNAME')

def jobser():
    ty=input('Enter job you want: ')
    loc=input('Enter job location you want: ')
    print('-'*10) 
    qqqq1="select e.coid, company_name, emid, job, salary, location from EMPLOYER e, JOBDESC j where(e.coid=j.coid and location='{}'and job='{}')".format(loc,ty)
    cursor.execute(qqqq1)
    data=cursor.fetchall()
    if (data==[]):
        print('Sorry. No Job Available')
    else:
        for i in data:
            print('Company Name: ',i[1])
            print('Email: ',i[2])
            print('Job: ',i[3])
            print('Salary: ',i[4])
            print('Location: ',i[5])
            print('-'*10)
    
