import pandas as pd
import math
import csv

test1 = pd.read_csv("F1_20190609_165402.txt",header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])
test2 = pd.read_csv("F2_20190609_165402.txt",header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])
test3 = pd.read_csv("F3_20190609_165402.txt",header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])
test4 = pd.read_csv("F4_20190609_165402.txt",header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])
test5 = pd.read_csv("F5_20190609_165803.txt",header=None,sep='^',names=['Timestamp','Count_Microseconds','X','Y','Pressure'])

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
    
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)


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
#std in jerk

#Dataset appending

with open('tpset.csv','a') as d:
    
    
    name=input("Name of the candidate : ")
    age=input("Age of the candidate : ")
    sex=input("Sex of the candidate : ")
    school=input("School or institute : ")
    total=0
    
    grade1=input("Grades last year : ")
    
    if(grade1=='A1'):
        total+=20
    if(grade1=='A2'):
        total+=15
    if(grade1=='B1'):
        total+=13
    if(grade1=='B2'):
        total+=11
    if(grade1=='C1'):
        total+=8
    if(grade1=='C2'):
        total+=7
    if(grade1=='D'):
        total+=3
    if(grade1=='E'):
        total+=1
    grade2=input("Grades before last year : ")
    if(grade2=='A1'):
        total+=20
    if(grade2=='A2'):
        total+=15
    if(grade2=='B1'):
        total+=13
    if(grade2=='B2'):
        total+=11
    if(grade2=='C1'):
        total+=8
    if(grade2=='C2'):
        total+=7
    if(grade2=='D'):
        total+=3
    if(grade2=='E'):
        total+=1
    grade3=input("Grades before two years : ")   
    if(grade3=='A1'):
        total+=20
    if(grade3=='A2'):
        total+=15
    if(grade3=='B1'):
        total+=13
    if(grade3=='B2'):
        total+=11
    if(grade3=='C1'):
        total+=8
    if(grade3=='C2'):
        total+=7
    if(grade3=='D'):
        total+=3
    if(grade3=='E'):
        total+=1
    
    
    
    
    
    #learning_disability=input("Yes or No : ")
    
    if(total<32):
        learning_disability=1
    else:
        learning_disability=0
    
    x=[name,age,sex,school,on_paper_segments_1,in_air_segments_1,entire_time_1,mean_pressure_1,std_deviation_1,time_on_paper_1,time_in_air_1,length_1,velocity_1,acceleration_1,jerk_1,on_paper_segments_2,in_air_segments_2,entire_time_2,mean_pressure_2,std_deviation_2,time_on_paper_2,time_in_air_2,length_2,velocity_2,acceleration_2,jerk_2,on_paper_segments_3,in_air_segments_3,entire_time_3,mean_pressure_3,std_deviation_3,time_on_paper_3,time_in_air_3,length_3,velocity_3,acceleration_3,jerk_3,on_paper_segments_4,in_air_segments_4,entire_time_4,mean_pressure_4,std_deviation_4,time_on_paper_4,time_in_air_4,length_4,velocity_4,acceleration_4,jerk_4,on_paper_segments_5,in_air_segments_5,entire_time_5,mean_pressure_5,std_deviation_5,time_on_paper_5,time_in_air_5,length_5,velocity_5,acceleration_5,jerk_5,grade1,grade2,grade3,learning_disability]
   # x='\n' + name + ',' + age + ',' + sex + ',' + on_paper_segments_1 + ',' + on_paper_segments_2 + ',' + on_paper_segments_3 + ',' + on_paper_segments_4 + ',' +on_paper_segments_5 + ',' + in_air_segments_1 + ',' + in_air_segments_2 + ',' + in_air_segments_3 + ',' + in_air_segments_4 + ',' + in_air_segments_5 + ',' + learning_disability
    writer=csv.writer(d)
    writer.writerow(x)

d.close()
