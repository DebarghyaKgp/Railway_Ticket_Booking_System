import mysql.connector as mycon
import random
def body2(ucode):
    k=None
    while k!=4:
        print('''1. VIEW BOOKINGS
2. MANAGE BOOKINGS
3. NEW BOOKING
4. MAIN MENU''')
        k=int(input('Enter your choice: '))
        if k==1:
            cur.execute('select * from bookings where usercode='+str(ucode))
            result=cur.fetchall()
            print("%20s"%"USERCODE","%20s"%"TRAIN ID","%20s"%"NUMBER OF PASSENGERS","%20s"%"DATE OF JOURNEY","%20s"%"TIME OF JOURNEY","%20s"%"NAME OF TRAIN","%20s"%"SOURCE","%20s"%"DESTINATION")
            for row in result:
                print("%20s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%20s"%row[4],"%20s"%row[5],"%20s"%row[6],"%20s"%row[7])
        elif k==2:
            c=input('WARNING!! DO YOU REALLY WANT TO CANCEL BOOKING?[Y/N]: ')
            if c=='Y':
                cur.execute('select * from bookings where usercode="'+str(ucode)+'"')
                result=cur.fetchall()
                print("%20s"%"USERCODE","%20s"%"TRAIN ID","%20s"%"NUMBER OF PASSENGERS","%20s"%"DATE OF JOURNEY","%20s"%"TIME OF JOURNEY","%20s"%"NAME OF TRAIN","%20s"%"SOURCE","%20s"%"DESTINATION")
                for row in result:
                    print("%20s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%20s"%row[4],"%20s"%row[5],"%20s"%row[6],"%20s"%row[7])
                f=input('Enter the Train Id of the train you want to cancel')
                cur.execute('select count(*) from bookings where train_id="'+str(f)+'"')
                result=cur.fetchall()
                if str(result[0][0]==1):
                    cur.execute('delete from bookings where train_id="'+str(f)+'"')
                    con.commit()
                    print('BOOKINGS DELETED SUCCESSFULLY!! REFUND AMOUNT WILL BE SENT TO YOUR ACCOUNT SHORTLY!!')
                else:
                    print('NO TRAINS FOUND!!')
        elif k==3:
            print('/'*191)
            print('''WELCOME TO BOOKING TERMINAL
THE TRAINS AVAILABLE ARE AS FOLLOWS''')
            cur.execute('select * from trains')
            result=cur.fetchall()
            print("%10s"%"PNR","%20s"%"NAME","%20s"%"SOURCE","%20s"%"DESTINATION","%10s"%"SEATS","%10s"%"DEPARTURE","%10s"%"ARRIVAL","%40s"%"TIER","%40s"%"COST PER TICKET")
            print('/'*191)
            for row in result:
                print("%10s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%10s"%row[4],"%10s"%row[5],"%10s"%row[6],"%40s"%row[7],"%40s"%row[8])
                print('/'*191)
            pnr=int(input('ENTER PNR OF THE TRAIN YOU WANT TO BOOK: '))
            cur.execute('select count(*) from trains where pnr='+str(pnr))
            result=cur.fetchall()
            if str(result[0][0])=='0':
                print('NO TRAINS AVAILABLE')
            else:
                cur.execute('select * from trains where pnr='+str(pnr))
                r=cur.fetchall()
                tier=input('ENTER TIER NAME: ')
                if tier in r[0][7]:
                    print('Tier available!!')
                    date=input('Enter date of journey[YYYY-MM-DD]: ')
                    seats=int(input('Enter the number of seats you want to book: '))
                    if seats>r[0][4]:
                        print("Not enough seats")
                    else:
                        print('BOOKING DETAILS STORED!! PROCEEDING TO PAYMENT...')
                        print('AMOUNT DUE: ',r[0][8]*seats)
                        cardno=input('ENTER CARD NUMBER: ')
                        if len(cardno)==16:
                            cvv=input('ENTER CVV: ')
                            if len(cvv)==3:
                                print('/'*191)
                                print('PAYMENT SUCCESSFUL')
                                print('/'*191)
                                query="insert into bookings values({},{},{},'{}','{}','{}','{}','{}')".format(ucode,r[0][0],seats,date,r[0][5],r[0][1],r[0][2],r[0][3])
                                cur.execute(query)
                                remseats=r[0][4]-seats
                                cur.execute('update trains set seats='+str(remseats)+' where pnr='+str(pnr))
                                con.commit()
                            else:
                                print('Invalid cvv')
                            
                        else:
                            print('Invalid Card Number')
                else:
                    print('Tier unavailable!!Try some other time!!')
                
                
                
            
                
    


