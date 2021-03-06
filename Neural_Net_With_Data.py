import tensorflow as tf
import numpy as np
import os
import pandas as pd
from pandas import DataFrame
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Gather data from excel:
df = pd.read_excel("Training_Data.xlsx", sheetname = "Sheet1")
state = df["STATE ABBREVIATION"]
incumbent_status = df["(I)"]
party = df["PARTY"]
pres_party = df["PRES PARTY"]
outcome = df["GE WINNER INDICATOR"]
year = df["YEAR"]
state_dict = {}  #The dictionries contain all unique instances of a variable and assign them a unique integer
incumb_status_dict = {}
party_dict = {}
pres_party_dict = {}
outcome_dict = {}
year_dict = {}
state_num = []  #The "num" list contains the data in numerical form
                #For example, state_num represents states as different integers
incumb_status_num = []
party_num = []
pres_party_num = []
outcome_num = [[],[]]
year_num = []

rows = len(state)
a = 0
b = 0
c = 0
d = 0
e = 0 
f = 0

###################################
#Populate dictionaries:
for i in state.tolist():
    if i in state_dict.keys():
        pass
    else:
       state_dict[i] = a
       a += 1
for i in incumbent_status.tolist():
    if i in incumb_status_dict.keys():
        pass
    else:
       incumb_status_dict[i] = b
       b += 1
for i in party.tolist():
    if i in party_dict.keys():
        pass
    else:
       party_dict[i] = c
       c += 1
for i in pres_party.tolist():
    if i in pres_party_dict.keys():
        pass
    else:
       pres_party_dict[i] = d
       d += 1
for i in outcome.tolist():
    if i in outcome_dict.keys():
        pass
    else:
       outcome_dict[i] = e
       e += 1
for i in year.tolist():
    if i in year_dict.keys():
        pass
    else:
       year_dict[i] = f
       f += 1
       
#Use dictionaries to convert data to numbers:
#state_num = list(state_dict.values())
#incumb_status_num = list(incumb_status_dict.values())
#party_num = list(party_dict.values())
#pres_party_num = list(pres_party_dict.values())
#outcome_num = list(outcome_dict.values())
#year_num = list(year_dict.values())
for x in state.tolist():
    state_num.append(state_dict[x])
for x in incumbent_status.tolist():
    incumb_status_num.append(incumb_status_dict[x])
for x in party.tolist():
    party_num.append(party_dict[x])
for x in pres_party.tolist():
    pres_party_num.append(pres_party_dict[x])
for x in year.tolist():
    year_num.append(year_dict[x])
for x in outcome.tolist():
    if x == "W":
        outcome_num[0].append(0)
        outcome_num[1].append(1)
    else:
        outcome_num[0].append(1)
        outcome_num[1].append(0)
    
####################################

#Sanity Checks:
print(pres_party_dict)
print(party_dict)
print(party_num)
print(type(party_num))
#print(state_dict)
print(outcome_num)


#Define the input of our model
x = tf.placeholder(tf.float32, [None, 5])   #5 Features: Party, year, incumbent status,
                                            #presidential party, state
inputArray = np.array([state_num, incumb_status_num, party_num, pres_party_num, year_num])
outputArray = np.array([outcome_num])
inputArray = inputArray.reshape(1106, 5)
outputArray = outputArray.reshape(1106, 2)
print(inputArray.shape)
print(outputArray.shape)

#Define the model parameters (weights and biases):
W = tf.Variable(tf.zeros([5, 2]))  #This is just a two-layer neural net for now
b = tf.Variable(tf.zeros([2]))       #The 2 is for 2 parties: Rep. and Dem.

#Predict the label (party of winner) for each example:
y = tf.nn.softmax(tf.matmul(x, W) + b)  

#Input the actual labels:
y_ = tf.placeholder(tf.float32, [None, 2])

#loss function:
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))  


#Training model (Gradient Descent):
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy) #Learning Rate = 0.5


#Define session
sess = tf.InteractiveSession()

#Initialize variables:
tf.global_variables_initializer().run()

#Input the training data to train our model
sess.run(train_step, feed_dict={x: inputArray, y_: outputArray})
  
#Find out which of our predictions are correct:
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1)) 
                                                               
#Calculate the accuracy of our model:
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) 

#Print the results of our model:
print(sess.run(accuracy, feed_dict={x: inputArray, y_: outputArray}))