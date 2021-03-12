import json
import urllib.request
from collections import Counter

def ReadJSON():
    #getsjson from url
    print("Loading Data Please Wait")
    response = urllib.request.urlopen("https://triadicdash.com/randomdata/producedata")
    data = json.loads(response.read())
    return data
   
def ArrangeData(data):
    print("Arranging Data")
    DictofOrders = {}
    SoldProduct = []
    OrderNoDoubles = []
    DataList = data.split("&")
    for i in DataList:
        i = i.lower()
        thisOrder = i.split(",")
        NumCut = thisOrder[-1].split(" ")
        thisOrder.remove(thisOrder[-1])
        Date = str(NumCut[0])
        for x in thisOrder:
            SoldProduct.append(x)
        OrderLine = []
        for v in thisOrder:
            if v not in OrderLine:
                OrderLine.append(v)
            else:
                continue
        for v in OrderLine:
                OrderNoDoubles.append(v)
            
        
        DictofOrders[Date] = thisOrder

     
       
    
    print("Data Arraged -")

    return DictofOrders,SoldProduct,OrderNoDoubles

def FindMinMax(CountedDict):
    maxitem = list(CountedDict.keys())[0]
    minitem = list(CountedDict.keys())[-1]
    maxval = CountedDict.get(maxitem)
    minval = CountedDict.get(minitem)
    print("The Most popular item in the data is ", maxitem, " which sold ", maxval)
    print("The Least popular item in the data is ", minitem, " which sold ", minval)

def FindAverageOrder(Ordrlst,mostSold):

    #finds the average length of order
    lengthtotal = 0
    Tick = 0
    numberoflists = len(Ordrlst.values())
    for list in Ordrlst.values():
        x = len(list)
        lengthtotal += x
    lengthaverage = lengthtotal//numberoflists
    print("The average order contains ", lengthaverage, " items")
    Average = []
    count = 0
    while count <lengthaverage:
        for i in mostSold.keys():
            Average.append(i)
            count += 1
    Average.sort()
    print(Average)

        
def ChangeOverTime(x):
  
    ThisYear = {}
    LastYear = {}
    ThisYearsSales = []
    LastYearsSales = []
    SaleDifferenceUP = []
    SaleDifferenceDOWN = []
    NoDiff = []
    FinalIncreases = {}
    FinalDecreases = {}

 
    
    for key,value in x.items():
        if "2021" in key:
            ThisYear[key] = value
            for v in value:
                ThisYearsSales.append(v)
        else:
            LastYear[key] = value
            for v in value:
                LastYearsSales.append(v)

        
    
    ThisYearsSales.sort()
    LastYearsSales.sort()
    SalesThisYear = dict(Counter(ThisYearsSales))
    SalesLastYear = dict(Counter(LastYearsSales))
    for key,val in SalesThisYear.items():
        for k,v in SalesLastYear.items():
            if val > v:
                diffUP = val - v
                if k not in SaleDifferenceUP:
                    SaleDifferenceUP.append(k)
                    FinalIncreases[k] = diffUP
            if val < v:
                diffDOWN = v - val
                if k not in SaleDifferenceDOWN:
                    SaleDifferenceDOWN.append(k)
                    FinalDecreases[k] = diffDOWN
            if val == v:
                if k not in NoDiff:
                    NoDiff.append(k)
                    print(k, "has stayed consistent")

    IncreaseTup = [(k,v) for k,v in FinalIncreases.items()]
    IncreaseTup.sort(key=lambda x:x[1],reverse=True)

    DecreaseTup = [(k,v) for k,v in FinalDecreases.items()]
    DecreaseTup.sort(key=lambda x:x[1],reverse=True)

    i = 0
    print("The Following have had the most increase in sales since last year: --")
    while i < 5:
            firstelement = IncreaseTup[i]
            print(firstelement[0], " sales have gone up by ", firstelement[1])
            i +=1
    i=0
    print("The Following have had the most decrease in sales since last year: --")
    while i < 5:
            firstelement = DecreaseTup[i]
            print(firstelement[0], " sales have gone down by ", firstelement[1])
            i +=1



   
                    
   



                

            



    
