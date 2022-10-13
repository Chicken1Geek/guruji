import mysql.connector as sql

fit=sql.connect(host='localhost',user='root',passwd='admin@123',database='fit_project')
if fit.is_connected():
       print('connected')
 
print('')
print('')
print('WELCOME TO RAHI FITNESS CENTRE')
print('')
print('')
print('TO LOGIN PRESS                                    :1        ')
print('')
print('')
print('TO CREATE YOUR NEW ACCOUNT PRESS                  :2        ')
print('')
print('')
print('TO EXIT PRESS                                     :3      ')
print('')
c=int(input('enter your choices'))


if (c==1):
    print('')
    print('to login please enter your user id and password')
    print('')
    user_id=input('enter your user id')
    print('')
    passwd=input('enter your password')
    print('')
    name=input('enter your name')
    print('')
    c1=fit.cursor()
    c1.execute('select * from user_fitness_rahi1')
    data=c1.fetchall()
    count=c1.rowcount

    
    for row in data:
        if (user_id in row) and (passwd in row):
            print(' ')
            print('SUCCESSFULLY LOGIN!!!!!!!!')
            print('welcome to ',name,' fitness centre')
            print(' ')
            print(' ')
            print('to see castumer details press             :1          ')
            print(' ')
            print(' to update costumer details press         :2           ')
            print(' ')
            print('to see items in jim press                 :3       ')
            print('')
            print('to update new items press                 :4         ')
            print('')
            c2=int(input('enter your choice'))
            if (c2==1):
                c1=fit.cursor()
                c1.execute('select * from custmer')
                data=c1.fetchall()
                count=c1.rowcount
                print('total custamer is',count)
                for row in data:
                    print(row)
            elif (c2==2):
                print('')
                print('to update costumer details please enter the following details')
                print('')
                v_cusamer_id=int(input('inter castamar id (in intiger)     :'))
                print('')
                v_custamar_name=input('castamer name is        :')
                print('')
                v_camtamar_addras=input('enter addras of castamer')
                print('')
                v_date_of_joined=input('camtamer joined data')
                print('')
                v_amt_paid=int(input('paid amuount'))
                print('')
                c1=fit.cursor()
                #c1.execute('create table custmer(custmer varchar(100) primary key,custmer_name varchar(100),custmer_address varchar(1000),joined_date varchar(100),amt_paid varchar(100))')
                update_dtails="insert into custmer values("+ str(v_cusamer_id) +",'"+ (v_custamar_name) +"','"+ (v_camtamar_addras) +"','"+ (v_date_of_joined) +"',"+ str(v_amt_paid) +")"
                c1.execute(update_dtails)
                fit.commit()
                print('costumer details succesully updated')
            elif (c2==3):
                   print('FOLLOWING ITEMS RECTHERE IN',name ,'JIM')
                   c1=fit.cursor()
                   c1.execute('select * from jim_items')
                   data=c1.fetchall()
                   count=c1.rowcount
                   print('total jim item is',count)
                   for row in data:
                          print(row)
            elif (c2==4):
                   print('to update new items enter the following detils')
                   v_object_id=int(input('enter the object code(in integer)'))
                   v_object_name=input('enter the name of jim items')
                   v_date_of_purchase=input('enter the date og purchase')
                   v_repairing_date=input('enter the date of repair')
                   v_total_people_using=int(input('total person'))
                   c1=fit.cursor()
                   updates2=("insert into jim_items values('"+ str(v_object_id) +"','"+ (v_object_name) +"','"+ (v_date_of_purchase) +"','"+ (v_repairing_date) +"','"+ str(v_total_people_using) +"')")
                   c1.execute(updates2)
                   fit.commit()
                   print('item updated')
                   
            else:
                  ('something wemt wrong')
    
              
                   
                
                


elif (c==2):
    print('')
    print('to create your account please enter your user id and password')
    print('')
    c1=fit.cursor()
    #c1=fit.cursor("('create table user_fitness_rahi1(user_id varchar(100) primary key,password varchar(100),name varchar(100))') 
    v_user_id=int(input('choose your user id (in integar)'))
    print('')
    v_passwd=int(input('create your password (in integar)'))
    print('')
    v_name=input('your full  name')
    print('')
    c1=fit.cursor()
    update=("insert into user_fitness_rahi1 values("+ str(v_user_id) +","+ str(v_passwd) +",'"+ (v_name) +"')")
    c1.execute(update)
    fit.commit()
    print('account created')
elif (c==3):
    print('vist again')
    print('')
    print('thank you')
else:
    ('something wemt wrong')
   
