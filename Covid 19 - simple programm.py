#Kotsarapoglou Iason-Eirinaios icsd14092
import urllib.request
from urllib.parse import urlparse
import re
import csv

class countries:#dimiourgoume mia klash countries kai ftiaxnoume enan default contructor pou exei ena onoma(ths xwras) kai 2 listes(mia gia tis politeies kai mia gia ta krousmata ana hmera)
    def __init__(self):
        self.name=''
        self.departments=[]
        self.victims=[]

    def setName(self,name):#ftiaxnoume set methodous gia ta stoixeia mas
        self.name=name

    def add_department(self,department):#me to append sthn ousia prosthetw kathe fora ena department sthn lista(auto pou prosthetw to dinw ws orisma)
        self.departments.append(department)

    def setVictims(self,victim,flag):#sthn periptwsh pou to flag einai 0 einai opws kai sthn panw periptwsh dld prosthetw kanonika ta krousmata an hmeromhnia
        if (flag==0):
            self.victims.append(victim)
        else:#einai h periptwsh pou h xwra uparxei hdh kai thelw na prosthesw ta krousmata ths kainourias politeias se authn thn xwra
            self.victims[flag]=int(self.victims[flag])+int(victim)#kanw cast gia int gt se allh periptwsh tha mou vgazei lathos (px 1+0=10)
        
    def getName(self):#exw epishs getters gia ola ta stoixeia sta departments kai sta victims epistrefw lista
        return self.name
    
    def getDepartments(self):
        return self.departments
    
    def getVictims(self):
        return self.victims
    
tempname=''#einai metavlhtes pou tha mou xreiastoun gia proswrinh apothikeush
templist=[]
templist1=[]
templist2=[]
test=countries()
object_list=[]#einai h lista me ola ta object countries
flag=0
#pairnw to url csv arxeio kai to pernaw se mia lista ( thn data) me to append
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
webpage = urllib.request.urlopen(url)
datareader = csv.reader(webpage.read().decode('utf-8').splitlines())
data = []
for row in datareader:
    data.append(row)
    
size=len(data)#me ton len pairnw to megethos ths listas
for j in range (0,size):#metatrepw kathe seira ths listas se string kai meta to kathe ena string se mia lista 
    str1=','.join(data[j])#etsi exw gia kathe xwra mia lista px to 1o stoixeio ths listas new tha einai me thn seira keno(den exei politeua),onoma xwras,suntetagmenes kai meta ola ta krousmata ana hmera
    new=str1.split(",")
    new.pop(2)#afairw tis suntetagmenes
    new.pop(2)
    size=len(object_list)
    for b in range (0,size):#elegxo an h xwra pouthelw na prosthesw(new[0]) upraxei hdh sthn lista mou
        if (object_list[b].getName()==new[1]):
            object_list[b].add_department(new[0])#an nai prosthetw to department sthn lista
            for i in range (2,len(new)):
                object_list[b].setVictims(new[i],i-2)# kai prosthetw kai ta krousmata sta hdh uparxwn (einai i-2 ) gia na xekinhsei apo 0
            flag=1 #kanw to flag 1 etsi wste na mhn ftiaxw neo antikeimeno
            break
        
    if (flag==0): #an den ginei ena tote ftiaxnw antikeimeno kalw ta set etsi wste na dwse tis times pou thelw kai kallo thn append kai prosthetw to antikeimeno sthn lista       
        x=countries()
        x.setName(new[1])
        x.add_department(new[0])
        nI=len(new)
        for i in range (2,nI):
            x.setVictims(new[i],0)
        object_list.append(x)
    flag=0 #xanakanw to flag 0 se periptwsh pou eixe ginei 1

for k in range (0,len(object_list)):#tis xwres pou eixan provlhma me ta 2 eisagwgika tis allaxa me to xeri statika
    if (object_list[k].getName()== "Korea"):
        object_list[k].setName("Korea,South")
        object_list[k].getVictims().pop(0)
    if (object_list[k].getName()== " Sint Eustatius and Saba"):
        object_list[k].getVictims().pop(0)            
    if (object_list[k].getName()== "Netherlands"):
        object_list[k].add_department("Bonaire, Sint Eustatius and Saba")
        object_list[k].getDepartments().pop(3)

print("Welcome to the Covid-19 app Choose from the options bellow : ")#emfanizw ena menu epilogwn
print("1 Display how many people were infected from the virus for a specific country ")
print("2 Display all the countries and their cases for a specific day ")
print("3 Display the country that has the more cases today ")
answer=int(input())#diavazw thn apanthsh
flag=0#xrhsimopoiw to flag gia na dw se periptwsh pou kati den vrethei kai na ektupwse munhma lathous
if (answer==1):
    print("Please write down the name of the country that you want the results")
    country=input()#diavazw to onoma ths xwras kai psaxnw sthn lista me ta antikeiena na vrw an uparxei( me to getname)
    for i in range (0,len(object_list)):
        if (country==object_list[i].getName()):
            templist=list(map(int,object_list[i].getVictims()))#an uparxei tote apothikevw se mia proxeirh lista olhn lista me ta krousmata alla se morfh int
            print("The total number of people that were infected from the virus is : ",max(templist)) #me thn max pernw kai ektupwnw to megalutero stoixeio
            flag=1
            break
    if (flag==0):
        print("The country that you insert doesnt exist. Try again next time! ")
elif (answer==2):#diavazw thn hmeromhnia 
    print("Please write down the date (mm/dd/yy) that you want to see the results : ")
    date=input()#to antikeimeno sthn thesh 1 ths listas einai auto me ta dates opote psaxnw mono ekei
    print(object_list[0].getVictims()[5])
    for i in range (0,len(object_list[0].getVictims())):
        if (date==(object_list[0].getVictims())[i]):#an vrw hmeromhnia pou tairiazei tote paw apo to 2o stoixeio kai ektupwnw tis xwres kai ta krousmata
            for j in range (1,len(object_list)):
                print(object_list[j].getName())
                print((object_list[j].getVictims())[i])
                flag=1
    if (flag==0):
        print("The date that you insert doesnt exist. Try again next time! ")
elif (answer==3):
    max1=max(list(map(int,object_list[1].getVictims())))#pairnw to megisto stoixeio tou prwtou antikeimenou ( se int)
    for i in range (2,len(object_list)):
        if (max(list(map(int,object_list[i].getVictims())))>max1):#kai psaxnw se olh thn upoloiph lista an uparxei kapoio megalutero
            max1=max(list(map(int,object_list[i].getVictims())))
            tempname=object_list[i].getName()#apothikevw proswrina to onoma ths xwras
    print("The country with the most cases today is : ",tempname," and the number is : ",max1)# ektupwnw to mmax
else:
    print("You gave Wrong answer.Please try again the next time with the write values")
