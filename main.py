import mysql.connector
MYDB=mysql.connector.connect(host='localhost',user='root',password='k@leL4601',database='bank_management')

def openacc():
    n= input("enter the name:")
    ac=input("enter the account number:")
    db=input("enter the data of birth:")
    add=input("enter the address:")
    cn=input("enter the contact number:")
    ob= int(input("enter the opening balance:"))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values (%s,%s,%s)')
    x=MYDB.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    MYDB.commit()
    print('data enter successfully..')
    main()
def despoAMO():
    amount=input('enter the amount you want to deposit:')
    ac=input('enter the account number :')
    a='select balance from amount where ACCNO=%s'
    data=(ac,)
    x=MYDB.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=('update amount set balance where ACCNO=%s')
    d=(t,ac)
    x.execute(sql,d)
    MYDB.commit()
    main()

def withdrawAmount():
    amount = input('enter the amount you want to withdraw:')
    ac = input('enter the account number :')
    a = 'select balance from amount where ACCNO=%s'
    data = (ac,)
    x = MYDB.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update amount set balance where ACCNO=%s')
    d = (t, ac)
    x.execute(sql, d)
    MYDB.commit()
    main()

def balEnq():
    ac = input('enter the account number :')
    a='select * from amount where ACCNO=%s'
    data=(ac,)
    x=MYDB.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print('Balance for account ',ac,'is ',result[-1])
    main()

def disdetails():
    ac = input('enter the account number :')
    a = 'select * from account where ACCNO=%s'
    data = (ac,)
    x = MYDB.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()

def closeAcc():
    ac = input('enter the account number :')
    sql1='delete from account where ACCNO=%s'
    sql2='delete from amount where ACCNO=%s'
    data=(ac,)
    x=MYDB.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    MYDB.commit()
    main()
def main():
    print(
        '''
        1. open new ACCOUNT
        2. DEPOSIT AMOUNT
        3. WITHDRAW THE AMOUNT
        4. BALANCE ENQUIRY
        5. DISPLAY CUSTOMER DETAILS
        6. CLOSE ACCOUNT'''
    )
    choice = input("enter the task you want to perform:")
    if (choice=='1'):
        openacc()
    elif (choice=='2'):
        despoAMO()
    elif (choice=='3'):
        withdrawAmount()
    elif (choice=='4'):
        balEnq()
    elif (choice=='5'):
        disdetails()
    elif (choice=='6'):
        closeAcc()
    else:
        print('invalid choice')
        main()
main()


