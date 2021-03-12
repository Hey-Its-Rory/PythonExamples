import json
import urllib.request
from collections import Counter
from FunctionsRoryNorth import *


welcomemessage = ("Hello! Lets Start By Importing some Data")
print(welcomemessage)

#Imports the data and turns it into a series of more helpful things
JSONdata = ReadJSON()
print("Now we need to arrange them. This might take a moment, hold tight!")
DataTup = ArrangeData(JSONdata)
print("Done!")

#Assign the helpful data to individual variables
DataDictionary = DataTup[0]
SP = DataTup[1]

#use counter to get a count for each item
SoldProducts =dict(Counter(DataTup[1]))
SoldNoDoubles = dict(Counter(DataTup[2]))

#sort data into alphabetical order
SP.sort()
StockAlphabetical = dict(Counter(SP))

print ("Now its time to use our data!")
print("First Up we have the item sales in alphabetical order")
ViewAlphabeticalOrder = input("Enter Y to load or just hit ENTER to skip this one").upper()
if ViewAlphabeticalOrder == "Y" :
    print(StockAlphabetical)


#and now i can look through them to find their max and min values since theyre sorted by frequency, I can just take the first and last elements
MinMaxDecide = input("Now for the most sold items, Y to load, N to skip").upper()
if MinMaxDecide == "Y":
    FindMinMax(SoldProducts);
    print("and if we exclude multiple purchases of the same item ---")
    FindMinMax(SoldNoDoubles);

#Here I calculate the average length of each shopping list and populate my prediction with the most sold items.
predictDecide = input("How about my prediction? Y to load").upper()
if predictDecide == "Y":
    FindAverageOrder(DataDictionary,SoldProducts)
#print(SP)
SaleChangeDecide = input("Last One, This is a dictionary of every item and its change since the previous year. Y to load").upper()
if SaleChangeDecide == "Y":
    ChangeOverTime(DataDictionary)
print("Thats All Folks!")












