import sys
import matplotlib.pyplot as plt
import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',
                              password='abhisek',database='exam')
mycur=mycon.cursor()

def Student_Profile():
    sql="Insert into student(adm_no,name,class,section)values(%s,%s,%s,%s)"
    print('\nPLEASE PROVIDE THE REQUIRED INFORMATION\n')
    ad=input('\nENTER THE ADMISSION NUMBER TO REGISTER FOR EXAM:')
    nm=input('\nENTER THE STUDENT NAME:')
    cls=int(input('\nENTER THE CLASS(11/12):'))
    sec=input('\nENTER THE SECTION(A-D):')
    value=(ad,nm,cls,sec)
    try:
        mycur.execute(sql,value)
        print(nm,'ADDED SUCCESSFULLY TO EXAM MODULE')
        mycon.commit()
    except:
        print('UNABLE TO INSERT!!!!!')



def Edit_Profile():
    sql="Update student set section=%s where adm_no=%s";
    ph=input('\nENTER THE ADMISSION NUMBER WHOSE SECTION TO MODIFY:')
    nm=input('\nENTER THE NEW SECTION(A-D):')
    value=(nm,ph)
    try:
        mycur.execute(sql,value)
        mycon.commit()
        print('RECORD UPDATED SUCCESSFULLY')
    except:
        print('UNABLE TO UPDATE SECTION!!!!')



def Remove_Profile():
    ph=input('\nENTER THE ADMISSION NUMBER TO DELETE:')
    sql='Delete from student where Adm_no=%s'
    value=(ph,)
    try:
        mycur.execute(sql,value)
        mycon.commit()
        print('RECORD DELETED SUCCESSFULLY')
    except:
        mycon.rollback()
        print('UNABLE TO DELETE RECORD!!!')



def Record_Entry():
    sql="Insert into result(adm_no,exam_name,sub1,sub2,sub3,sub4,sub5,total,percentage,attendance,grade,remarks)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print('\nPLEASE PROVIDE THE REQUIRED INFORMATION\n')
    ad=int(input('\nENTER THE ADMISSION NUMBER TO ENTER RECORD:'))
    nm=input('\nENTER THE EXAM NAME:')
    sub1=int(input('ENTER MARKS IN SUBJECT 1(MAX:100):'))
    sub2=int(input('ENTER MARKS IN SUBJECT 2(MAX:100):'))
    sub3=int(input('ENTER MARKS IN SUBJECT 3(MAX:100):'))
    sub4=int(input('ENTER MARKS IN SUBJECT 4(MAX:100):'))
    sub5=int(input('ENTER MARKS IN SUBJECT 5(MAX:100):'))
    total=sub1+sub2+sub3+sub4+sub5
    per=total//5
    wrkday=int(input('ENTER TOTAL NUMBER OF WORKING DAYS:'))
    present=int(input('ENTER NO OF DAYS PRESENT:'))
    att=present/wrkday*100
    att=int(att)
    if(per>=90):
        g='A'
        rem='EXCELLENT PERFORMANCE!!'
    elif(per>=75 and per<90):
        g='B'
        rem='VERY GOOD PERFORMANCE!!'
    elif(per>=55 and per<=75):
        g='C'
        rem='SATISFACTORY PERFORMANCE!!'
    elif(per>=35 and per<55):
        g='D'
        rem='AVERAGE PERFORMANCE!!'
    else:
        g='E'
        rem='SCOPE FOR IMPROVEMENT!!'
    value=(ad,nm,sub1,sub2,sub3,sub4,sub5,total,per,att,g,rem)
    try:
        mycur.execute(sql,value)
        print('RECORD ADDED SUCCESSFULLY TO EXAM MODULE')
        mycon.commit()        
    except:
        print('UNABLE TO INSERT!!!!!')


