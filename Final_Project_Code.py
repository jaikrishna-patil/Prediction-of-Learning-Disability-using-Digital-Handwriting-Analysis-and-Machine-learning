#Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.model_selection import GridSearchCV

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier

from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

import warnings
warnings.simplefilter('ignore')


df=pd.read_csv("dataset1.csv")
df = df.dropna()


X=df.drop(["name","age","sex","school","grade1","grade2","grade3","learning_disability"],axis='columns')
Y=df[["learning_disability"]]

np.random.seed(3140)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.35,random_state=3000)



np.random.seed(34)
dt = DecisionTreeClassifier(criterion='gini',max_depth=5)
dt.fit(X_train,Y_train)

dt_accuracy=accuracy_score(Y_test,dt.predict(X_test))


np.random.seed(2)

rf = RandomForestClassifier(n_estimators=45)
rf.fit(X_train, Y_train)
rf_accuracy=accuracy_score(Y_test,rf.predict(X_test))


np.random.seed(2)

ada = AdaBoostClassifier(n_estimators=42)
ada.fit(X_train, Y_train)
ada_accuracy=accuracy_score(Y_test,ada.predict(X_test))




svm2=SVC(kernel='rbf')
svm2.fit(X_train, Y_train)
svm2_accuracy=accuracy_score(Y_test,svm2.predict(X_test))


svm3=SVC(kernel='sigmoid')
svm3.fit(X_train, Y_train)
svm3_accuracy=accuracy_score(Y_test,svm3.predict(X_test))


svm4=SVC(kernel='poly')
svm4.fit(X_train, Y_train)
svm4_accuracy=accuracy_score(Y_test,svm4.predict(X_test))



svc=SVC(kernel="rbf",probability=True)
dt1=DecisionTreeClassifier()
classifiers=[('dt1',dt1),('svc',svc)]
vc=VotingClassifier(estimators=classifiers,voting='soft')
vc.fit(X_train, Y_train)
vc_accuracy=accuracy_score(Y_test,vc.predict(X_test))



import pandas as pd
import math
import csv






#Tkinter
from tkinter import filedialog
from tkinter import *

root2 = Tk()
root2.geometry('1000x1200')
root2.title("Project Details ")

def begin():

    root2.destroy()

label_00 = Label(root2, text="Identifying Learning Disability Through Digital Handwriting Analysis\n\n\n",width=100,font=("bold", 20))
label_00.pack()


label_10 = Label(root2, text="Project by : \n",width=100,font=("bold", 20))
label_10.pack()



label_11 = Label(root2, text="Purva Parab       ::    B150374273\n\n",width=100,font=("bold", 20))
label_11.pack()



label_12 = Label(root2, text="Jaikrishna Patil       ::    B150374274\n\n",width=100,font=("bold", 20))
label_12.pack()


label_13 = Label(root2, text="Akash Sharma       ::    B150374298\n\n",width=100,font=("bold", 20))
label_13.pack()

label_14 = Label(root2, text="Rohit Wagh       ::    B150374320\n\n",width=100,font=("bold", 20))
label_14.pack()

Button(root2, text='Let us Begin',width=100,bg='brown',fg='white',command = begin).pack()

root2.mainloop()


name=''
age=''
school=''
sex=0


root = Tk()
root.geometry('1000x1200')
root.title("Details ")

Name=StringVar()
Age=StringVar()
var = IntVar()
School=StringVar()







def display():

    root.destroy()



def read_file1():
    global test1
    root.file1 =  filedialog.askopenfilename(initialdir = "/",title = "Select file 1",filetypes = (("txt file","*.txt"),("all files","*.*")))
    test1 = pd.read_csv(root.file1,header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])

def read_file2():
    global test2
    root.file2 =  filedialog.askopenfilename(initialdir = "/",title = "Select file 2",filetypes = (("txt file","*.txt"),("all files","*.*")))
    test2 = pd.read_csv(root.file2,header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])

def read_file3():
    global test3
    root.file3 =  filedialog.askopenfilename(initialdir = "/",title = "Select file 3",filetypes = (("txt file","*.txt"),("all files","*.*")))
    test3 = pd.read_csv(root.file3,header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])

def read_file4():
    global test4
    root.file4 =  filedialog.askopenfilename(initialdir = "/",title = "Select file 4",filetypes = (("txt file","*.txt"),("all files","*.*")))
    test4 = pd.read_csv(root.file4,header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])
    
