# censusTxt = open("D:\\Akash\\2018ElectionPrediction\\census.txt", 'r')
# censusData=censusTxt.readlines()
# censusTxt.close()
# 
# truncCensusData = []
# censusTxt = open("D:\\Akash\\2018ElectionPrediction\\newCensus.txt", 'w')
# for line in censusData:
#     if (int(line[:4]) >= 2000 and int(line[:4]) % 2 == 0):
#         censusTxt.write(line)
# censusTxt.close()
# 
# class State:
#     def __init__(self, state, year):
#         self.state = state
#         self.year = year
#     white = 0
#     black = 0
#     native = 0
#     asian = 0
#     hispanic = 0
#     male = 0
#     female = 0
#     zero = 0
#     oneToFour = 0
#     fiveToNine = 0
#     tenToFourteen = 0
#     fifteenTo19 = 0
#     twentyto24 = 0
#     twenty5to29 = 0
#     thirtyto34 = 0
#     thirty5to39 = 0
#     fortyto44 = 0
#     forty5to49 = 0
#     fiftyto54 = 0
#     fifty5to59 = 0
#     sixtyto64 = 0
#     sixty5to69 = 0
#     seventyto74 = 0
#     seventy5to79 = 0
#     eightyto84 = 0
#     eighty5plus = 0
# 
# 
# def toString(stateData):
#     return stateData.state + ", " + str(stateData.year) + ", " + str(stateData.white) + ", " + str(stateData.black) + ", " + str(stateData.native) + ", " + str(stateData.asian) + ", " + str(stateData.hispanic) + ", " + str(stateData.male) + ", " + str(stateData.female) + ", " + str(stateData.zero)+ ", " + str(stateData.oneToFour) + ", " + str(stateData.fiveToNine) + ", " + str(stateData.tenToFourteen) + ", " + str(stateData.fifteenTo19)    + ", " + str(stateData.twentyto24) + ", " + str(stateData.twenty5to29) + ", " + str(stateData.thirtyto34) + ", " + str(stateData.thirty5to39)   + ", " + str(stateData.fortyto44) + ", " + str(stateData.forty5to49) + ", " + str(stateData.fiftyto54) + ", " + str(stateData.fifty5to59)   + ", " + str(stateData.sixtyto64) + ", " + str(stateData.sixty5to69) + ", " + str(stateData.seventyto74) + ", " + str(stateData.seventy5to79)    + ", " + str(stateData.eightyto84) + ", " + str(stateData.eighty5plus) + "\n"
# 
# 
# 
# 
# stateDict = {}
# 
# censusTxt = open("C:\\Akash\\2018ElectionPrediction\\newCensus.txt", 'r')
# censusData=censusTxt.readlines()
# censusTxt.close()
# 
# censusTxt = open("C:\\Akash\\2018ElectionPrediction\\censusData.csv", 'w')
# 
# censusTxt.write("state, year, white, black, native, asian, hispanic, male, female, 0, 1-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80-84, 85+\n")
# 
# for line in censusData:
#     currStateYear = None
#     pop = int(line[18:])
#     if not line[:6] in stateDict:
#         stateDict[line[:6]] = State(line[4:6], int(line[:4]))
#     currStateYear = stateDict[line[:6]]
#     
#     if line[14] == "0" and line[13] == "1":
#         currStateYear.white+= pop
#     elif line[14] == "0" and line[13] == "2":
#         currStateYear.black+= pop
#     elif line[14] == "0" and line[13] == "3":
#         currStateYear.native+= pop
#     elif line[14] == "0" and line[13] == "4":
#         currStateYear.asian+= pop
#     elif line[14] == "1":
#         currStateYear.hispanic+= pop
#     
#     if line[15] == "1":
#         currStateYear.male+= pop
#     else:
#         currStateYear.female+= pop
#     
#     if line[16:18] == "00":
#         currStateYear.zero += pop
#     elif line[16:18] == "01":
#         currStateYear.oneToFour += pop
#     elif line[16:18] == "02":
#         currStateYear.fiveToNine += pop
#     elif line[16:18] == "03":
#         currStateYear.tenToFourteen += pop
#     elif line[16:18] == "04":
#         currStateYear.fifteenTo19 += pop
#     elif line[16:18] == "05":
#         currStateYear.twentyto24 += pop
#     elif line[16:18] == "06":
#         currStateYear.twenty5to29 += pop
#     elif line[16:18] == "07":
#         currStateYear.thirtyto34 += pop
#     elif line[16:18] == "08":
#         currStateYear.thirty5to39 += pop
#     elif line[16:18] == "09":
#         currStateYear.fortyto44 += pop
#     elif line[16:18] == "10":
#         currStateYear.forty5to49 += pop
#     elif line[16:18] == "11":
#         currStateYear.fiftyto54 += pop
#     elif line[16:18] == "12":
#         currStateYear.fifty5to59 += pop
#     elif line[16:18] == "13":
#         currStateYear.sixtyto64 += pop
#     elif line[16:18] == "14":
#         currStateYear.sixty5to69 += pop
#     elif line[16:18] == "15":
#         currStateYear.seventyto74 += pop
#     elif line[16:18] == "16":
#         currStateYear.seventy5to79 += pop
#     elif line[16:18] == "17":
#         currStateYear.eightyto84 += pop
#     elif line[16:18] == "18":
#         currStateYear.eighty5plus += pop
# 
# for i in stateDict:
#     censusTxt.write(toString(stateDict[i]))
# 
# censusTxt.close()

import pandas as pd

left = pd.read_csv('C:\\Akash\\2018ElectionPrediction\\Training_Data.csv')
right = pd.read_csv('C:\\Akash\\2018ElectionPrediction\\censusData.csv')

merged = pd.merge(left, right, how='left', on=['state', 'year'])

merged.to_csv("C:\\Akash\\2018ElectionPrediction\\Training_Data_Census.csv")