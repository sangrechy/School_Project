##################################-IMPORTING MODULE AND PACKAGES-###########################
import mysql.connector as sql
import time

#######################################-CONNECTING TO MYSQL-################################
user='root'#{user_name}
password=''#{user_password}
def CONNECT():
    connection_object=sql.connect(host='localhost',user=user,passwd=password)
    return connection_object
connection_object=CONNECT()
if connection_object.is_connected():
    print('SUCCESSFULLY CONNECTED TO MYSQL..')
else:
    print('ERROR CONNECTING TO MYSQL, PLEASE TRY AGAIN')
    connection_object=CONNECT()
    if connection_object.is_connected():
        print('SUCCESSFULLY CONNECTED TO MYSQL..')
    else:
        print('ERROR CONNECTING TO MYSQL, PLEASE TRY LATER')
        time.sleep(20)
        exit()
cursor_object=connection_object.cursor()

#######################################-CREATING DATABASE AND TABLES-######################
#CREATING DATABASES AND ACCESSING IT
cursor_object.execute('CREATE DATABASE IF NOT EXISTS MOVIES;')
cursor_object.execute('USE MOVIES;')

#CREATING TABLES:-
#TABLES:-
#1.MOVIES_INFO TABLE: CONTAINS INFORMATION ABOUT MOVIES (i.e)MOVIE CODE, MOVIES NAME,YEAR RELEASED,
#  MOVIE GENERE,DURATION, ACTORS NAME, IMDB RATING.  ******
#2.MOVIES_ANALYSING TABLE: CONTAINS DATA OF MOVIES SUCH AS WHICH AGE CATAGEROY PEOPLE WOULD
#  WATCH, WHETHER ITS MALE OR FEMALE.
#3.USER_INFO TABLE: CONTAINS INFORMATION OF USER SUCH AS USER ID, NAME, AGE, GENDER,
#  FAVORITE ACTOR. 
#4.USER_ANALYSING TABLE: CONTAINS STATSTICS OF USER ABOUT HIS/HER PREFERENCES IN GENERE
#5.AGE_ANALYSING TABLE: CONTAINS STATSTICS OF MOVIES GENERE ACCORDING TO AGE
#6.RENT_HISTORY TABLE: CONTAIN RENT HISTORY. ******

tempvar='CREATE TABLE IF NOT EXISTS MOVIE_INFO(MOVIE_CODE INT PRIMARY KEY,MOVIE_NAME VARCHAR(60),\
YEAR_RELEASED YEAR(4),GENERE VARCHAR(50),ACTORS VARCHAR(50),DURATION TIME,IMDB_RATING FLOAT, PRICE INT DEFAULT 0);'
cursor_object.execute(tempvar)

tempvar='CREATE TABLE IF NOT EXISTS MOVIE_ANALYSING(MOVIE_CODE INT  REFERENCES \
MOVIE_INFO(MOVIE_CODE),1_5 INT DEFAULT 0, 5_10 INT DEFAULT 0, 10_15 INT DEFAULT 0, 15_20\
 INT DEFAULT 0, 20_25 INT DEFAULT 0, 25_30 INT DEFAULT 0, 30_40 INT DEFAULT 0, 40_50 INT\
 DEFAULT 0, 50_70 INT DEFAULT 0,70PLUS INT DEFAULT 0,MALE INT DEFAULT 0,FEMALE INT DEFAULT 0 ,NIL INT  );'
cursor_object.execute(tempvar)

tempvar='CREATE TABLE IF NOT EXISTS USER_INFO(USER_ID INT PRIMARY KEY,USER_NAME VARCHAR(20),AGE INT,\
GENDER ENUM("MALE","FEMALE","NIL"),FAVORITE_ACTOR VARCHAR(50));'
cursor_object.execute(tempvar)

tempvar='CREATE TABLE IF NOT EXISTS USER_ANALYSING(USER_ID  INT REFERENCES \
 USER_INFO(USER_ID),SCI_FI  INT DEFAULT 0,ACTION  INT DEFAULT 0, THRILLER  INT DEFAULT\
 0, HORROR  INT DEFAULT 0, ANIMATION  INT DEFAULT 0, FAMILY  INT DEFAULT 0, FANTASY  INT \
 DEFAULT 0, COMEDY  INT DEFAULT 0, DRAMA  INT DEFAULT 0, FICTION  INT DEFAULT 0,\
 ROMANCE  INT DEFAULT 0, ADVENTURE  INT DEFAULT 0);'
