import tabulate
import mysql.connector as sab
import random
import datetime
def get_super(x): 
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s)) 
    return x.translate(res)
phone_lst=[]
email_lst=[]

count=24
count2=0
count3=random.randint(1,6)
mydb=sab.connect(host="localhost",user="root",password="123456",port="3306")
cur=mydb.cursor()
cur.execute("create database if not exists icarus_aviation")
cur.execute("use icarus_aviation")
cur.execute("create table if not exists flight_status(flight_no varchar(5) primary key,from_place varchar(20),to_place varchar(20),price varchar(9),date varchar(20))")
today=datetime.datetime.today()
date5=today+datetime.timedelta(days=count3)
date_5=str(date5.strftime('%d/%m/%Y'))
def flight_sts(board,dest):
    today=datetime.datetime.today()
    date1=today+datetime.timedelta(days=3)
    date2=today+datetime.timedelta(days=2)
    date3=today+datetime.timedelta(days=1)
    date4=today+datetime.timedelta(days=4)
    date5=today+datetime.timedelta(days=count3)
    date_1=str(date1.strftime('%d/%m/%Y'))
    date_2=str(date2.strftime('%d/%m/%Y'))
    date_3=str(date3.strftime('%d/%m/%Y'))
    date_4=str(date4.strftime('%d/%m/%Y'))
    date_5=str(date5.strftime('%d/%m/%Y'))
    for i in range(1):
        cur.execute("delete from flight_status")
        mydb.commit()
        cur.execute("insert into flight_status values('12113','{}','{}','9400','{}')".format(board,dest,date_1))
        cur.execute("insert into flight_status values('15114','{}','{}','7800','{}')".format(board,dest,date_2))
        cur.execute("insert into flight_status values('15625','{}','{}','4600','{}')".format(board,dest,date_3))
        cur.execute("insert into flight_status values('13346','{}','{}','7300','{}')".format(board,dest,date_4))
        mydb.commit()
