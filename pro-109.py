import csv
import statistics
import pandas as p

data = p.read_csv("studentPerformance.csv")

dataList = data["reading score"].to_list()

n = len(dataList)


mean = statistics.mean(dataList)
print("The Mean Is -->",mean)
print("-------------------------------------------------------------------------")


mode = statistics.mode(dataList)
print("The Mode Is -->",mode)
print("-------------------------------------------------------------------------")


median = statistics.median(dataList)
print("The Median Is -->",median)
print("-------------------------------------------------------------------------")


std = statistics.stdev(dataList)
print("The Standard Divison Is -->",std)
print("-------------------------------------------------------------------------")


stdStart1 , stdEnd1 = mean - std , mean + std
stdStart2 , stdEnd2 = mean - (2 * std) , mean + (2 * std)
stdStart3 , stdEnd3 = mean - (3 * std) , mean + (3 * std)

listOfStd1 = [result for result in dataList if result > stdStart1 and result < stdEnd1]
b1 = len(listOfStd1)
p1 = (b1 * 100)/n
 
print("Percentage of Data lies within Std Dev 1 --> " , p1)
print("-------------------------------------------------------------------------")

listOfStd2 = [result for result in dataList if result > stdStart2 and result < stdEnd2]
b2 = len(listOfStd2)
p2 = (b2 * 100)/n
 
print("Percentage of Data lies within Std Dev 2 --> " , p2)
print("-------------------------------------------------------------------------")

listOfStd3 = [result for result in dataList if result > stdStart3 and result < stdEnd3]
b3 = len(listOfStd3)
p3 = (b3 * 100)/n
 
print("Percentage of Data lies within Std Dev 3 --> " , p3)
print("-------------------------------------------------------------------------")