cursor_object.execute(tempvar)

tempvar='CREATE TABLE IF NOT EXISTS AGE_ANALYSING(GENERE VARCHAR(20) PRIMARY KEY,1_5\
 INT DEFAULT 0, 5_10 INT DEFAULT 0, 10_15 INT DEFAULT 0, 15_20 INT DEFAULT 0, 20_25 \
 INT DEFAULT 0, 25_30 INT DEFAULT 0, 30_40 INT DEFAULT 0, 40_50 INT DEFAULT 0 ,\
 50_70 INT DEFAULT 0 ,70PLUS INT DEFAULT 0 ,MALE INT DEFAULT 0 ,FEMALE INT DEFAULT 0,NIL INT  );'
cursor_object.execute(tempvar)

tempvar='CREATE TABLE IF NOT EXISTS RENT_HISTORY(USER_ID INT REFERENCES USER_INFO(USER_ID),USER_NAME\
 VARCHAR(20),MOVIE_CODE INT REFERENCES MOVIE_INFO(MOVIE_CODE),\
MOVIE_NAME VARCHAR(60),RENTED_DATE DATE, DUE_DATE DATE,PAYMENT_STATUS \
ENUM("DUE","PAYED"));'
cursor_object.execute(tempvar)

cursor_object.fetchall()
tempvar=('SELECT COUNT(*) FROM AGE_ANALYSING ;')
cursor_object.execute(tempvar)
if not int(cursor_object.fetchone()[0])==12:
    tempvar="INSERT INTO AGE_ANALYSING (GENERE) VALUES('SCI_FI'),('ACTION'),('THRILLER'),('HORROR'),('ANIMATION'),('FAMILY'),('FANTASY'),\
    ('COMEDY'),('DRAMA'),('FICTION'),('ROMANCE'),('ADVENTURE');"
    cursor_object.execute(tempvar)
    connection_object.commit()

#################################################-FUNCTIONS-######################################3
#1.checkdue(userid): CHECKS FOR PENDING DUES. +
#2.agegap(age): GROUPS AGE.
#3.pay(moviecode,userid):PAYS THE RENT.
#4.payment(userid):FIND AND PAY THE RENT OR DUE.
#5.movievote(moviecode,age,gender):COLLECTS THE INFORMATION ABOUT MOVIE AND USER ON EACH PURCHASE.
#6.rent(moviecode,moviename,userid,username):CREATE A RENT HISTORY.
#7.movieselect(userid):SELECTS THE MOVIE FOR PURCHASING. +++++++++++++
#8.recommend(userid):RECOMMEND THE MOVIES ON COMMONFEED AS WELL AS USERFEED.

def tableconnection():
    cursor_object.fetchall()
    tempvar=('SELECT COUNT(*) FROM MOVIE_INFO ;')
    cursor_object.execute(tempvar)
    movieinfo=int(cursor_object.fetchone()[0])
    cursor_object.fetchall()
    tempvar=('SELECT COUNT(*) FROM MOVIE_ANALYSING ;')
    cursor_object.execute(tempvar)
    movieanalyse=int(cursor_object.fetchone()[0])
    if not movieinfo==movieanalyse:
            for i in range(movieanalyse+1,movieinfo+1):
                tempvar=("INSERT INTO MOVIE_ANALYSING (MOVIE_CODE) VALUES ({moviecode});")\
.format(moviecode=i)
                cursor_object.execute(tempvar)
                connection_object.commit()
    cursor_object.fetchall()
    tempvar=('SELECT COUNT(*) FROM USER_INFO ;')
    cursor_object.execute(tempvar)
    userinfo=int(cursor_object.fetchone()[0])
    cursor_object.fetchall()
    tempvar=('SELECT COUNT(*) FROM USER_ANALYSING ;')
    cursor_object.execute(tempvar)
    useranalyse=int(cursor_object.fetchone()[0])
    if not userinfo==useranalyse:
            for i in range(useranalyse+1,userinfo+1):
                tempvar=("INSERT INTO USER_ANALYSING (USER_ID) VALUES ({userid});")\
