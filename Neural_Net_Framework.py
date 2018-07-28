import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Define the input of our model
x = tf.placeholder(tf.float32, [None, 100])   #100 is just a placeholder; Idk how many features we're dealing with 

#Define the model parameters (weights and biases):
W = tf.Variable(tf.zeros([100, 2]))  #This is just a two-layer neural net for now
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
for _ in range(1000):
  batch_xs, batch_ys = #INSERT TRAINING DATA HERE!!!!!!!!!!!!!!!!!!!
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
  
#Find out which of our predictions are correct:
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1)) 
                                                               
#Calculate the accuracy of our model:
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) 

#Print the results of our model:
print(sess.run(accuracy, feed_dict={#INSERT TEST DATA HERE!!!!!!}))