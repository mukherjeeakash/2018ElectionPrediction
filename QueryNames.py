import pandas

senateData = pandas.read_csv('senate-candidate-2018.csv')

#Names appear in the following format: 'lastName, firstName nickname(if it exists) middleName/initial'
#We want to extract the first and last names for each candidate and store it as 'firstName lastName'
queryNames = []
for name in senateData['Cand_Name']:
    lastNameLength = name.find(",")
    lastName = name[ : lastNameLength]
    firstName = name[lastNameLength + 1: ].split()[0]
    queryNames.append(firstName + " " + lastName)

#Append queryNames to dataframe and save updated csv file
senateData['Query_Name'] = queryNames
senateData.to_csv('updated-senate-data.csv')