.format(userid=i)
                cursor_object.execute(tempvar)
                connection_object.commit()
        
        
        
def checkdue(userid):
    cursor_object.fetchall()
    tempvar=('SELECT MOVIE_NAME,MOVIE_CODE FROM RENT_HISTORY WHERE USER_ID={userid} AND\
 DUE_DATE < CURDATE() AND PAYMENT_STATUS="DUE";').format(userid=userid)
    cursor_object.execute(tempvar)
    duemovie=cursor_object.fetchall()
    if len(duemovie)==0:
        return True
    else:
        print('YOUR RENT ON THE MOVIES:-',end="")
        for i in duemovie:
            print(i[0],'code=',i[1],end=',')
        print('HAVE NOT RETURNED AND YOUR DUE DATE HAD BEEN OVER.PLEASE COMPLETE YOUR\
 DUE TO CLEAR ALL RESTRICTION')
        return False
    

def agegap(age):
    if age>=70:
        return '70PLUS'
    elif age>=50:
        return '50_70'
    elif age>=40:
        return '40_50'
    elif age>=30:
        return '30_40'
    elif age>=25:
        return '25_30'
    elif age>=20:
        return '20_25'
    elif age>=15:
        return '15_20'
    elif age>=10:
        return '10_15'
    elif age>=5:
        return '5_10'
    else:
        return '1_5'

def pay(moviecode,userid):
    tempvar=("SELECT TIMESTAMPDIFF(DAY , CURDATE(),DUE_DATE) FROM RENT_HISTORY\
 WHERE USER_ID={userid} AND MOVIE_CODE={moviecode} AND PAYMENT_STATUS='DUE';").\
format(userid=userid,moviecode=moviecode)
    cursor_object.execute(tempvar)
    datediff=int(cursor_object.fetchone()[0])
    cursor_object.fetchall()
    tempvar=("SELECT PRICE FROM MOVIE_INFO WHERE MOVIE_CODE={moviecode};").\
             format(moviecode=moviecode)
    cursor_object.execute(tempvar)
    price=(cursor_object.fetchone())
    if price==(None,):
        price=[1000]
    price=int(price[0])
    cursor_object.fetchall()
    if datediff >=0:
        print('YOUR PRICE IS:',price)
        finalprice=price
    else:
        fine=-1*(5/100)*price*datediff
        finalprice=price+fine
        print('YOUR FINAL AMOUNT:',price,'+',fine,'(FINE)=',finalprice)
        print('YOU HAVE FINED BECAUSE YOUR DUE DATE IS OVER BEFORE:',datediff*-1,'DAYS')
    temp=True
    while temp:
        try:
            var=int(input('ENTER 1 TO PROCCED TRANSACTION..'))
            temp=False
        except:
            print('INVALID INPUT, PLESE TRY AGAIN')
    if var==1:
        tempvar=("UPDATE RENT_HISTORY SET PAYMENT_STATUS='PAYED' WHERE USER_ID={userid}\
 AND MOVIE_CODE={moviecode};").format(userid=userid,moviecode=moviecode)
        cursor_object.execute(tempvar)
        connection_object.commit()
        print('YOUR TRANSACTION IS SUCCESSFUL')
    else:
        print('TRANSACTION FAILED.. PLEASE TRY AGAIN')

def payment(userid):
    tempvar=("SELECT MOVIE_NAME, MOVIE_CODE FROM RENT_HISTORY WHERE USER_ID={userid}\
 AND PAYMENT_STATUS='DUE';").format(userid=userid)
    cursor_object.execute(tempvar)
    var=cursor_object.fetchall()
    if len(var)==0:
        print('YOU HAVE NO DUE PAYMENT')
        return None
    print('YOU HAVE DUE ON THE MOVIES:')
    moviecode1=[]
    for i in var:
        print(i[0],'MOVIE_CODE=',i[1])
        moviecode1.append(i[1])
    print('HAVE NOT PAYED YET')
    var=int(input('ENTER THE MOVIE CODE FOR PAYMENT...\
NOTE YOU CAN PAY ONLY ONE MOVIE AT A TIME'))
    if var not in moviecode1:
        print('INVALID MOVIE CODE, TRY AGAIN')
        return None
    pay(var,userid)