def read_file5():
    global test5
    root.file5 =  filedialog.askopenfilename(initialdir = "/",title = "Select file 5",filetypes = (("txt file","*.txt"),("all files","*.*")))
    test5 = pd.read_csv(root.file5,header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])

    
    Timestamp1 = test1['Timestamp'].values
    Count_Microseconds1 = test1['Count_Microseconds'].values
    X1 = test1['X'].values
    Y1 = test1['Y'].values
    Pressure1 = test1['Pressure'].values

    Timestamp2 = test2['Timestamp'].values
    Count_Microseconds2 = test2['Count_Microseconds'].values
    X2 = test2['X'].values
    Y2 = test2['Y'].values
    Pressure2 = test2['Pressure'].values


    Timestamp3 = test3['Timestamp'].values
    Count_Microseconds3 = test3['Count_Microseconds'].values
    X3 = test3['X'].values
    Y3 = test3['Y'].values
    Pressure3 = test3['Pressure'].values


    Timestamp4 = test4['Timestamp'].values
    Count_Microseconds4 = test4['Count_Microseconds'].values
    X4 = test4['X'].values
    Y4 = test4['Y'].values
    Pressure4 = test4['Pressure'].values


    Timestamp5 = test5['Timestamp'].values
    Count_Microseconds5 = test5['Count_Microseconds'].values
    X5 = test5['X'].values
    Y5 = test5['Y'].values
    Pressure5 = test5['Pressure'].values


    #0. Total number of segments

    count1=0
    count2=0
    count3=0
    count4=0
    count5=0

    for i in Pressure1:
        count1=count1+1
        
    for i in Pressure2:
        count2=count2+1

    for i in Pressure3:
        count3=count3+1
        
    for i in Pressure4:
        count4=count4+1
        
    for i in Pressure5:
        count5=count5+1
        


    #1. Number of on paper segments

    on_paper_segments_1=0
    on_paper_segments_2=0
    on_paper_segments_3=0
    on_paper_segments_4=0
    on_paper_segments_5=0

    for i in Pressure1:
        
        if(i==0):
            continue
        on_paper_segments_1=on_paper_segments_1+1
        
    for i in Pressure2:
        
        if(i==0):
            continue
        on_paper_segments_2=on_paper_segments_2+1

    for i in Pressure3:
        
        if(i==0):
            continue
        on_paper_segments_3=on_paper_segments_3+1
        
    for i in Pressure4:
        
        if(i==0):
            continue
        on_paper_segments_4=on_paper_segments_4+1
        
    for i in Pressure5:
        
        if(i==0):
            continue
        on_paper_segments_5=on_paper_segments_5+1
            
    #2. Number of in air segments

    in_air_segments_1=0
    in_air_segments_2=0
    in_air_segments_3=0
    in_air_segments_4=0
    in_air_segments_5=0

    for i in Pressure1:
        
        if(i!=0):
            continue
        in_air_segments_1=in_air_segments_1+1
        
    for i in Pressure2:
        
        if(i!=0):
            continue
        in_air_segments_2=in_air_segments_2+1
        
    for i in Pressure3:
        
        if(i!=0):
            continue
        in_air_segments_3=in_air_segments_3+1
        
    for i in Pressure4:
        
        if(i!=0):
            continue
        in_air_segments_4=in_air_segments_4+1
        
    for i in Pressure5:
        
        if(i!=0):
            continue
        in_air_segments_5=in_air_segments_5+1
        
        
    #3 Entire time in microseconds

    first=0
    last=0

    entire_time_1=0
    entire_time_2=0
    entire_time_3=0
    entire_time_4=0
    entire_time_5=0

    first=Count_Microseconds1[0]
    last=Count_Microseconds1[-1]

    entire_time_1=last-first

    #print(entire_time_1)
        
    first=Count_Microseconds2[0]
    last=Count_Microseconds2[-1]

    entire_time_2=last-first


    first=Count_Microseconds3[0]
    last=Count_Microseconds3[-1]

    entire_time_3=last-first


    first=Count_Microseconds4[0]
    last=Count_Microseconds4[-1]

    entire_time_4=last-first

    first=Count_Microseconds5[0]
    last=Count_Microseconds5[-1]

    entire_time_5=last-first



    #4. Mean pressure applied on a pen


    mean_pressure_1=0
    mean_pressure_2=0
    mean_pressure_3=0
    mean_pressure_4=0
    mean_pressure_5=0

    sum=0
    for i in Pressure1:
        
        if(i==0):
            continue
        sum=sum+i;
        
    mean_pressure_1=sum/on_paper_segments_1

    sum=0
    for i in Pressure2:
        
        if(i==0):
            continue
        sum=sum+i;
        
    mean_pressure_2=sum/on_paper_segments_2


    sum=0
    for i in Pressure3:
        
        if(i==0):
            continue
        sum=sum+i;
        
    mean_pressure_3=sum/on_paper_segments_3


    sum=0
    for i in Pressure4:
        
        if(i==0):
            continue
        sum=sum+i;
        
    mean_pressure_4=sum/on_paper_segments_4


    sum=0
    for i in Pressure5:
        
        if(i==0):
            continue
        sum=sum+i;
        
    mean_pressure_5=sum/on_paper_segments_5

    #5. Std deviation on pressure


    std_deviation_1=0
    std_deviation_2=0
    std_deviation_3=0
    std_deviation_4=0
    std_deviation_5=0

    sum=0
    for i in Pressure1:
        
        if(i==0):
            continue
        sum=sum+((i-mean_pressure_1)**2);
        
    std_deviation_1=math.sqrt(sum/on_paper_segments_1)


    sum=0
    for i in Pressure2:
        
        if(i==0):
            continue
        sum=sum+((i-mean_pressure_2)**2);
        
    std_deviation_2=math.sqrt(sum/on_paper_segments_2)


    sum=0
    for i in Pressure3:
        
        if(i==0):
            continue
        sum=sum+((i-mean_pressure_3)**2);
        
    std_deviation_3=math.sqrt(sum/on_paper_segments_3)



    sum=0
    for i in Pressure4:
        
        if(i==0):
            continue
        sum=sum+((i-mean_pressure_4)**2);
        
    std_deviation_4=math.sqrt(sum/on_paper_segments_4)



    sum=0
    for i in Pressure5:
        
        if(i==0):
            continue
        sum=sum+((i-mean_pressure_5)**2);
        
    std_deviation_5=math.sqrt(sum/on_paper_segments_5)


    #6. Time spent on paper

    time_on_paper_1=0
    time_on_paper_2=0
    time_on_paper_3=0
    time_on_paper_4=0
    time_on_paper_5=0



    i=0
    sum=0
    while i<count1:
        
        if Pressure1[i]==0:
            i=i+1
            continue
        
        first=Count_Microseconds1[i]
        last=0
        
        while Pressure1[i]!=0:
            
            last=Count_Microseconds1[i]
            i=i+1
            
        sum=sum+(last-first)
        i=i+1
        
    time_on_paper_1=sum
    #print(sum)    
          
    i=0
    sum=0
    while i<count2:
        
        if Pressure2[i]==0:
            i=i+1
            continue
        
        first=Count_Microseconds2[i]
        last=0
        
        while Pressure2[i]!=0:
            
            last=Count_Microseconds2[i]
            i=i+1
            
        sum=sum+(last-first)
        i=i+1
        
    time_on_paper_2=sum


    i=0
    sum=0
    while i<count3:
        
        if Pressure3[i]==0:
            i=i+1
            continue
        
        first=Count_Microseconds3[i]
        last=0
        
        while Pressure3[i]!=0:
            
            last=Count_Microseconds3[i]
            i=i+1
            
        sum=sum+(last-first)
        i=i+1
        
    time_on_paper_3=sum


    i=0
    sum=0
    while i<count4:
        
        if Pressure4[i]==0:
            i=i+1
            continue
        
        first=Count_Microseconds4[i]
        last=0
        
        while Pressure4[i]!=0:
            
            last=Count_Microseconds4[i]
            i=i+1
            
        sum=sum+(last-first)
        i=i+1
        
    time_on_paper_4=sum




    i=0
    sum=0
    while i<count5:
        
        if Pressure5[i]==0:
            i=i+1
            continue
        
        first=Count_Microseconds5[i]
        last=0
        
        while Pressure5[i]!=0:
            
            last=Count_Microseconds5[i]
            i=i+1
            
        sum=sum+(last-first)
        i=i+1
        
    time_on_paper_5=sum


    #7. Time spent in air

    time_in_air_1=entire_time_1-time_on_paper_1
    time_in_air_2=entire_time_2-time_on_paper_2
    time_in_air_3=entire_time_3-time_on_paper_3
    time_in_air_4=entire_time_4-time_on_paper_4
    time_in_air_5=entire_time_5-time_on_paper_5

    #8. Total distance / length

    length_1=0
    length_2=0
    length_3=0
    length_4=0
    length_5=0

    i=0
    sum=0
    while i<count1-1:
        
        if Pressure1[i]==0:
            i=i+1
            continue
        
        while Pressure1[i]!=0:
            
            sum=sum+(math.sqrt(((X1[i+1]-X1[i])**2) + ((Y1[i+1]-[Y1[i]])**2)))
            i=i+1
        
    length_1=sum
    #print(sum) 

    i=0
    sum=0
    while i<count2-1:
        
        if Pressure2[i]==0:
            i=i+1
            continue
        
        while Pressure2[i]!=0:
            
            sum=sum+(math.sqrt(((X2[i+1]-X2[i])**2) + ((Y2[i+1]-[Y2[i]])**2)))
            i=i+1
        
    length_2=sum


    i=0
    sum=0
    while i<count3-1:
        
        if Pressure3[i]==0:
            i=i+1
            continue
        
        while Pressure3[i]!=0:
            
            sum=sum+(math.sqrt(((X3[i+1]-X3[i])**2) + ((Y3[i+1]-[Y3[i]])**2)))
            i=i+1
        
    length_3=sum


    i=0
    sum=0
    while i<count4-1:
        
        if Pressure4[i]==0:
            i=i+1
            continue
        
        while Pressure4[i]!=0:
            
            sum=sum+(math.sqrt(((X4[i+1]-X4[i])**2) + ((Y4[i+1]-[Y4[i]])**2)))
            i=i+1
        
    length_4=sum


    i=0
    sum=0
    while i<count5-1:
        
        if Pressure5[i]==0:
            i=i+1
            continue
        
        while Pressure5[i]!=0:
            
            sum=sum+(math.sqrt(((X5[i+1]-X5[i])**2) + ((Y5[i+1]-[Y5[i]])**2)))
            i=i+1
        
    length_5=sum

    #std in distance

    #9. aVERAGE VELOCITY OF PEN

    velocity_1=0
    velocity_2=0
    velocity_3=0
    velocity_4=0
    velocity_5=0


    velocity_1=length_1/entire_time_1
    velocity_2=length_2/entire_time_2
    velocity_3=length_3/entire_time_3
    velocity_4=length_4/entire_time_4
    velocity_5=length_5/entire_time_5

    #std in velocity

    #10. Average accelration

    acceleration_1=0
    acceleration_2=0
    acceleration_3=0
    acceleration_4=0
    acceleration_5=0

    acceleration_1=velocity_1/entire_time_1
    acceleration_2=velocity_2/entire_time_2
    acceleration_3=velocity_3/entire_time_3
    acceleration_4=velocity_4/entire_time_4
    acceleration_5=velocity_5/entire_time_5


    #std in accleration

    #11. Jerk

    jerk_1=acceleration_1/entire_time_1
    jerk_2=acceleration_2/entire_time_2
    jerk_3=acceleration_3/entire_time_3
    jerk_4=acceleration_4/entire_time_4
    jerk_5=acceleration_5/entire_time_5


    global name, age, sex, school
    name=Name.get()
    age=Age.get()
    sex=var.get()
    if sex==1:
        sex='M'
    if sex==2:
        sex='F'
    school=School.get()
    with open('inputset.csv','w',newline='') as d:
    
        y=['name','age','sex','school','on_paper_segments_1','in_air_segments_1','entire_time_1','mean_pressure_1','std_deviation_1','time_on_paper_1','time_in_air_1','length_1','velocity_1','acceleration_1','jerk_1','on_paper_segments_2','in_air_segments_2','entire_time_2','mean_pressure_2','std_deviation_2','time_on_paper_2','time_in_air_2','length_2','velocity_2','acceleration_2','jerk_2','on_paper_segments_3','in_air_segments_3','entire_time_3','mean_pressure_3','std_deviation_3','time_on_paper_3','time_in_air_3','length_3','velocity_3','acceleration_3','jerk_3','on_paper_segments_4','in_air_segments_4','entire_time_4','mean_pressure_4','std_deviation_4','time_on_paper_4','time_in_air_4','length_4','velocity_4','acceleration_4','jerk_4','on_paper_segments_5','in_air_segments_5','entire_time_5','mean_pressure_5','std_deviation_5','time_on_paper_5','time_in_air_5','length_5','velocity_5','acceleration_5','jerk_5']
        x=[name,age,sex,school,on_paper_segments_1,in_air_segments_1,entire_time_1,mean_pressure_1,std_deviation_1,time_on_paper_1,time_in_air_1,length_1,velocity_1,acceleration_1,jerk_1,on_paper_segments_2,in_air_segments_2,entire_time_2,mean_pressure_2,std_deviation_2,time_on_paper_2,time_in_air_2,length_2,velocity_2,acceleration_2,jerk_2,on_paper_segments_3,in_air_segments_3,entire_time_3,mean_pressure_3,std_deviation_3,time_on_paper_3,time_in_air_3,length_3,velocity_3,acceleration_3,jerk_3,on_paper_segments_4,in_air_segments_4,entire_time_4,mean_pressure_4,std_deviation_4,time_on_paper_4,time_in_air_4,length_4,velocity_4,acceleration_4,jerk_4,on_paper_segments_5,in_air_segments_5,entire_time_5,mean_pressure_5,std_deviation_5,time_on_paper_5,time_in_air_5,length_5,velocity_5,acceleration_5,jerk_5]
        writer=csv.writer(d,delimiter=',')
        writer.writerow(y)
        writer.writerow(x)

    d.close()