cur.execute("create table if not exists booked_flight(boarding varchar(30),destination varchar(30),date varchar(20),phone_num varchar(10), flight_no varchar(5), seats varchar(10))")
cur.execute("create table if not exists customer(username varchar(30), phone_num varchar(10), email varchar(30), password varchar(15), primary key(phone_num,email))")
def log_in():
    count=24
    count2=0
    phone_lst=[]
    cur.execute("select*from customer")
    res=cur.fetchall()
    for i in res:
        p=[i[1],i[3],i[0]]
        phone_lst.append(p)
    if len(phone_lst)==0:
        print("NO RECORD AVAILABLE TO SEARCH INTO")
        return()
    else:

        while True:
            print()
            usrnm=input("enter username ")
            
            while True:
                password=input("Enter password")
                print()
                if (len(password))>0:
                    break
                else:
                    print("PASSWORD LENGTH SHOULD BE GREATER THAN 0")
                    continue
            flag=0
            for i in phone_lst:
                if i[2]==usrnm and i[1]==password:
                    flag+=1
                    phone=i[0]
            if flag==1:
                print("LOGIN SUCCESSFULL!! LET's FLY ✈️")
                break
            else:
                print("Please check your password, email and phone number again,")
                print("something feels sketchy!! 🤔 ")
                print("DO YOU WANT TO SIGN-up INSTEAD yes(y)/no(n)")
                choice=input()
                if choice in ['y','Y','yes','YES']:
                    return None
                else:
                    continue
                
                
                continue
        while True:
            print()
            print(" -------------------------------------------------------------------")
            print("| ✈️✈️✈️✈️ICARUS AVIATION WELCOMES "+usrnm+" ✈️✈️✈️✈ |")
            print(" -------------------------------------------------------------------")
            print()
            print()
            choice2=[['       CHOICE      ','     KEY TO BE PRESSED ON KEYBOARD      '],['Booking a flight',1],['Cancelling a flight',2],['update existing customer details ',3],['view Booked Flights',4],['sign out',5]]
            print(tabulate.tabulate(choice2,headers='firstrow',tablefmt='fancy_grid'))
            print()
            print()
            ch3=input()
            if ch3=='1':
                while True:
                    print()
                    board=input("FROM: ")
                    print()
                    if board.isalpha():
                        print(" ✅ ")
                        break
                    else:
                        print("Sorry, our services have not yet started here ")
                        continue
                            
                while True:
                    print()
                    dest=input("TO: ")
                    print()
                    if dest.isalpha():
                        print(" ✅ ")
                        break
                    else:
                        print("Sorry, our services have not yet started here ")
                        continue
                flight_sts(board,dest)
                count+=1
                count_st=str(count)
                flight_val="111"+count_st
                cost=random.randint(7000,9000)
                cost_updt=str(cost)
                cur.execute("insert into flight_status values('{}','{}','{}','{}','{}')".format(flight_val,board,dest,cost_updt,date_5))
                mydb.commit()
                cur.execute("select*from flight_status")
                myres=cur.fetchall()
                statu=[["FLIGHT NO","BOARDING","DESTINATION","COST","DATE"]]
                for x in myres:
                    lis=[x[0],x[1],x[2],x[3],x[4]]
                    statu.append(lis)
                print(tabulate.tabulate(statu,headers='firstrow',tablefmt='fancy_grid'))
                book=input("Enter flight number: ")
                while True:
                    seats=input("Enter no. of seats (maximum 10): ")
                    if seats.isdigit():
                        break
                    else:
                        print(" PLEASE SELECT NUMBER OF SEATS (maximum 10): ")
                        continue
                while True:
                    print()
                    payment=input("Enter payment mode: (card➟ Type(c), UPI➟ Type(u)): ")
                    print()
                    if payment.lower()=='c':
                        cvv=input("Please enter the cvv number printed at the back of your card: ")
                        if cvv.isdigit():
                            print()
                            break
                        else:
                            print("cvv should be a number ")
                            continue
                    else:
                        print()
                        print(" ACCEPTING UPI REQUEST ")
                        print()
                        break
                while True:
                    pin=input("Please enter the four digit pin of your account")
                    if pin.isdigit():
                        print()
                        break
                    else:
                        print("pin should be a number ")
                        continue
                    
                cur.execute("select*from flight_status where flight_no='{}'".format(book))
                res=cur.fetchall()
                for s in res:
                    from_place=s[1]
                    to=s[2]
                    date=s[4]
                    amt=s[3]
                amt_final=(int(amt)*int(seats))
                amt_final2=str(amt_final)
                Type=input("✈ PRESS ENTER TO PROCEED TO PAY "+"₹"+amt_final2)
                print()
                print(".................................PROCESSING ⌛.....................................")
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PAYMENT SUCCESSFULL ✅~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                cur.execute("insert into booked_flight values('{}','{}','{}','{}','{}','{}')".format(from_place,to,date,phone,book,seats))
                mydb.commit()
                print()
                print(seats+" seat/seats booked successfully in flight number"+book+" ✈️")
                print()
                print(" ----------------------------------------------------------------------------------")
                print("|                    THANK YOU FOR CHOOSING ICARUS AVIATION ✈                     |")
                print(" ----------------------------------------------------------------------------------")
                print()
            elif ch3=='2':
                while True:
                    list3=[]
                    cur.execute("select*from booked_flight")
                    res=cur.fetchall()
                    for t in res:
                        list3.append([t[3],t[4]])
                    book2=input("Enter flight number of flight to cancel ")
                    LIST4=[phone,book2]
                    if LIST4 in list3:
                        cur.execute("delete from booked_flight where phone_num='{}'".format(phone))
                        print()
                        print("✈️FLIGHT CANCELLED SUCCESSFULLY ")
                        print(" A refund of only 80% of the total amount will be provided")
                        print(" Refund amount will get credited in your bank account,")
                        print(" within 2-3 business days")
                        break
                    else:
                        print("✈ NO BOOKINGS MADE FOR SELECTED FLIGHT ")
                        break
            elif ch3=='5':
                print(" EXITING.........  ")
                return
            elif ch3=='3':
                while True:
                    print()
                    choice3=[['       CHOICE      ','     KEY TO BE PRESSED ON KEYBOARD      '],['update username',1],['update email',2],['update phone_no',3],['update password',4],['exit this menu',5]]
                    print(tabulate.tabulate(choice2,headers='firstrow',tablefmt='fancy_grid'))

                    print()
                    select=input("")
                    if select=='1':
                        new=input("✈ Enter new username ")
                        cur.execute("update customer set username='{}' where phone_num='{}'".format(new,phone))
                        mydb.commit()
                    elif select=='2':
                        new2=input("✈ Enter new email ")
                        cur.execute("update customer set email='{}' where phone_num='{}'".format(new2,phone))
                        mydb.commit()
                    elif select=='3':
                        new3=input("✈ Enter new phone number ")
                        cur.execute("update customer set phone_num='{}' where phone_num='{}'".format(new3,phone))
                        mydb.commit()
                    elif select=='4':
                        new4=input("✈ Enter new password ")
                        cur.execute("update customer set phone_num='{}' where phone_num='{}'".format(new4,phone))
                        mydb.commit()
                    elif select=='5':
                        break
                    else:
                        print(" PLEASE ENTER A VALID CHOICE ")
            elif ch3=='6':
                return None
            elif ch3=='4':
                jo=[['BOARDING','DESTINATION','DATE','PHONE','FLIGHT_NO','SEATS']]
                cur.execute("select * from booked_flight where phone_num='{}'".format(phone))
                resolt=cur.fetchall()
                for i in resolt:
                    x=[i[0],i[1],i[2],i[3],i[4],i[5]]
                    jo.append(x)
                if len(jo)>1:
                    print(tabulate.tabulate(jo,headers='firstrow',tablefmt='fancy_grid'))
                else:
                    print()
                    print("✈ No flights booked 🫠 ")
                    print()
            else:
                print(" PLEASE ENTER A VALID CHOICE FROM (1/2/3/4/5/6)")

        