def movievote(moviecode,age,gender):
    tempvar=("UPDATE MOVIE_ANALYSING  SET {age}={age}+1 WHERE MOVIE_CODE={moviecode};").\
             format(moviecode=moviecode,age=age)
    cursor_object.execute(tempvar)
    connection_object.commit()
    tempvar=("UPDATE MOVIE_ANALYSING  SET {gender}={gender}+1 WHERE MOVIE_CODE={moviecode};").\
             format(moviecode=moviecode,gender=gender)
    cursor_object.execute(tempvar)
    connection_object.commit()
    tempvar=("SELECT GENERE FROM MOVIE_INFO WHERE MOVIE_CODE={moviecode};").\
             format(moviecode=moviecode)
    cursor_object.execute(tempvar)
    genere=cursor_object.fetchone()[0].split(',')
    for i in genere:
        tempvar=("UPDATE AGE_ANALYSING  SET {age}={age}+1 WHERE GENERE='{genere}';").format(genere=i,age=age)
        cursor_object.execute(tempvar)
        connection_object.commit()
        tempvar=("UPDATE AGE_ANALYSING  SET {gender}={gender}+1 WHERE GENERE='{genere}';").format(genere=i,gender=gender)
        cursor_object.execute(tempvar)
        connection_object.commit()
        tempvar=("UPDATE USER_ANALYSING  SET {genere}={genere}+1 WHERE USER_ID={userid};").format(genere=i,userid=userid)
        cursor_object.execute(tempvar)
        connection_object.commit()

def rent(moviecode,moviename,userid,username):
    tempvar=("INSERT INTO RENT_HISTORY(MOVIE_CODE,MOVIE_NAME,USER_NAME,USER_ID,DUE_DATE,RENTED_DATE,PAYMENT_STATUS)\
 VALUES({moviecode},'{moviename}','{username}',{userid},DATE_ADD(CURDATE() ,INTERVAL 60 DAY) ,CURDATE(),'DUE' );")\
 .format(userid=userid,moviecode=moviecode,username=username,moviename=moviename)
    cursor_object.execute(tempvar)
    connection_object.commit()
    tempvar='SELECT DATE_ADD(CURDATE() ,INTERVAL 60 DAY)'
    cursor_object.execute(tempvar)
    date=cursor_object.fetchone()[0]
    cursor_object.fetchall()
    print('MOVIE PURCHASED.. \n  NOTE: YOUR DUE DATE IS AFTER 60 DAYS FROM NOW ON..THAT IS',date)


def movieselect(userid):
    tempvar=("SELECT MOVIE_NAME,MOVIE_CODE FROM MOVIE_INFO;")
    cursor_object.execute(tempvar)
    movie=cursor_object.fetchall()
    var=input('ENTER THE MOVIENAME')
    var=var.lower().split()
    x=0
    if x>=0:
        print('MATCHES FOUND:')
    for i in movie:
        i1=i[0].lower().split()+[str(i[1])]
        if any(x in var for x in i1):
            x=x+1
            print(i[0],'CODE=',i[1])
    if x==0:
        print('NONE , TRY AGAIN')
        return False
    tempvar=("SELECT AGE, GENDER, USER_NAME FROM USER_INFO WHERE USER_ID={userid};").format(userid=userid)
    cursor_object.execute(tempvar)
    var=cursor_object.fetchone()
    cursor_object.fetchall()
    age=agegap(int(var[0]))
    gender=var[1]
    username=var[2]
    temp=True
    while temp:
        try:
            var=int(input('ENTER THE MOVIE CODE:'))
            temp=False
        except:
            print('INVALID INPUT, PLESE TRY AGAIN')
    temp=var
    tempvar=("SELECT MOVIE_NAME FROM MOVIE_INFO WHERE MOVIE_CODE={moviecode};").format(moviecode=temp)
    cursor_object.execute(tempvar)
    var3=cursor_object.fetchone()
    cursor_object.fetchall()
    if var3==None:
            print('NO RESULT FOUND, TRY AGAIN')
            return False
    moviename=var3[0]
    moviecode=temp
    rent(moviecode,moviename,userid,username)
    movievote(moviecode,age,gender)
    print('HOPE YOU ENJOYED OUR SERVICE')
    return True