label_0 = Label(root, text="Details of person",width=20,font=("bold", 20))
label_0.place(x=300,y=53)


label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=250,y=130)

entry_1 = Entry(root,textvar=Name)
entry_1.place(x=450,y=130)

label_2 = Label(root, text="Age",width=20,font=("bold", 10))
label_2.place(x=250,y=180)

entry_2 = Entry(root,textvar=Age)
entry_2.place(x=450,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=250,y=230)
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=450,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=550,y=230)

label_4 = Label(root, text="School",width=20,font=("bold", 10))
label_4.place(x=250,y=280)

entry_4 = Entry(root,textvar=School)
entry_4.place(x=450,y=280)


Button(root, text='Upload file1',width=20,bg='brown',fg='white',command = read_file1).place(x=90,y=330)
Button(root, text='Upload file2',width=20,bg='brown',fg='white',command = read_file2).place(x=290,y=330)
Button(root, text='Upload file3',width=20,bg='brown',fg='white',command = read_file3).place(x=490,y=330)
Button(root, text='Upload file4',width=20,bg='brown',fg='white',command = read_file4).place(x=690,y=330)
Button(root, text='Upload file5',width=20,bg='brown',fg='white',command = read_file5).place(x=870,y=330)



Button(root, text='Submit',width=20,bg='brown',fg='white',command = display).place(x=250,y=430)




