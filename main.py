import mysql.connector as sq
conn=sq.connect(host='localhost', user='root', database='asa_jobs', passwd='tiger12@', charset='utf8')
cursor=conn.cursor()
import modules as md

md.dbntbcr()
ans="y" 
while (ans=="y" or ans=="Y"):
    
    print("\t\tWhat Would You Like To Do---")
    print('1. REGISTRATION')
    print('2. LOGIN')
    print('3. ENTER JOB')
    print()
    choice=int(input('Enter your choice- '))
    print('~-+'*20)

    if (choice==1):
        print("\t\tREGISTRATION")
        print('Register as: \n1.Job Seeker or \n2.Employer')
        print()
        cho=int(input('Enter Your Choice- '))
        print()
        if (cho==1):
            md.seereg()
        elif (cho==2):
            md.empreg()
        else:
            print('Invalid Input')
        print('~-+'*20)

    if (choice==2):
        md.seelog()
        print('~-+'*20)

    if (choice==3):
        md.jobentry()
        print('~-+'*20)
        
    ans=input("Do you want to return to home page(y/n): ")
    print('~-+'*20)
if (ans=="n" or ans=="N"):
    print("Thanks for visiting and using ASA JOBS SEARCH.....\nWe hope to see you again....")
    print()
    