def recommend(userid):
    print('LET US ANALYSE FOR YOU')
    tempvar=("SELECT AGE, GENDER, USER_NAME FROM USER_INFO WHERE USER_ID={userid};").format(userid=userid)
    cursor_object.execute(tempvar)
    var=cursor_object.fetchone()
    cursor_object.fetchall()
    age=agegap(int(var[0]))
    gender=var[1]
    username=var[2]
    tempvar=("SELECT GENERE FROM AGE_ANALYSING ORDER BY {age} desc;").format(age=age)
    cursor_object.execute(tempvar)
    genere=cursor_object.fetchall()
    if genere==None :
        genere=[]
    if  len(genere)>=2:
        genere1=genere[0][0]
        genere2=genere[1][0]
        tempvar=("SELECT MOVIE_NAME,MOVIE_INFO.MOVIE_CODE FROM MOVIE_INFO, MOVIE_ANALYSING WHERE MOVIE_INFO.MOVIE_CODE=\
    MOVIE_ANALYSING.MOVIE_CODE AND (GENERE LIKE '%{genere1}%' OR GENERE LIKE '%{genere2}%') ORDER BY\
    ({age}+{gender});").format(genere1=genere1,genere2=genere2,gender=gender,age=age)
        cursor_object.execute(tempvar)
        movies=cursor_object.fetchmany(5)
        cursor_object.fetchall()
        x=0
        print(('BASED ON COMMON FEED, MOST {gender}S AT YOUR AGE WOULD LIKE TO WATCH {genere1} AND {genere2}\
 THUS I RECOMMEND:').format(gender=gender,genere1=genere1,genere2=genere2))
        for i in movies:
            x=x+1
            print(x,'.',i[0],'CODE=',i[1])
    else:
        print('INSUFFICENT DATA FOR COMMON FEED')
    print()
    tempvar=("SELECT * FROM USER_ANALYSING WHERE USER_ID={userid}").format(userid=userid)
    cursor_object.execute(tempvar)
    var=['SCI_FI', 'ACTION', 'THRILLER', 'HORROR', 'ANIMATION', 'FAMILY', 'FANTASY', 'COMEDY']
    var1=(cursor_object.fetchone())
    if var1 == (None) :
        var1=[0]
    var1=list(var1) 
    cursor_object.fetchall()
    var1.pop(0)
    var2=sorted(var1,reverse=True)
    var2=list(set(var2)) 
    if len(var2)>=2:
        genere1=var[var1.index(var2[0])]
        genere2=var[var1.index(var2[1])]
        tempvar=("SELECT MOVIE_NAME,MOVIE_INFO.MOVIE_CODE FROM MOVIE_INFO, MOVIE_ANALYSING WHERE MOVIE_INFO.MOVIE_CODE=\
    MOVIE_ANALYSING.MOVIE_CODE AND (GENERE LIKE '%{genere1}%' OR GENERE LIKE '%{genere2}%') ORDER BY\
     ({age}+{gender});").format(genere1=genere1,genere2=genere2,gender=gender,age=age)
        cursor_object.execute(tempvar)
        movies=cursor_object.fetchmany(5)
        cursor_object.fetchall()
        x=0
        print(('BASED ON YOUR FEED, YOU WOULD LIKE TO WATCH {genere1} AND {genere2}\
 THUS I RECOMMEND:').format(genere1=genere1,genere2=genere2))
        for i in movies:
            x=x+1
            print(x,'.',i[0],'CODE=',i[1])
    else:
        print('INSUFFICENT DATA FOR USER FEED')