while True:
    print("✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈ ✈️✈️✈️✈️✈️✈  ✈  ✈    ")
    print("✈️                         ICARUS AVIATION                       ✈ ")
    print("✈️                        "+get_super("the world on wings")+"                     ✈")
    print("✈️✈️✈️✈️✈️✈️✈️✈️✈️✈️✈ ✈️✈️✈️✈️✈️✈  ✈  ✈    ")
    print()
    print()
    choice=[['       CHOICE      ','     KEY TO BE PRESSED ON KEYBOARD      '],['LOG-in   ',1],['Sign-up  ',2],['To exit  ',3]]
    print(tabulate.tabulate(choice,headers='firstrow',tablefmt='fancy_grid'))
    print()
    print()
    ch=input()
    if ch=='2':
        phone_lst=[]
        email_lst=[]
        cur.execute("select*from customer")
        res=cur.fetchall()
        for u in res:
            p=[u[1],u[3],u[0]]
            q=[u[2],u[3],u[0]]
            phone_lst.append(p)
            email_lst.append(q)

        password=input("enter your password maximum length 15 characters ")
        if len(password)>15:
            print(" Please enter a valid password ")
        us_name=input("enter username: ")
        go=0
        while True:
            length=len(phone_lst)
            cnt2=0
            phone=input("enter phone: ")
            if phone.isdigit() and (len(phone)==10):
                for i in phone_lst:
                    if phone==i[0]:
                        print("An Account Already Exists With This Phone Number!")
                        ch2=input(" Want to LOG-in? (y/n) ")
                        if ch2=='y' or ch2=='Y' :
                            log_in()
                            break
                        else:
                            print("Enter a new phone number ")
                            continue
                    else:
                        cnt2+=1
                        continue
            else:
                print(" ENTER A VALID PHONE NUMBER ")
            if cnt2==length:
                go+=1
                break
            else:
                continue
        while True:
            length2=len(email_lst)
            cnt=0
            email=input("enter email: ")
            for j in email_lst:
                if email==j[0]:
                    print("An Account Already Exists With This email !")
                    ch3=input(" Want to LOG-in? (y/n) ")
                    if ch3=='y' or ch3=='Y' :
                        log_in()
                        break
                    else:
                        print("Enter a new email ")
                else:
                    cnt+=1
                    continue
            if cnt==length:
                go+=1
                break
            else:
                continue
        if go==2:
            cur.execute("insert into customer values('{}','{}','{}','{}')".format(us_name,phone,email,password))
            mydb.commit()
        while True:
            print()
            print("------------------------------------------------------------------------------------")
            print("       ✈️✈️✈️✈️ICARUS AVIATION WELCOMES "+us_name+" ✈️✈️✈️✈️    ")
            print("------------------------------------------------------------------------------------")
            print()
            print()
            choice2=[['       CHOICE      ','     KEY TO BE PRESSED ON KEYBOARD      '],['Booking a flight',1],['Cancelling a flight',2],['update existing customer details ',3],['view Booked Flights',4],['sign out',5]]
            print(tabulate.tabulate(choice2,headers='firstrow',tablefmt='fancy_grid'))
            print()
            print()
            ch3=input()
            if ch3=='1':
                while True:
                    print()
                    board=input("FROM: ")
                    print()
                    if board.isalpha():
                        print(" ✅ ")
                        break
                    else:
                        print("Sorry, our services have not yet started here ")
                        continue
                            
                while True:
                    print()
                    dest=input("TO: ")
                    print()
                    if dest.isalpha():
                        print(" ✅ ")
                        break
                    else:
                        print("Sorry, our services have not yet started here ")
                        continue
                flight_sts(board,dest)
                count+=1
                count_st=str(count)
                flight_val="111"+count_st
                cost=random.randint(7000,9000)
                cost_updt=str(cost)
                cur.execute("insert into flight_status values('{}','{}','{}','{}','{}')".format(flight_val,board,dest,cost_updt,date_5))
                mydb.commit()
                cur.execute("select*from flight_status")
                myres=cur.fetchall()
                statu=[["FLIGHT NO","BOARDING","DESTINATION","COST","DATE"]]
                for x in myres:
                    lis=[x[0],x[1],x[2],x[3],x[4]]
                    statu.append(lis)
                print(tabulate.tabulate(statu,headers='firstrow',tablefmt='fancy_grid'))
                while True:
                    book=input("Enter flight number: ")
                    if book.isdigit():
                        print()
                        break
                    else:
                        print(" PLEASE ENTER A VALID FLIGHT NUMBER")
                while True:
                    seats=input("Enter no. of seats (maximum 10): ")
                    if seats.isdigit():
                        break
                    else:
                        print(" PLEASE SELECT NUMBER OF SEATS (maximum 10): ")
                        continue
                while True:
                    print()
                    payment=input("Enter payment mode: (card➟ Type(c), UPI➟ Type(u)): ")
                    print()
                    if payment.lower()=='c':
                        cvv=input("Please enter the cvv number printed at the back of your card: ")
                        if cvv.isdigit():
                            print()
                            break
                        else:
                            print("cvv should be a number ")
                            continue
                    else:
                        print()
                        print(" ACCEPTING UPI REQUEST ")
                        print()
                        break
                while True:
                    pin=input("Please enter the four digit pin of your account")
                    if pin.isdigit():
                        print()
                        break
                    else:
                        print("pin should be a number ")
                        continue
                    
                cur.execute("select*from flight_status where flight_no='{}'".format(book))
                res=cur.fetchall()
                for s in res:
                    date=s[4]
                    to=s[2]
                    from_place=s[1]
                    amt=s[3]
                amt_final=(int(amt)*int(seats))
                amt_final2=str(amt_final)
                Type=input("✈ TYPE ENTER TO PROCEED TO PAY "+"₹"+amt_final2)
                print()
                print(".................................PROCESSING ⌛.....................................")
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PAYMENT SUCCESSFULL ✅~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                cur.execute("insert into booked_flight values('{}','{}','{}','{}','{}','{}')".format(from_place,to,date,phone,book,seats))
                mydb.commit()
                print()
                print(seats+"seats booked successfully in flight number"+book+" ✈️")
                print()
                print("+----------------------------------------------------------------------------------+")
                print("|                    THANK YOU FOR CHOOSING ICARUS AVIATION ✈                      |")
                print("+----------------------------------------------------------------------------------+")
                print()
            elif ch3=='2':
                while True:
                    list3=[]
                    cur.execute("select*from booked_flight")
                    res=cur.fetchall()
                    for t in res:
                        list3.append([t[3],t[4]])
                    book2=input("Enter flight number of flight to cancel ")
                    LIST4=[phone,book2]
                    if LIST4 in list3:
                        cur.execute("delete from booked_flight where phone_num='{}'".format(phone))
                        print()
                        print("✈️FLIGHT CANCELLED SUCCESSFULLY ")
                        print(" A refund of only 80% of the total amount will be provided")
                        print(" Refund amount will get credited in your bank account,")
                        print(" within 2-3 business days")
                        break
                    else:
                        print()
                        print("✈ The flight number entered does not exist! ")
                        break
            elif ch3=='sshshshsh':
                break
            elif ch3=='3':
                while True:
                    count=24
                    count2=0
                    phone_lst=[]
                    cur.execute("select*from customer")
                    res=cur.fetchall()
                    for i in res:
                        p=[i[1],i[3],i[0]]
                        phone_lst.append(p)
                    if len(phone_lst)==0:
                        print("NO RECORD AVAILABLE TO SEARCH INTO")
                    else:

                        while True:
                            print()
                            usrnm=input("enter username ")
                            
                            while True:
                                password=input("Enter password")
                                print()
                                if (len(password))>0:
                                    break
                                else:
                                    print("Please enter your password ")
                                    continue
                            flag=0
                            for i in phone_lst:
                                if i[2]==usrnm and i[1]==password:
                                    flag+=1
                                    phone=i[0]
                            if flag==1:
                                print("LOGIN SUCCESSFULL!! ✈️")
                                break
                            else:
                                print("Please check your password, email and phone number again,")
                                print("something feels sketchy!! 🤔 ")
                                continue
                    print()
                    choice3=[['       CHOICE      ','     KEY TO BE PRESSED ON KEYBOARD      '],['update username',1],['update email',2],['update phone_no',3],['update password',4],['exit this menu',5]]
                    print(tabulate.tabulate(choice2,headers='firstrow',tablefmt='fancy_grid'))

                    print()
                    select=input("")
                    if select=='1':
                        new=input("✈ Enter new username ")
                        cur.execute("update customer set username='{}' where phone_num='{}'".format(new,phone))
                        mydb.commit()
                    elif select=='2':
                        new2=input("✈ Enter new email ")
                        cur.execute("update customer set email='{}' where phone_num='{}'".format(new2,phone))
                        mydb.commit()
                    elif select=='3':
                        new3=input("✈ Enter new phone number ")
                        cur.execute("update customer set phone_num='{}' where phone_num='{}'".format(new3,phone))
                        mydb.commit()
                    elif select=='4':
                        new4=input("✈ Enter new password ")
                        cur.execute("update customer set phone_num='{}' where phone_num='{}'".format(new4,phone))
                        mydb.commit()
                    elif select=='5':
                        break
                    else:
                        print(" PLEASE ENTER A VALID CHOICE ")
                        
            elif ch3=='5':
                print()
                print(" EXITING........ ")
                print()
                break
            elif ch3=='4':
                j=[['BOARDING','DESTINATION','DATE','PHONE','FLIGHT_NO','SEATS']]
                cur.execute("select * from booked_flight where phone_num='{}'".format(phone))
                resolt=cur.fetchall()
                for i in resolt:
                    x=[i[0],i[1],i[2],i[3],i[4],i[5]]
                    j.append(x)
                if len(j)>1:
                    print(tabulate.tabulate(j,headers='firstrow',tablefmt='fancy_grid'))
                else:
                    print()
                    print("✈ No flights booked {{{(>_<)}}} ")
                    print()

            else:
                print()
                print("PLEASE ENTER A VALID CHOICE (1/2/3/4/5)")
    elif ch=='1':
        log_in()
    elif ch=='3':
        print(" EXITING..........")
        break
    else:
        print("✈️ Please enter a valid choice (1/2/3) ")

               
        