def Report_Card():
    ad=int(input('\nENTER THE ADMISSION NUMBER TO SEARCH:'))
    sql1='Select * from student where adm_no=%s'
    value=(ad,)
    mycur.execute(sql1,value)
    rec1=mycur.fetchone()
    if(rec1!=None):
           adm=rec1[0]
           name=rec1[1]
           cls=rec1[2]
           sec=rec1[3]
    sql2='Select * from result where adm_no=%s'
    value=(ad,)
    mycur.execute(sql2,value)
    rec2=mycur.fetchone()
    if(rec2!=None):
           adm=rec2[0]
           exname=rec2[1]
           sub1=rec2[2]
           sub2=rec2[3]
           sub3=rec2[4]
           sub4=rec2[5]
           sub5=rec2[6]
           total=rec2[7]
           per=rec2[8]
           att=rec2[9]
           g=rec2[10]
           rem=rec2[11]
    if(rec1==None and rec2==None):
         print('WRONG ADMISSION NUMBER GIVEN!!!!!!')
    else:
         print('\n\n--------REPORT CARD OF',name,'----------\n\n')      
         print('\nCLASS-',cls,'SECTION-',sec,'\n')
         print('\n------------------------------\n')
         print('\nRESULT OF',exname,'\n')
         print('\n------------------------------\n')
         if(sec=='A'):
             print('\n ENGLISH    : ',sub1)
             print('\n HISTORY    : ',sub2)
             print('\n POL. SC    : ',sub3)
             print('\n ECONOMICS  : ',sub4)
             print('\n GEOGRAPHY  : ',sub5)
             print('\n TOTAL      : ',total)
             print('\n PERCENTAGE : ',per)
             print('\n ATTENDANCE : ',att,'%')
             print('\n GRADE      : ',g)
             print('\n REMAKS     : ',rem)
         elif(sec=='B'):
             print('\n ENGLISH    : ',sub1)
             print('\n ACCOUNTANCY: ',sub2)
             print('\n B.STUDIES  : ',sub3)
             print('\n ECONOMICS  : ',sub4)
             print('\n INFO.PRAC  : ',sub5)
             print('\n TOTAL      : ',total)
             print('\n PERCENTAGE : ',per)
             print('\n ATTENDANCE : ',att,'%')
             print('\n GRADE      : ',g)
             print('\n REMAKS     : ',rem)
         elif(sec=='C'):
              print('\n ENGLISH    : ',sub1)
              print('\n PHYSICS    : ',sub2)
              print('\n COMP.SC    : ',sub3)
              print('\n CHEMISTRY  : ',sub4)
              print('\n MATHEMATICS: ',sub5)
              print('\n TOTAL      : ',total)
              print('\n PERCENTAGE : ',per)
              print('\n ATTENDANCE : ',att,'%')
              print('\n GRADE      : ',g)
              print('\n REMAKS     : ',rem)
         elif(sec=='D'):
              print('\n ENGLISH    : ',sub1)
              print('\n PHYSICS    : ',sub2)
              print('\n BIO.SC    : ',sub3)
              print('\n CHEMISTRY  : ',sub4)
              print('\n MATHEMATICS: ',sub5)
              print('\n TOTAL      : ',total)
              print('\n PERCENTAGE : ',per)
              print('\n ATTENDANCE : ',att,'%')
              print('\n GRADE      : ',g)
              print('\n REMAKS     : ',rem)


def Remove_Record():
    ph=input('\nENTER THE ADMISSION NUMBER TO DELETE:')
    sql='Delete from RESULT where Adm_no=%s'
    value=(ph,)
    try:
        mycur.execute(sql,value)
        mycon.commit()
        print('RECORD DELETED SUCCESSFULLY')
    except:
        mycon.rollback()
        print('UNABLE TO DELETE RECORD!!!')

def Graph():
    ad=int(input('\nENTER THE ADMISSION NUMBER TO SEARCH:'))
    sql1='Select * from result where adm_no=%s'
    value=(ad,)
    mycur.execute(sql1,value)
    T=mycur.fetchone()
    sql2='Select section from student where adm_no=%s';
    mycur.execute(sql2,value)
    s=mycur.fetchone()
    L=[T[2],T[3],T[4],T[5],T[6]]
    sec=s[0]
    if(sec=='A'):
        sub1,sub2,sub3,sub4,sub5='English','History','Pol.Sc','Economics','Geography'
    elif(sec=='B'):
        sub1,sub2,sub3,sub4,sub5='English','Accountancy','B.Studies','Economics','Info.Practices'
    elif(sec=='C'):
        sub1,sub2,sub3,sub4,sub5='English','Physics','Computer Sc.','Chemistry','Mathematics'    
    elif(sec=='D'):
        sub1,sub2,sub3,sub4,sub5='English','Physics','Biology','Chemistry','Mathematics'
    sub=[sub1,sub2,sub3,sub4,sub5]
    clr=('red','green','blue','orange','brown')
    plt.bar(sub,L,color=clr)
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Marks Analysis')
    plt.show()



     
def Close():

    print('\nTHANK YOU FOR USING THE APPLICATION')
    sys.exit()             
             

        

print('-----------WELCOME TO EXAMINATION MODULE  SYSTEM FOR CLASS-XI & XII-------------\n\n')
while(True):
    print('\n\nPRESS 1 TO CREATE A STUDENT PROFILE')
    print('PRESS 2 TO EDIT A STUDENT PROFILE')
    print('PRESS 3 TO DELETE A STUDENT PROFILE')
    print('PRESS 4 FOR MARKS AND ATTENDANCE ENTRY')
    print('PRESS 5 TO GENERATE REPORT CARD')
    print('PRESS 6 TO DELETE MARKS DETAILS')
    print('PRESS 7 TO PRODUCE A GRAPH PERFORMANCE')
    print('PRESS 8 TO CLOSE THE APPLICATION')
    choice=int(input('ENTER YOUR CHOICE : '))
    if(choice==1):
        Student_Profile()
    elif(choice==2):
        Edit_Profile()
    elif(choice==3):
        Remove_Profile()
    elif(choice==4):
        Record_Entry()
    elif(choice==5):
        Report_Card()
    elif(choice==6):
        Remove_Record()
    elif(choice==7):
        Graph()
    elif(choice==8):
        Close()
        
        
    
    
    
        
           
    
