###################################################-LOG IN-#########################################################
def login():
    username=input('ENTER THE USER NAME:')
    tableconnection()
    tempvar=('SELECT USER_ID FROM USER_INFO WHERE USER_NAME="{username}" ;').format(username=username)
    cursor_object.execute(tempvar)
    userexists=cursor_object.fetchone()
   
    if userexists==None:
        print('WELCOME IT SEEMS LIKE YOU ARE NEW TO OUR SHOP..LETS CREATE AN ACCOUNT FOR YOU')
        temp=True
        while temp:
            try:
                age=int(input('YOUR AGE:'))
                temp=False
            except:
                print('INVALID INPUT, PLESE TRY AGAIN')
        gender=input('ARE YOU MALE OR FEMALE:').upper()
        if not(gender ==  'MALE' or gender == 'FEMALE'):
           gender='NIL'
        tempvar='SELECT COUNT(*)FROM USER_INFO;'
        cursor_object.execute(tempvar)
        userid=userexists=cursor_object.fetchone()[0]+1
        tempvar=('INSERT INTO USER_INFO VALUES({userid},"{username}",{age},"{gender}",NULL);')\
                 .format(userid=userid,username=username,age=age,gender=gender.upper())
        cursor_object.execute(tempvar)
        connection_object.commit()
        print(('YOUR USERNAME:{username} \n     USERID:{userid}').format(username=username,userid=userid))
    tempvar=('SELECT USER_ID FROM USER_INFO WHERE USER_NAME="{username}" ;').format(username=username)
    cursor_object.fetchall()
    cursor_object.execute(tempvar)
    userid=cursor_object.fetchone()[0]
    temp=True
    while temp:
        try:
            varuserid=int(input('ENTER YOUR ID:'))
            temp=False
        except:
            print('INVALID INPUT, PLESE TRY AGAIN')
    if varuserid==userid:
        print('WELCOME',username.upper())
    else:
        print('WRONG USER ID..TRY AGAIN')
        temp=True
        while temp:
            
            try:
                varuserid=int(input('ENTER YOUR ID:'))
                temp=False
            except:
                print('INVALID INPUT, PLESE TRY AGAIN')

        if varuserid==userid:
            print('WELCOME',username.upper())
        else:
            print('WRONG USER ID..TRY LATER')
            time.sleep(5)
            exit()
    return userid

############################################-START-########################################
def start(userid):
    print('WHAT CAN I DO FOR YOU:')
    for i in range(10):
        print()
        print('###########################################################################')
        print('1.RENT A MOVIE','2.RECOMMEND A MOVIE','3.PAY FOR THE MOVIE RENT','4.EXIT',sep='\n')
        print('ENTER THE CORRECT SNO FOR GIVEN OPTIONS')
        temp=True
        while temp:
            try:
                var=int(input('SNO:'))
                temp=False
            except:
                print('INVALID INPUT, PLESE TRY AGAIN')
        print()
        if var==1:
            for i in range(5):
                x=movieselect(userid)
                if x==True:
                    break
            else:
               print('PLEASE TRY LATER..')
        elif var==2:
            recommend(userid)
        elif var==3:
            payment(userid)
        elif var==4:
            print('HOPE WE MEET AGAIN THANK YOU')
            print('YOU WOULD AUTOMATICALLY EXIT IN 10 SEC')
            connection_object.close()
            time.sleep(10)
            exit()#################END
            break
            time.sleep(10)
        else:
           if i==4:
               print('CANT UNDERSTAND YOU TRY LATER..')
               exit()
           else:
                print('CANT UNDERSTAND YOU TRY AGAIN..')
        print()
        print()
                
    print('YOU WOULD AUTOMATICALLY EXIT IN 10 SEC')
    connection_object.close()
    time.sleep(10)
    exit()##############END      
               
temp1=True
while temp1:
    try:
        userid=login()
        temp1=False
    except:
        print("THERE IS AN ERROR CAUSED DURING LOGIN PLEASE TRY AGAIN..")
        
tableconnection()
varv1=checkdue(userid)
while not varv1:
    print('YOU CANT ACCSESS ANY FUNCTION WITHOUT CLEARING YOUR EXPIRY DUE..')
    payment(userid)
    varv1=checkdue(userid)

temp1=True
while temp1:
    try:
        start(userid)
        temp1=False
    except:
        print("THERE IS AN ERROR CAUSED ON OUR SIDE PLEASE TRY AGAIN..")

        
    







