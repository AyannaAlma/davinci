import numpy as np
import pandas  as pd

dataA = pd.read_csv("C:/Users/Ayanna/stock_A.csv") 
dataB = pd.read_csv("C:/Users/Ayanna/stock_B.csv") 

def profitloss(A,B):
    dif_price_A=A['price'].diff(periods=1)
    priceA=A['price']
    priceB=B['price']
    
    sellingprice=priceA #idon't know if it's true, but let's assume
    costprice=priceB
    profit=0 #initialization
    loss=0

    for i in range(len(dif_price_A)):
        if dif_price_A[i]>0.015:
            #i think i should add M and take B price corresponding to this time, but I had no time to do this 
            sellingprice[i]=priceA[i]
              
        elif dif_price_A[i]<-0.015: 
            sellingprice[i]=priceB[i]
    
        profit=profit+sellingprice[i]-costprice[i]
        loss=loss+costprice[i]-sellingprice[i]
       
    if profit==0 : 
        print("No profit nor Loss") 
    elif profit>0 : 
        print(profit, "Profit") 
    else: 
        print(loss, "Loss") 

profitloss(dataA,dataB)
    
    

    