root.mainloop()

inp=pd.read_csv("inputset.csv")
inp = inp.dropna()

Xinp=inp.drop(["name","age","sex","school"],axis='columns')

max_accuracy=max([dt_accuracy,rf_accuracy,ada_accuracy,svm2_accuracy,svm3_accuracy,svm4_accuracy,vc_accuracy])


if(max_accuracy==rf_accuracy):
    output=rf.predict(Xinp)

if(max_accuracy==ada_accuracy):
    output=ada.predict(Xinp)

if(max_accuracy==dt_accuracy):
    output=dt.predict(Xinp)
    
if(max_accuracy==svm2_accuracy):
    output=svm2.predict(Xinp)
    
if(max_accuracy==svm3_accuracy):
    output=svm2.predict(Xinp)

if(max_accuracy==svm4_accuracy):
    output=svm4.predict(Xinp)
    
if(max_accuracy==vc_accuracy):
    output=vc.predict(Xinp)




if(output==0):
    output=name+' is not likely to have a learning disability'

else:
    output=name+ ' is Likely to have a learning disability'

root1 = Tk()
root1.geometry('1000x1000')
root1.title("Result ")



label_4 = Label(root1, text=output,bd=1,relief="solid",width=100,height=50,font="Times 32")
label_4.pack()

root1.mainloop()


