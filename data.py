import pandas as pd 
import statistics
import csv
df = pd.read_csv("data.csv")
mathlist = df["math score"].to_list()
writinglist = df["writing score"].to_list()

mathmean = statistics.mean(mathlist)
writingmean = statistics.mean(writinglist)
mathmedian = statistics.median(mathlist)
writingmedian = statistics.median(writinglist) 
mathmode = statistics.mode(mathlist)
writingmode = statistics.mode(writinglist)

print("Mean, Median, Mode Of Maths Score Is: {}, {}, {} respectively".format(mathmean, mathmedian, mathmode))
print("Mean, Median, Mode of Writing Score Is:- {}, {}, {} respectively".format(writingmean, writingmedian, writingmode))

mathstdDev = statistics.stdev(mathlist)
writingstdDev = statistics.stdev(writinglist)

math1stdDevStart, math1stdDevEnd = mathmean - mathstdDev, mathmean + mathstdDev
math2stdDevStart, math2stdDevEnd = mathmean - (2*mathstdDev), mathmean + (2*mathstdDev)
math3stdDevStart, math3stdDevEnd = mathmean - (3*mathstdDev), mathmean + (3*mathstdDev)

writing1stdDevStart, writing1stdDevEnd = writingmean - writingstdDev, writingmean + writingstdDev
writing2stdDevStart, writing2stdDevEnd = writingmean - (2*writingstdDev), writingmean + (2*writingstdDev)
writing3stdDevStart, writing3stdDevEnd = writingmean - (3*writingstdDev), writingmean + (3*writingstdDev)

mathDataWithin1std = [result for result in mathlist if result > math1stdDevStart and result < math1stdDevEnd]
mathDataWithin2std = [result for result in mathlist if result > math2stdDevStart and result < math2stdDevEnd]
mathDataWithin3std = [result for result in mathlist if result > math3stdDevStart and result < math3stdDevEnd]

writingDataWithin1std = [result for result in writinglist if result > writing1stdDevStart and writing1stdDevEnd]
writingDataWithin2std = [result for result in writinglist if result > writing2stdDevStart and writing2stdDevEnd]
writingDataWithin3std = [result for result in writinglist if result > writing3stdDevStart and writing3stdDevEnd]

print("{} % Of Maths Score lies within 1st Standard Deviation".format(len(mathDataWithin1std)*100/len(mathlist)))
print("{} % Of Maths Score lies within 2nd Standard Deviation".format(len(mathDataWithin2std)*100/len(mathlist)))
print("{} % Of Maths Score lies within 3rd Standard Deviation".format(len(mathDataWithin3std)*100/len(mathlist)))
print("{} % Of Writing Score lies within 1st Standard Deviation".format(len(writingDataWithin1std)*100/len(writinglist)))
print("{} % Of Writing Score lies within 2nd Standard Deviation".format(len(writingDataWithin2std)*100/len(writinglist)))
print("{} % Of Writing Score lies within 3rd Standard Deviation".format(len(writingDataWithin3std)*100/len(writinglist)))