def body(un,pwd):
    k=None
    while k!=4:
        print('/'*191)
        print('''1. VIEW ACCOUNT
2. ALTER ACCOUNT DETAILS
3. MORE
4. LOGOUT''')
        k=int(input("Enter your choice: "))
        cur.execute('SELECT * FROM Account where username="'+un+'" and userpassword="'+pwd+'"')
        result=cur.fetchall()
        ucode=result[0][0]
        if k==1:
            cur.execute('SELECT * FROM Account where username="'+un+'" and userpassword="'+pwd+'"')
            result=cur.fetchall()
            print("%20s"%"USERCODE","%20s"%"USERPASSWORD","%20s"%"USERNAME")
            print('/'*191)
            for row in result:
                print("%20s"%row[0],"%20s"%row[1],"%20s"%row[2])
                print('/'*191)
        elif k==2:
            u=input('ENTER NEW USERNAME: ')
            p=input('ENTER NEW PASSWORD: ')
            cur.execute('update account set username="'+u+'", userpassword="'+p+'" where usercode="'+str(ucode)+'"')
            con.commit()
            un=u
            pwd=p
            print('USERNAME PASSWORD CHANGED SUCCESSFULLY!!')
        elif k==3:
            body2(ucode)
        elif k==4:
            print('LOGGED OUT SUCCESSFULLY!!')
            break
        else:
            print('INVALID INPUT. TRY AGAIN')


            

def initiate(n):
    print('/'*191)
    cur.execute("use Anand_Railway_Services")
    print('WECOLME TO ANAND RAILWAY SERVICES')
    print('/'*191)
    while n!=3:
        print('''1. LOGIN
2. SIGNUP
3. EXIT''')
        n=int(input("Enter choice: "))
        if n==1:
            print("PLEASE ENTER USERNAME")
            un=input()
            print("ENTER PASSWORD")
            pwd=input()
            cur.execute('select count(*) from account where username="'+un+'" and userpassword="'+pwd+'"')
            result=cur.fetchall()
            if str(result[0][0])=='1':
                print('/'*191)
                print("ACCEPTED!!")
                body(un,pwd)
            else:
                print("INVALID USER ID/PASSWORD, TRY SINGUP!!\n \n")
        elif n==2:
            print("PLEASE ENTER USERNAME")
            un=input()
            print("ENTER PASSWORD")
            pwd=input()
            cur.execute('select count(*) from account where username="'+un+'" and userpassword="'+pwd+'"')
            result=cur.fetchall()
            if result[0][0]==0:
                print("CONFIRM PASSWORD")
                pwd2=input()
                if pwd==pwd2:
                    cur.execute('select max(usercode) from account')
                    r1=cur.fetchall()
                    r2=r1[0][0]+random.randint(1,1000)
                    q='insert into account values({},"{}","{}")'.format(r2,pwd,un)
                    cur.execute(q)
                    con.commit()
                    print('/'*191)
                    print('ACCOUNT CREATED SUCCESSFULLY!!')
                    print('/'*191)
                else:
                    print('PASSWORDS DO NOT MATCH')
            else:
                print('DUPLICATE ACCOUNT FOUND. TRY ANOTHER USERNAME/PASSWORD!!')
        elif n==3:
            print('/'*191)
            print('THANK YOU!!')
            print('/'*191)
            break
        else:
            print('INVALID INPUT. TRY AGAIN.')
    
con = mycon.connect(host='localhost', user='root', password = 'abc123')
cur = con.cursor()
initiate(None)
    
